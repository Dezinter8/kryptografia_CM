import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from PySide6.QtWidgets import QMessageBox, QFileDialog

class Rsa:
    def __init__(self, main_window):
        self.main_window = main_window

        self.loaded_text = ''
        self.loaded_cipher_text = ''
        
        self.key = None
        self.public_key = None

        # Obsługa przycisków zmieniających tryb pracy rsa
        self.main_window.rsa_normalMode_button.clicked.connect(lambda: self.switch_rsa_page(0))
        self.main_window.rsa_allFileMode_button.clicked.connect(lambda: self.switch_rsa_page(1))

        # Obsługa przycisków szyfrowania rsa
        self.main_window.rsa_generateKey_pushButton.clicked.connect(self.generate_keys)
        self.main_window.rsa_cipher_button.clicked.connect(self.encrypt_text)
        self.main_window.rsa_decipher_button.clicked.connect(self.decrypt_text)
        self.main_window.rsa_cipherFile_button.clicked.connect(self.encrypt_file)
        self.main_window.rsa_decipherFile_button.clicked.connect(self.decrypt_file)


        # Obsługa przycisków zapisania i wczytania kluczy
        self.main_window.rsa_save_publicKey_pushButton.clicked.connect(self.save_public_key)
        self.main_window.rsa_save_privateKey_pushButton.clicked.connect(self.save_private_key)
        self.main_window.rsa_load_publicKey_pushButton.clicked.connect(self.load_public_key)
        self.main_window.rsa_load_privateKey_pushButton.clicked.connect(self.load_private_key)




    def switch_rsa_page(self, index):
        self.main_window.stackedWidget_rsa.setCurrentIndex(index)

    # Dodawanie zakodowanych plikow base64 do zmiennej
    def text_update(self, text):
        self.loaded_text = text
        print("tekst zostal zczytany")

    # Dodawanie zawartosci plikow do zmiennej
    def cipher_text_update(self, text):
        self.loaded_cipher_text = text
        print("zaszyfrowany tekst zostal zczytany")


















    def save_public_key(self):
        if not self.public_key:
            QMessageBox.warning(
                self.main_window,
                "Brak klucza publicznego",
                "Najpierw wygeneruj lub załaduj klucz publiczny."
            )
            return
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self.main_window,
            "Zapisz Klucz Publiczny",
            "",
            "PEM Files (*.pem);;All Files (*)",
            options=options
        )
        if file_name:
            try:
                with open(file_name, 'wb') as f:
                    f.write(self.public_key.export_key())
                print("Klucz publiczny zapisany pomyślnie.")
            except Exception as e:
                QMessageBox.critical(
                    self.main_window,
                    "Błąd",
                    f"Nie udało się zapisać klucza publicznego: {str(e)}"
                )
                print("Błąd podczas zapisywania klucza publicznego.")

    def save_private_key(self):
        if not self.key:
            QMessageBox.warning(
                self.main_window,
                "Brak klucza prywatnego",
                "Najpierw wygeneruj lub załaduj klucz prywatny."
            )
            return
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self.main_window,
            "Zapisz Klucz Prywatny",
            "",
            "PEM Files (*.pem);;All Files (*)",
            options=options
        )
        if file_name:
            try:
                with open(file_name, 'wb') as f:
                    f.write(self.key.export_key())
                print("Klucz prywatny zapisany pomyślnie.")
            except Exception as e:
                QMessageBox.critical(
                    self.main_window,
                    "Błąd",
                    f"Nie udało się zapisać klucza prywatnego: {str(e)}"
                )
                print("Błąd podczas zapisywania klucza prywatnego.")

    def load_public_key(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self.main_window,
            "Wczytaj Klucz Publiczny",
            "",
            "PEM Files (*.pem);;All Files (*)",
            options=options
        )
        if file_name:
            try:
                with open(file_name, 'rb') as f:
                    self.public_key = RSA.import_key(f.read())
                # Aktualizacja pola wyświetlania klucza publicznego
                public_pem = self.public_key.export_key().decode('utf-8')
                self.main_window.rsa_publicKey.setText(public_pem)
                print("Klucz publiczny wczytany pomyślnie.")
            except Exception as e:
                QMessageBox.critical(
                    self.main_window,
                    "Błąd",
                    f"Nie udało się wczytać klucza publicznego: {str(e)}"
                )
                print("Błąd podczas wczytywania klucza publicznego.")

    def load_private_key(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self.main_window,
            "Wczytaj Klucz Prywatny",
            "",
            "PEM Files (*.pem);;All Files (*)",
            options=options
        )
        if file_name:
            try:
                with open(file_name, 'rb') as f:
                    self.key = RSA.import_key(f.read())
                    self.public_key = self.key.publickey()
                # Aktualizacja pól wyświetlania kluczy
                public_pem = self.public_key.export_key().decode('utf-8')
                private_pem = self.key.export_key().decode('utf-8')
                self.main_window.rsa_publicKey.setText(public_pem)
                self.main_window.rsa_privetKey.setText(private_pem)
                print("Klucz prywatny wczytany pomyślnie.")
            except Exception as e:
                QMessageBox.critical(
                    self.main_window,
                    "Błąd",
                    f"Nie udało się wczytać klucza prywatnego: {str(e)}"
                )
                print("Błąd podczas wczytywania klucza prywatnego.")











    def generate_keys(self):
        # Pobierz wybrany rozmiar klucza
        key_size_text = self.main_window.rsa_keySize.currentText()
        key_size = int(key_size_text)

        try:
            # Generowanie klucza RSA
            self.key = RSA.generate(key_size)
            self.public_key = self.key.publickey()

            # Eksport kluczy w formacie PEM
            public_pem = self.public_key.export_key().decode('utf-8')
            private_pem = self.key.export_key().decode('utf-8')

            # Wyświetlanie kluczy w interfejsie
            self.main_window.rsa_publicKey.setText(public_pem)
            self.main_window.rsa_privetKey.setText(private_pem)
        except Exception as e:
            QMessageBox.critical(
                self.main_window,
                "Błąd",
                f"Nie udało się wygenerować kluczy RSA: {str(e)}"
            )



















    def encrypt_text(self):
        if not self.public_key:
            QMessageBox.warning(
                self.main_window,
                "Brak klucza publicznego",
                "Najpierw wygeneruj klucz publiczny."
            )
            return

        plaintext = self.main_window.rsa_plainText.toPlainText()
        if not plaintext:
            QMessageBox.warning(
                self.main_window,
                "Brak tekstu jawnego",
                "Wprowadź tekst jawny do zaszyfrowania."
            )
            return

        try:
            plaintext_bytes = plaintext.encode('utf-8')                         # Konwersja tekstu jawnego na bajty
            cipher = PKCS1_OAEP.new(self.public_key)                            # Inicjalizacja szyfratora PKCS1_OAEP
            ciphertext_bytes = cipher.encrypt(plaintext_bytes)                  # Szyfrowanie tekstu
            ciphertext_hex = binascii.hexlify(ciphertext_bytes).decode('utf-8') # Konwersja ciphertext do formatu heksadecymalnego dla czytelności
            self.main_window.rsa_cipherText.setText(ciphertext_hex)             # Wyświetlanie ciphertext w interfejsie
        except Exception as e:
            QMessageBox.critical(
                self.main_window,
                "Błąd",
                f"Nie udało się zaszyfrować tekstu: {str(e)}"
            )




    def decrypt_text(self):
        if not self.key:
            QMessageBox.warning(
                self.main_window,
                "Brak klucza prywatnego",
                "Najpierw wygeneruj klucz prywatny."
            )
            return

        ciphertext_hex = self.main_window.rsa_cipherText.toPlainText()
        if not ciphertext_hex:
            QMessageBox.warning(
                self.main_window,
                "Brak ciphertext",
                "Wprowadź tekst zaszyfrowany do odszyfrowania."
            )
            return

        try:
            ciphertext_bytes = binascii.unhexlify(ciphertext_hex)   # Konwersja ciphertext z formatu heksadecymalnego na bajty
            cipher = PKCS1_OAEP.new(self.key)                       # Inicjalizacja deszyfratora PKCS1_OAEP
            plaintext_bytes = cipher.decrypt(ciphertext_bytes)      # Deszyfrowanie ciphertext
            plaintext = plaintext_bytes.decode('utf-8')             # Konwersja bajtów na tekst
            self.main_window.rsa_plainText.setText(plaintext)       # Wyświetlanie odszyfrowanego tekstu w interfejsie
        except (ValueError, binascii.Error) as e:
            QMessageBox.critical(
                self.main_window,
                "Błąd",
                f"Nieprawidłowy ciphertext lub klucz: {str(e)}"
            )
        except Exception as e:
            QMessageBox.critical(
                self.main_window,
                "Błąd",
                f"Nie udało się odszyfrować tekstu: {str(e)}"
            )














































    def encrypt_file(self):
        if not self.public_key:
            QMessageBox.warning(self.main_window,"Brak klucza publicznego","Najpierw wygeneruj klucz publiczny.")
            return

        base64_text = self.loaded_text

        if not base64_text:
            QMessageBox.warning(self.main_window,"Brak tekstu jawnego","Wprowadź tekst jawny do zaszyfrowania.")
            return

        try:
            decoded_bytes = binascii.a2b_base64(base64_text)                        # Dekodowanie Base64 do bajtów
            cipher = PKCS1_OAEP.new(self.public_key)                                # Inicjalizacja szyfratora PKCS1_OAEP

            encrypted_blocks = []
            for byte in decoded_bytes:
                plaintext = bytes([byte])
                encrypted_bytes = cipher.encrypt(plaintext)
                encrypted_hex = binascii.hexlify(encrypted_bytes).decode('utf-8')   # Konwersja do heksadecymalnego formatu
                encrypted_blocks.append(encrypted_hex)

            encrypted_content = ' '.join(encrypted_blocks)                          # Łączenie zaszyfrowanych bloków z separatorem (np. spacja)
            self.main_window.save_content_to_file(2, encrypted_content)             # Zapisanie zaszyfrowanej zawartości do pliku
            print("Szyfrowanie pliku zakończone sukcesem.")                         # Informacja o sukcesie
        except Exception as e:
            QMessageBox.critical(self.main_window,"Błąd",f"Nie udało się zaszyfrować pliku: {str(e)}")
            print(f"Nie udało się zaszyfrować pliku: {e}")




    def decrypt_file(self):
        if not self.key:
            QMessageBox.warning(self.main_window,"Brak klucza prywatnego","Najpierw wygeneruj klucz prywatny.")
            return

        ciphertext_hex = self.loaded_cipher_text
        if not ciphertext_hex:
            QMessageBox.warning(self.main_window,"Brak ciphertext","Wprowadź tekst zaszyfrowany do odszyfrowania.")
            return

        try:
            encrypted_hex_blocks = ciphertext_hex.split(' ')                                # Podział zaszyfrowanej zawartości na bloków heksadecymalnych
            cipher = PKCS1_OAEP.new(self.key)                                               # Inicjalizacja deszyfratora PKCS1_OAEP

            decrypted_bytes = bytearray()
            for encrypted_hex in encrypted_hex_blocks:
                encrypted_bytes = binascii.unhexlify(encrypted_hex)
                decrypted_byte = cipher.decrypt(encrypted_bytes)
                decrypted_bytes.extend(decrypted_byte)

            decrypted_base64 = binascii.b2a_base64(decrypted_bytes).decode('utf-8').strip() # Konwersja odszyfrowanych bajtów do Base64
            self.main_window.save_to_file_using_base64(decrypted_base64)                    # Zapisanie odszyfrowanej zawartości do pliku
            print("Deszyfrowanie pliku zakończone sukcesem.")                               # Informacja o sukcesie
        except Exception as e:
            QMessageBox.critical(self.main_window,"Błąd",f"Nie udało się odszyfrować pliku: {str(e)}")
            print(f"Nie udało się odszyfrować pliku: {e}")
