# dataStream.py
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QObject, Slot
from Crypto.Cipher import AES
from Crypto.Util import Counter
from PySide6.QtGui import QTextCursor
import os

class DataStream(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # Stały klucz AES (16 bajtów dla AES-128)
        self.key = b'StandaryKey12345'
        if len(self.key) not in (16, 24, 32):
            raise ValueError("Klucz AES musi mieć długość 16, 24 lub 32 bajty.")

        # Inicjalizacja cipher dla użytkownika A i B
        self.ciphers = {}
        self.initialize_cipher('A')
        self.initialize_cipher('B')

        # Śledzenie poprzedniego tekstu w inputA i inputB
        self.last_text = {'A': "", 'B': ""}

        # Śledzenie, czy użytkownik ma aktualnie aktywną wiadomość
        self.current_messages = {'A': False, 'B': False}

        # Śledzenie kursorów per użytkownik
        self.user_cursors = {'A': None, 'B': None}

        # Flaga blokująca przetwarzanie podczas aktualizacji UI
        self.updating_message = False

        self.setup_connections()

    def initialize_cipher(self, user):
        nonce = os.urandom(8)  # 64-bitowy nonce
        counter = Counter.new(64, prefix=nonce)
        self.ciphers[user] = AES.new(self.key, AES.MODE_CTR, counter=counter)

    def setup_connections(self):
        # Połączenie przycisków "Wyślij" z metodą send_message
        self.main_window.sendButtonA.clicked.connect(lambda: self.send_message('A'))
        self.main_window.sendButtonB.clicked.connect(lambda: self.send_message('B'))

        # Połączenie sygnałów textChanged z metodami obsługi
        self.main_window.inputA.textChanged.connect(lambda: self.on_input_changed('A'))
        self.main_window.inputB.textChanged.connect(lambda: self.on_input_changed('B'))

    @Slot()
    def on_input_changed(self, user):
        """
        Obsługuje zmiany tekstu w inputA i inputB w czasie rzeczywistym.
        Aktualizuje wyświetlaną wiadomość jako całość.
        """
        if self.updating_message:
            return

        try:
            # Pobierz bieżący tekst
            current_text = self.main_window.inputA.text() if user == 'A' else self.main_window.inputB.text()
            last_text = self.last_text[user]
            self.last_text[user] = current_text

            if len(current_text) < len(last_text):
                # Użytkownik usunął tekst, resetuj wiadomość
                if self.current_messages[user]:
                    self.remove_current_message(user)
                self.current_messages[user] = False
                return

            new_text = current_text[len(last_text):]

            if new_text:
                if not self.current_messages[user]:
                    # Inicjalizuj nowy stream dla użytkownika
                    self.initialize_cipher(user)
                    self.current_messages[user] = True
                    self.append_new_message(user)

                encrypted = self.encrypt_stream(user, new_text)
                decrypted = new_text  # Wyświetlamy oryginalny tekst

                self.updating_message = True
                self.append_to_message(user, decrypted)
                self.updating_message = False

        except Exception as e:
            QMessageBox.critical(self.main_window, "Błąd", f"Wystąpił błąd podczas szyfrowania: {str(e)}")

    def append_new_message(self, user):
        """
        Dodaje nową linię wiadomości dla użytkownika i zapisuje kursor.
        """
        message = f"Użytkownik {user}: "
        self.main_window.messagesTextEdit.append(message)
        # Uzyskaj kursor na końcu nowej wiadomości
        cursor = self.main_window.messagesTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.main_window.messagesTextEdit.setTextCursor(cursor)
        self.user_cursors[user] = cursor

    def append_to_message(self, user, decrypted_message):
        """
        Dodaje tekst do aktualnej wiadomości użytkownika.
        """
        cursor = self.user_cursors[user]
        if cursor:
            cursor.insertText(decrypted_message)
            # Przenieś kursor na koniec
            cursor.movePosition(QTextCursor.End)
            self.main_window.messagesTextEdit.setTextCursor(cursor)

        # Aktualizacja statusu
        print(f"Wiadomość od Użytkownika {user} jest szyfrowana.")

    def remove_current_message(self, user):
        """
        Usuwa aktualną wiadomość użytkownika z messagesTextEdit.
        """
        search = f"Użytkownik {user}:"
        document = self.main_window.messagesTextEdit.document()
        block = document.lastBlock()

        while block.isValid():
            text = block.text()
            if text.startswith(search):
                cursor = QTextCursor(block)
                cursor.select(QTextCursor.BlockUnderCursor)
                cursor.removeSelectedText()
                break
            block = block.previous()

    @Slot()
    def send_message(self, user):
        """
        Finalizuje stream po kliknięciu przycisku "Wyślij".
        Czyści pole tekstowe i resetuje śledzenie wiadomości.
        """
        # Najpierw ustawiamy current_messages na False, aby zasygnalizować zakończenie wiadomości
        self.current_messages[user] = False

        if user == 'A':
            self.main_window.inputA.clear()
            self.last_text[user] = ""
        elif user == 'B':
            self.main_window.inputB.clear()
            self.last_text[user] = ""

        # Reinitialize cipher for the next message
        self.initialize_cipher(user)

        # Aktualizacja statusu
        print(f"Stream od Użytkownika {user} został zakończony.")

    def encrypt_stream(self, user, data):
        """
        Szyfruje dane w trybie strumieniowym dla danego użytkownika.
        """
        return self.ciphers[user].encrypt(data.encode('utf-8'))

    def decrypt_stream(self, user, encrypted_data):
        """
        Odszyfrowuje dane w trybie strumieniowym dla danego użytkownika.
        (Może być użyteczne, jeśli potrzebujesz odszyfrować dane)
        """
        return self.ciphers[user].decrypt(encrypted_data).decode('utf-8', errors='ignore')
