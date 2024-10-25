import socket
import threading
import time

class Network():

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.port = 50001
        self.broadcast_interval = 2  # Czas między broadcastami w sekundach
        self.devices = {}  # Przechowuje dostępne urządzenia w formacie {IP: "Nazwa"}
        self.running = True  # Flaga kontrolująca działanie wątków


        # Połączenie przycisku do metody wyszukiwania
        self.main_window.network_search_button.clicked.connect(self.start_network_discovery)


    def start_network_discovery(self):
        """Rozpoczyna proces wyszukiwania innych aplikacji w sieci."""
        # Start wątków broadcast i nasłuchiwania
        threading.Thread(target=self.broadcast_presence).start()
        threading.Thread(target=self.start_broadcast_listener).start()


    def broadcast_presence(self):
        """Cyklicznie wysyła wiadomości broadcast na porcie 50001."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.settimeout(self.broadcast_interval)

            while self.running:
                try:
                    message = "Hello from {}".format(socket.gethostbyname(socket.gethostname()))
                    sock.sendto(message.encode(), ('<broadcast>', self.port))
                    print("Broadcast sent: ", message)
                except Exception as e:
                    print("Error broadcasting:", e)
                time.sleep(self.broadcast_interval)

    def start_broadcast_listener(self):
        """Nasłuchuje broadcastów na porcie 50001 i dodaje nowe urządzenia do listy."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind(('', self.port))
            sock.settimeout(1)  # Ustaw timeout, aby obsługiwać flagę `running` i umożliwić zatrzymanie wątku
            
            while self.running:
                try:
                    data, addr = sock.recvfrom(1024)
                    ip_address = addr[0]
                    message = data.decode()

                    if ip_address not in self.devices:
                        # Dodaje nowe urządzenie do listy
                        self.devices[ip_address] = message
                        self.update_main_window()
                        print(f"Discovered device: {ip_address} - {message}")

                except socket.timeout:
                    continue  # Timeout służy tylko do utrzymania sprawdzania flagi `running`
                except Exception as e:
                    print("Error listening for broadcasts:", e)

    def update_main_window(self):
        """Aktualizuje GUI na podstawie wykrytych urządzeń."""
        # Placeholder: Funkcja ta powinna odświeżać listę urządzeń w GUI,
        # np. przez wywołanie funkcji w main_window do zaktualizowania widgetów
        pass

    def stop(self):
        """Zatrzymuje broadcast i nasłuchiwanie."""
        self.running = False
        self.broadcast_thread.join()
        self.listener_thread.join()
