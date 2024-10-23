import socket
import threading
import time
from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QWidget
from Ui.networkDevicesForm import Ui_Form

class Network(QObject):
    device_found_signal = Signal(dict)

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.server_socket = None
        self.client_socket = None
        self.is_server = False
        self.connected = False
        self.host_ip = self.get_host_ip()
        self.host_name = socket.gethostname()
        self.port = 50000  # Port do komunikacji
        self.discovery_port = 50001  # Osobny port dla komunikacji discovery
        
        self.device_widgets = {}  # Przechowujemy referencje do widgetów na podstawie IP
        self.searching = False  # Flaga do kontrolowania wyszukiwania
        self.cooldown_duration = 2  # Czas cooldownu w sekundach


        self.main_window.automatic_connect_pushButton.clicked.connect(lambda: self.switch_network_page(0))
        self.main_window.manual_connect_pushButton.clicked.connect(lambda: self.switch_network_page(1))

        # Połączenie przycisku do metody wyszukiwania
        self.main_window.network_search_button.clicked.connect(self.start_network_discovery)

        # Podłączamy sygnał do metody dodającej widget urządzenia
        self.device_found_signal.connect(self.add_device_widget)


    def switch_network_page(self, index):
        """Zmiana strony w trybie połączenia sieciowego."""
        self.main_window.network_mode_stackedWidget.setCurrentIndex(index)

    def get_host_ip(self):
        """Pobiera lokalny adres IP hosta."""
        try:
            # Tworzymy tymczasowe połączenie, aby uzyskać lokalny adres IP.
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception as e:
            print(f"Błąd podczas pobierania adresu IP: {e}")
            return "127.0.0.1"

    def start_network_discovery(self):
        """Rozpoczyna proces wyszukiwania innych aplikacji w sieci."""
        if self.searching:
            print("Wyszukiwanie już w toku, czekam na cooldown...")
            return  # Nie rozpoczynaj ponownie wyszukiwania, jeśli już trwa

        self.searching = True  # Ustaw flagę na true
        self.update_host_info()

        # Startujemy wątki do wyszukiwania i nasłuchiwania
        threading.Thread(target=self.start_server, daemon=True).start()
        threading.Thread(target=self.listen_for_discovery, daemon=True).start()
        threading.Thread(target=self.send_discovery_message, daemon=True).start()

        # Cooldown po zakończeniu wyszukiwania
        threading.Thread(target=self.cooldown_search, daemon=True).start()

    def cooldown_search(self):
        """Czeka przez określony czas, aby nie wyszukiwać ponownie zbyt szybko."""
        time.sleep(self.cooldown_duration)
        self.searching = False  # Zwalnia flagę po upływie cooldownu

    def update_host_info(self):
        """Aktualizuje informacje o hoście w interfejsie."""
        self.main_window.host_user_name.setText(self.host_name)
        self.main_window.host_user_ip.setText(self.host_ip)

    def start_server(self):
        """Uruchamia serwer, który nasłuchuje na połączenia."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host_ip, self.port))
        self.server_socket.listen(1)
        print(f"Serwer nasłuchuje na {self.host_ip}:{self.port}")

        while not self.connected:
            try:
                client_socket, client_address = self.server_socket.accept()
                print(f"Połączono z {client_address}")
                self.client_socket = client_socket
                self.is_server = True
                self.connected = True
                
                # Pobranie nazwy hosta na podstawie adresu IP
                try:
                    client_name = socket.gethostbyaddr(client_address[0])[0]
                except socket.herror:
                    # Jeśli nie uda się pobrać nazwy hosta, użyj adresu IP jako nazwy
                    client_name = client_address[0]

                # Emitujemy sygnał z nazwą hosta i adresem IP
                self.device_found_signal.emit({
                    "name": client_name,
                    "ip": client_address[0],
                    "status": "Połączono"
                })
            except Exception as e:
                print(f"Błąd serwera: {e}")

    def listen_for_discovery(self):
        """Nasłuchuje na broadcast DISCOVER i odpowiada na niego."""
        discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        discovery_socket.bind(("", self.discovery_port))

        while not self.connected:
            try:
                data, address = discovery_socket.recvfrom(1024)
                if data.startswith(b"DISCOVER"):
                    print(f"Otrzymano DISCOVER od {address[0]}")
                    if address[0] != self.host_ip:
                        # Odpowiedz na DISCOVER, że jesteśmy tutaj
                        response = f"RESPONSE:{self.host_ip}".encode()
                        discovery_socket.sendto(response, address)
            except Exception as e:
                print(f"Błąd nasłuchiwania DISCOVER: {e}")


    def send_discovery_message(self):
        """Wysyła broadcast DISCOVER, aby znaleźć inne urządzenia w sieci."""
        discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        message = f"DISCOVER:{self.host_ip}".encode()

        while not self.connected:
            discovery_socket.sendto(message, ("<broadcast>", self.discovery_port))
            print("Wysłano DISCOVER broadcast")
            try:
                discovery_socket.settimeout(2)
                data, address = discovery_socket.recvfrom(1024)
                if data.startswith(b"RESPONSE"):
                    print(f"Otrzymano odpowiedź od {address[0]}")
                    if address[0] != self.host_ip:
                        # Emitujemy sygnał znalezionego urządzenia, aby je wyświetlić w GUI
                        self.device_found_signal.emit({
                            "name": address[0],
                            "ip": address[0],
                            "status": "Dostępny"
                        })
            except socket.timeout:
                continue



    def connect_to_server(self, server_ip):
        """Próbuje połączyć się do znalezionego serwera."""
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, self.port))
            print(f"Połączono z serwerem {server_ip}")
            self.client_socket = client_socket
            self.connected = True
            self.is_server = False

            # Pobranie nazwy hosta na podstawie adresu IP
            try:
                server_name = socket.gethostbyaddr(server_ip)[0]
            except socket.herror:
                server_name = server_ip

            # Emitujemy sygnał z nazwą hosta i adresem IP
            self.device_found_signal.emit({
                "name": server_name,
                "ip": server_ip,
                "status": "Połączono"
            })
        except Exception as e:
            print(f"Błąd połączenia z serwerem: {e}")





    def add_device_widget(self, device_info):
        """Dodaje widget z informacjami o urządzeniu do UI."""
        # Sprawdzenie, czy widget dla danego IP już istnieje
        if device_info["ip"] in self.device_widgets:
            return  # Już dodano widget, więc kończymy

        device_widget = QWidget()
        device_ui = Ui_Form()
        device_ui.setupUi(device_widget)

        device_ui.Client_name_label.setText(device_info["name"])
        device_ui.Client_ip_label.setText(device_info["ip"])
        device_ui.Client_status_label.setText(device_info["status"])
        device_ui.Client_connect_pushButton.setText("Połącz")

        # Przechowujemy widget w słowniku na podstawie adresu IP
        self.device_widgets[device_info["ip"]] = device_ui

        # Przypisujemy akcję do przycisku "Połącz"
        device_ui.Client_connect_pushButton.clicked.connect(
            lambda: self.initiate_connection(device_info["ip"])
        )

        # Dodajemy widget do listy urządzeń
        self.main_window.devicesList_widget.layout().addWidget(device_widget)

    def initiate_connection(self, server_ip):
        """Rozpoczyna proces łączenia się z wybranym urządzeniem po kliknięciu przycisku."""
        threading.Thread(target=self.connect_to_server, args=(server_ip,), daemon=True).start()

        # Po nawiązaniu połączenia, zmieniamy status w UI na "Łączenie..."
        self.update_device_status(server_ip, "Łączenie...")

    def update_device_status(self, ip, status):
        """Aktualizuje status urządzenia w UI na podstawie adresu IP."""
        device_ui = self.device_widgets.get(ip)
        if device_ui:
            device_ui.Client_status_label.setText(status)
            device_ui.Client_connect_pushButton.setText("Rozłącz" if status == "Połączono" else "Połącz")
