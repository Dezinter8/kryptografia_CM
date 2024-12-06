from PySide6.QtWidgets import QFileDialog, QMessageBox
import cryptography
from cryptography.hazmat.primitives import hashes, hmac as crypto_hmac
from cryptography.hazmat.primitives import serialization, keywrap
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os

class Hmac:
    def __init__(self, main_window):
        self.main_window = main_window

        # Połączenie przycisków z funkcjami
        self.main_window.computeHmac_pushButton.clicked.connect(self.compute_hmac)
        self.main_window.verifyHmac_pushButton.clicked.connect(self.verify_hmac)
        self.main_window.generateKey_pushButton.clicked.connect(self.generate_random_key)

    def compute_hmac(self):
        message = self.main_window.messageInput_lineEdit.text()
        key = self.main_window.keyInput_lineEdit.text()
        algorithm = self.main_window.hmacAlgorithm_comboBox.currentText()

        if not message or not key:
            QMessageBox.warning(self.main_window, "Błąd", "Wiadomość i klucz muszą być wypełnione!")
            return

        # Wybór algorytmu
        try:
            if algorithm == "HMAC-SHA1":
                hash_algo = hashes.SHA1()
            elif algorithm == "HMAC-SHA256":
                hash_algo = hashes.SHA256()
            elif algorithm == "HMAC-SHA512":
                hash_algo = hashes.SHA512()
            else:
                QMessageBox.warning(self.main_window, "Błąd", "Nieznany algorytm HMAC!")
                return

            # Tworzenie obiektu HMAC
            h = crypto_hmac.HMAC(key.encode(), hash_algo, backend=default_backend())
            h.update(message.encode())
            hmac_result = h.finalize()

            # Wyświetlanie HMAC w formacie hex
            self.main_window.computedHmac_output.setText(hmac_result.hex())
            print("HMAC wygenerowany.")
        except Exception as e:
            QMessageBox.warning(self.main_window, "Błąd", f"Nie udało się wygenerować HMAC: {str(e)}")

    def verify_hmac(self):
        message = self.main_window.verifyMessageInput_lineEdit.text()
        key = self.main_window.verifyKeyInput_lineEdit.text()
        input_hmac = self.main_window.verifyHmacInput_lineEdit.text()
        algorithm = self.main_window.verifyHmacAlgorithm_comboBox.currentText()

        if not message or not key or not input_hmac:
            QMessageBox.warning(self.main_window, "Błąd", "Wiadomość, klucz i HMAC muszą być wypełnione!")
            return

        # Wybór algorytmu
        try:
            if algorithm == "HMAC-SHA1":
                hash_algo = hashes.SHA1()
            elif algorithm == "HMAC-SHA256":
                hash_algo = hashes.SHA256()
            elif algorithm == "HMAC-SHA512":
                hash_algo = hashes.SHA512()
            else:
                QMessageBox.warning(self.main_window, "Błąd", "Nieznany algorytm HMAC!")
                return

            # Tworzenie obiektu HMAC do weryfikacji
            h = crypto_hmac.HMAC(key.encode(), hash_algo, backend=default_backend())
            h.update(message.encode())

            # Konwersja wprowadzonego HMAC z hex na bytes
            try:
                input_hmac_bytes = bytes.fromhex(input_hmac)
            except ValueError:
                QMessageBox.warning(self.main_window, "Błąd", "HMAC powinien być w formacie hex!")
                return

            # Weryfikacja HMAC
            try:
                h.verify(input_hmac_bytes)
                verification_result = "HMAC jest prawidłowy."
            except cryptography.exceptions.InvalidSignature:
                verification_result = "HMAC jest nieprawidłowy."

            # Wyświetlanie wyniku weryfikacji
            self.main_window.verifyHmacOutput_textEdit.setPlainText(verification_result)
            print("Weryfikacja HMAC zakończona.")
        except Exception as e:
            QMessageBox.warning(self.main_window, "Błąd", f"Nie udało się zweryfikować HMAC: {str(e)}")

    def generate_random_key(self):
        # Generowanie losowego klucza (np. 32 bajty dla HMAC-SHA256)
        key_length = 32
        random_key = os.urandom(key_length)
        self.main_window.keyInput_lineEdit.setText(random_key.hex())
        self.main_window.verifyKeyInput_lineEdit.setText(random_key.hex())
        print("Losowy klucz wygenerowany.")
