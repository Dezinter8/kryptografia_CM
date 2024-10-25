import socket
import threading
import time
import os
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, QObject
from Ui.networkDevicesForm import Ui_Form

class Network(QObject):
    device_found_signal = Signal(dict)      # Definiujemy sygnał, który emituje słownik zawierający informacje o urządzeniu
    connection_request_signal = Signal(str) # Sygnał do przekazywania IP przychodzącego żądania połączenia

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.port = 50001
        self.request_port = 50002  # Port na żądania połączeń
        self.broadcast_interval = 2  # Czas między broadcastami w sekundach
        self.devices = {}  # Przechowuje dostępne urządzenia w formacie {IP: "Nazwa"}
        self.device_widgets = {}  # Słownik do przechowywania widgetów dla unikalnych IP
        self.running = True  # Flaga kontrolująca działanie wątków
        
        self.host_name = socket.gethostname()
        self.host_ip = self.get_host_ip_address()

        # Wprowadzenie danych hosta do pól tekstowych
        self.update_host_info()

        # Połączenie przycisku do metody wyszukiwania
        self.main_window.network_search_button.clicked.connect(self.start_network_discovery)

        # Podłączamy sygnał do metody dodającej widget urządzenia
        self.device_found_signal.connect(self.add_device_widget)
        self.connection_request_signal.connect(self.show_connection_request)  # Nowy sygnał



    def get_host_ip_address(self):
        # Uzyskanie listy interfejsów sieciowych
        if os.name == 'posix':
            # W systemach Unix
            ip_addresses = []
            for line in os.popen('ip addr show').read().splitlines():
                if 'inet ' in line and not '127.' in line:
                    ip = line.split()[1]
                    ip_addresses.append(ip)
                    # Dzielimy adres IP na część przed i po znaku '/'
                    ip_address = ip_addresses[0].split('/')[0]
            return ip_address if ip_addresses else "Brak adresu IP"
        else:
            # Dla innych systemów, np. Windows
            return socket.gethostbyname(socket.gethostname())

    def update_host_info(self):
        """Aktualizuje informacje o hoście w interfejsie."""
        self.main_window.host_user_name.setText(self.host_name)
        self.main_window.host_user_ip.setText(self.host_ip)


    def start_network_discovery(self):
        """Rozpoczyna proces wyszukiwania innych aplikacji w sieci."""
        # Start wątków broadcast i nasłuchiwania
        self.broadcast_thread = threading.Thread(target=self.broadcast_presence)
        self.listener_thread = threading.Thread(target=self.start_broadcast_listener)
        # Start wątku do odbierania żądań połączeń
        self.connection_listener_thread = threading.Thread(target=self.receive_connection_request)

        self.broadcast_thread.start()
        self.listener_thread.start()
        self.connection_listener_thread.start()



    def broadcast_presence(self):
        """Cyklicznie wysyła wiadomości broadcast na porcie 50001."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.settimeout(self.broadcast_interval)

            while self.running:
                try:
                    message = "Hello from {}".format(self.host_name)
                    sock.sendto(message.encode(), ('<broadcast>', self.port))
                    print("Broadcast sent: ", message)
                except Exception as e:
                    print("Error broadcasting:", e)
                time.sleep(self.broadcast_interval)

    def start_broadcast_listener(self):
        """Nasłuchuje broadcastów na porcie 50001 i emituje sygnał przy znalezieniu nowego urządzenia."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind(('', self.port))
            sock.settimeout(1)  # Ustaw timeout, aby obsługiwać flagę `running` i umożliwić zatrzymanie wątku
            
            while self.running:
                try:
                    data, addr = sock.recvfrom(1024)
                    ip_address = addr[0]
                    message = data.decode()

                    if ip_address not in self.devices:
                        device_name = message.replace("Hello from ", "")

                        # Dodaje nowe urządzenie do listy i emituje sygnał
                        self.devices[ip_address] = message
                        device_info = {"ip_address": ip_address, "device_name": device_name}
                        self.device_found_signal.emit(device_info)
                        print(f"Discovered device: {ip_address} - {device_name}")

                except socket.timeout:
                    continue  # Timeout służy tylko do utrzymania sprawdzania flagi `running`
                except Exception as e:
                    print("Error listening for broadcasts:", e)

    def add_device_widget(self, device_info):
        """Dodaje widget z informacjami o urządzeniu do UI."""
        ip_address = device_info["ip_address"]
        device_name = device_info["device_name"]

        # Sprawdza, czy widget dla danego IP już istnieje
        if ip_address in self.device_widgets or ip_address == self.host_ip:
            return  # Już dodano widget

        # Tworzy nowy widget dla urządzenia
        device_widget = QWidget()
        device_ui = Ui_Form()
        device_ui.setupUi(device_widget)

        # Ustawia teksty i przyciski w interfejsie widgetu
        device_ui.Client_name_label.setText(device_name)
        device_ui.Client_ip_label.setText(ip_address)
        device_ui.Client_connect_pushButton.setText("Połącz")

        # Podłącz przycisk "Połącz" do funkcji inicjującej połączenie
        device_ui.Client_connect_pushButton.clicked.connect(
            lambda _, ip=ip_address: self.request_connection(ip)
        )

        # Dodaje widget do layoutu listy urządzeń w głównym oknie
        self.main_window.devicesList_widget.layout().addWidget(device_widget)

        # Dodaje widget do słownika, aby nie dublować urządzeń o tym samym IP
        self.device_widgets[ip_address] = device_widget

    def request_connection(self, target_ip):
        """Inicjuje żądanie połączenia do wybranego urządzenia."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.sendto(f"Connection request from {self.host_ip}".encode(), (target_ip, self.request_port))
            print(f"Connection request sent to {target_ip}")
        except Exception as e:
            print("Error requesting connection:", e)

    def receive_connection_request(self):
        """Nasłuchuje żądań połączenia i emituje sygnał do wyświetlenia zapytania o akceptację połączenia."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind(('', self.request_port))
            sock.settimeout(1)

            while self.running:
                try:
                    data, addr = sock.recvfrom(1024)
                    sender_ip = addr[0]
                    message = data.decode()

                    if "Connection request" in message:
                        # Emituje sygnał do głównego wątku, aby wyświetlić QMessageBox
                        self.connection_request_signal.emit(sender_ip)

                except socket.timeout:
                    continue
                except Exception as e:
                    print("Error receiving connection request:", e)

    def show_connection_request(self, sender_ip):
        """Wyświetla QMessageBox z zapytaniem o akceptację połączenia."""
        response = QMessageBox.question(
            self.main_window,
            "Request Connection",
            f"{sender_ip} wants to connect. Accept?",
            QMessageBox.Yes | QMessageBox.No
        )

        if response == QMessageBox.Yes:
            self.confirm_connection(sender_ip)
        else:
            self.decline_connection(sender_ip)

    def confirm_connection(self, sender_ip):
        """Potwierdza połączenie do urządzenia wysyłającego żądanie."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.sendto("Connection accepted".encode(), (sender_ip, self.request_port))
            print(f"Connection accepted with {sender_ip}")
        except Exception as e:
            print("Error confirming connection:", e)

    def decline_connection(self, sender_ip):
        """Odrzuca połączenie z urządzenia wysyłającego żądanie."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.sendto("Connection declined".encode(), (sender_ip, self.request_port))
            print(f"Connection declined with {sender_ip}")
        except Exception as e:
            print("Error declining connection:", e)


    def stop(self):
        """Zatrzymuje broadcast i nasłuchiwanie."""
        self.running = False
        self.broadcast_thread.join()
        self.listener_thread.join()
        self.connection_listener_thread.join()

