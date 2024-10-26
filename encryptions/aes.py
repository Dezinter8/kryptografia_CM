from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PySide6.QtWidgets import QMessageBox

class Aes:
    def __init__(self, main_window):
        self.main_window = main_window

        self.loaded_text = ''
        self.loaded_cipher_text = ''

        # Obsługa przycisków zmieniających tryb pracy aes
        self.main_window.aes_normalMode_button.clicked.connect(lambda: self.switch_aes_page(0))
        self.main_window.aes_allFileMode_button.clicked.connect(lambda: self.switch_aes_page(1))

        # Obsługa przycisków wywołujących szyfrowanie i deszyfrowanie
        self.main_window.Aes_button.clicked.connect(lambda: self.encrypt_aes(1, self.main_window.Aes_input_text))
        self.main_window.Aes_decode_button.clicked.connect(lambda: self.decrypt_aes(1, self.main_window.Aes_decode_input_text))

        # Obsługa przycisków wywołujących szyfrowanie i deszyfrowanie dla plików
        self.main_window.Aes_button_2.clicked.connect(lambda: self.encrypt_aes(2, self.loaded_text))
        self.main_window.Aes_decode_button_2.clicked.connect(lambda: self.decrypt_aes(2, self.loaded_cipher_text))




    def switch_aes_page(self, index):
        self.main_window.stackedWidget_aes.setCurrentIndex(index)

    # Dodawanie zakodowanych plikow base64 do zmiennej
    def text_update(self, text):
        self.loaded_text = text
        print("tekst zostal zczytany")

    # Dodawanie zawartosci plikow do zmiennej
    def cipher_text_update(self, text):
        self.loaded_cipher_text = text
        print("zaszyfrowany tekst zostal zczytany")

    def encrypt_aes(self, mode, text):
        # Sprawdzenie, który z radiobuttonów jest zaznaczony
        if self.main_window.aes_cbc_radioButton.isChecked():
            aes_mode = AES.MODE_CBC
        elif self.main_window.aes_cfb_radioButton.isChecked():
            aes_mode = AES.MODE_CFB
        elif self.main_window.aes_ecb_radioButton.isChecked():
            aes_mode = AES.MODE_ECB
        elif self.main_window.aes_ofb_radioButton.isChecked():
            aes_mode = AES.MODE_OFB
        elif self.main_window.aes_gcm_radioButton.isChecked():
            aes_mode = AES.MODE_GCM
        else:
            QMessageBox.warning(self.main_window, "Błąd", "Wybierz tryb szyfrowania AES.")
            return
        
        if mode == 1:
            plaintext = text.text()
            key = self.main_window.Aes_input_key.text()
        elif mode == 2:
            plaintext = text
            key = self.main_window.Aes_input_key_2.text()
        
        
        if len(key) not in (16, 24, 32):                            # Sprawdzamy poprawność klucza
            QMessageBox.warning(self.main_window, "Błąd", "Klucz musi mieć dokładnie 16, 24 lub 32 znaki.")
            return

        try:
            key_bytes = key.encode('utf-8')
            plaintext_bytes = plaintext.encode('utf-8')
            padded_data = pad(plaintext_bytes, AES.block_size)

            if aes_mode in (AES.MODE_ECB, AES.MODE_GCM):
                cipher = AES.new(key_bytes, aes_mode)
            else:
                iv = get_random_bytes(16)
                cipher = AES.new(key_bytes, aes_mode, iv=iv)

            ciphertext = cipher.encrypt(padded_data)
            encrypted_hex = ciphertext.hex()

            if aes_mode not in (AES.MODE_ECB, AES.MODE_GCM):
                iv_hex = iv.hex()
                encrypted_hex = iv_hex + encrypted_hex
            elif aes_mode == AES.MODE_GCM:
                encrypted_hex = cipher.nonce.hex() + encrypted_hex + cipher.digest().hex()


            if mode == 1:
                self.main_window.Aes_output.setPlainText(encrypted_hex)     # Wyświetlenie wyniku w polu tekstowym
            elif mode == 2:
                self.main_window.save_content_into_file(2, encrypted_hex)   # Zapisanie wynikow do pliku
        
        except Exception as e:
            QMessageBox.critical(self.main_window, "Błąd", f"Wystąpił błąd podczas szyfrowania: {str(e)}")


    def decrypt_aes(self, mode, text):
        # Sprawdzenie, który z radiobuttonów jest zaznaczony
        if self.main_window.aes_cbc_radioButton.isChecked():
            aes_mode = AES.MODE_CBC
        elif self.main_window.aes_cfb_radioButton.isChecked():
            aes_mode = AES.MODE_CFB
        elif self.main_window.aes_ecb_radioButton.isChecked():
            aes_mode = AES.MODE_ECB
        elif self.main_window.aes_ofb_radioButton.isChecked():
            aes_mode = AES.MODE_OFB
        elif self.main_window.aes_gcm_radioButton.isChecked():
            aes_mode = AES.MODE_GCM
        else:
            QMessageBox.warning(self.main_window, "Błąd", "Wybierz tryb szyfrowania AES.")
            return
        
        if mode == 1:
            encrypted_hex = text.text()
            key = self.main_window.Aes_decode_input_key.text()
        elif mode == 2:
            encrypted_hex = text
            key = self.main_window.Aes_decode_input_key_2.text()
        
        if len(key) not in (16, 24, 32):                            # Sprawdzamy poprawność klucza
            QMessageBox.warning(self.main_window, "Błąd", "Klucz musi mieć dokładnie 16, 24 lub 32 znaki.")
            return

        try:
            key_bytes = key.encode('utf-8')
            ciphertext = bytes.fromhex(encrypted_hex)

            if aes_mode == AES.MODE_ECB:
                cipher = AES.new(key_bytes, aes_mode)
                decrypted_padded_data = cipher.decrypt(ciphertext)  # Dodane odszyfrowanie dla trybu ECB
            elif aes_mode == AES.MODE_GCM:
                nonce = ciphertext[:16]
                ciphertext = ciphertext[16:]
                cipher = AES.new(key_bytes, aes_mode, nonce=nonce)
                tag = ciphertext[-16:]
                ciphertext = ciphertext[:-16]
                decrypted_padded_data = cipher.decrypt_and_verify(ciphertext, tag)
            else:
                iv = ciphertext[:16]
                ciphertext = ciphertext[16:]
                cipher = AES.new(key_bytes, aes_mode, iv=iv)
                decrypted_padded_data = cipher.decrypt(ciphertext)

            decrypted_data = unpad(decrypted_padded_data, AES.block_size)


            if mode == 1:
                self.main_window.Aes_decode_output.setPlainText(decrypted_data.decode('utf-8'))     # Przekształcenie bajtów na tekst i wyświetlenie w polu tekstowym
            elif mode == 2:
                self.main_window.save_to_file_using_base64(decrypted_data)                          # Zapisanie wynikow do pliku
        
        except ValueError as e:
            QMessageBox.critical(self.main_window, "Błąd", f"Błąd odszyfrowania: {str(e)}")
            print(f"Błąd odszyfrowania: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Błąd", f"Wystąpił błąd podczas odszyfrowania: {str(e)}")
            print(f"Wystąpił błąd podczas odszyfrowania: {str(e)}")