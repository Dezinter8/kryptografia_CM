import socket
import threading
from PySide6.QtWidgets import QWidget
from Ui.networkDevicesForm import Ui_Form

class Network:
    def __init__(self, main_window):
        self.main_window = main_window
        self.server_socket = None
        self.client_socket = None
        self.is_server = False
        self.connected = False
        self.host_ip = self.get_host_ip()
        self.host_name = socket.gethostname()
        self.port = 12345  # Port do komunikacji


        self.main_window.automatic_connect_pushButton.clicked.connect(lambda: self.switch_network_page(0))
        self.main_window.manual_connect_pushButton.clicked.connect(lambda: self.switch_network_page(1))

        # Inicjalizuj dynamiczne elementy interfejsu
        # self.init_network_devices()

        # Połączenie przycisku do metody wyszukiwania
        self.main_window.network_search_button.clicked.connect(self.start_network_discovery)


    def switch_network_page(self, index):
        self.main_window.network_mode_stackedWidget.setCurrentIndex(index)

    def init_network_devices(self):
        # Przykładowe dane urządzeń
        device_data = [
            {"name": "Device 1", "ip": "192.168.0.2", "status": "Dostępny"},
            {"name": "Device 2", "ip": "192.168.0.3", "status": "Połączono"},
            {"name": "Device 3", "ip": "192.168.0.4", "status": "Dostępny"}
        ]

        # Przez każde urządzenie dodaj widget do `automatic_page`
        for device in device_data:
            self.add_device_widget(device)

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
        self.update_host_info()
        # Startujemy wątki do wyszukiwania i nasłuchiwania
        threading.Thread(target=self.start_server, daemon=True).start()
        threading.Thread(target=self.discover_devices, daemon=True).start()

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
                self.add_device_widget({"name": client_address[0], "ip": client_address[0], "status": "Połączono"})
            except Exception as e:
                print(f"Błąd serwera: {e}")

    def discover_devices(self):
        """Wysyła broadcast w celu znalezienia innych urządzeń w sieci."""
        discovery_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        discovery_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        message = f"DISCOVER:{self.host_ip}".encode()

        while not self.connected:
            discovery_socket.sendto(message, ("<broadcast>", self.port))
            try:
                data, address = discovery_socket.recvfrom(1024)
                if data.startswith(b"DISCOVER"):
                    if address[0] != self.host_ip:
                        # Znaleziono inny host, spróbuj połączyć się jako klient
                        threading.Thread(target=self.connect_to_server, args=(address[0],), daemon=True).start()
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
            self.add_device_widget({"name": server_ip, "ip": server_ip, "status": "Połączono"})
        except Exception as e:
            print(f"Błąd połączenia z serwerem: {e}")

    def add_device_widget(self, device_info):
        """Dodaje widget z informacjami o urządzeniu do UI."""
        device_widget = QWidget()
        device_ui = Ui_Form()
        device_ui.setupUi(device_widget)

        device_ui.User_name_label.setText(device_info["name"])
        device_ui.User_ip_label.setText(device_info["ip"])
        device_ui.User_status_label.setText(device_info["status"])
        device_ui.User_label_pushButton.setText("Rozłącz" if device_info["status"] == "Połączono" else "Połącz")

        self.main_window.devicesList_widget.layout().addWidget(device_widget)
