from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PySide6.QtWidgets import QMessageBox

class Des:
    def __init__(self, main_window):
        self.main_window = main_window

        self.loaded_text = ''
        self.loaded_cipher_text = ''

        # Obsługa przycisków zmieniających tryb pracy des
        self.main_window.des_normalMode_button.clicked.connect(lambda: self.switch_des_page(0))
        self.main_window.des_allFileMode_button.clicked.connect(lambda: self.switch_des_page(1))
        self.main_window.des_networkMode_button.clicked.connect(lambda: self.switch_des_page(2))

        # Obsługa przycisków wywołujących szyfrowanie i deszyfrowanie
        self.main_window.Des_button.clicked.connect(lambda: self.encrypt_des(1, self.main_window.Des_input_text))
        self.main_window.Des_decode_button.clicked.connect(lambda: self.decrypt_des(1, self.main_window.Des_decode_input_text))

        # Obsługa przycisków wywołujących szyfrowanie i deszyfrowanie dla plików
        self.main_window.Des_button_2.clicked.connect(lambda: self.encrypt_des(2, self.loaded_text))
        self.main_window.Des_decode_button_2.clicked.connect(lambda: self.decrypt_des(2, self.loaded_cipher_text))




    def switch_des_page(self, index):
        self.main_window.stackedWidget_des.setCurrentIndex(index)

    # Dodawanie zakodowanych plikow base64 do zmiennej
    def text_update(self, text):
        self.loaded_text = text
        print("tekst zostal zczytany")

    # Dodawanie zawartosci plikow do zmiennej
    def cipher_text_update(self, text):
        self.loaded_cipher_text = text
        print("zaszyfrowany tekst zostal zczytany")

    def encrypt_des(self, mode, text):
        # Sprawdzenie, który z radiobuttonów jest zaznaczony
        if self.main_window.des_cbc_radioButton.isChecked():
            des_mode = DES.MODE_CBC
        elif self.main_window.des_cfb_radioButton.isChecked():
            des_mode = DES.MODE_CFB
        elif self.main_window.des_ecb_radioButton.isChecked():
            des_mode = DES.MODE_ECB
        elif self.main_window.des_ofb_radioButton.isChecked():
            des_mode = DES.MODE_OFB
        else:
            QMessageBox.warning(self.main_window, "Błąd", "Wybierz tryb szyfrowania DES.")
            return
        
        if mode == 1:
            plaintext = text.text()
            key = self.main_window.Des_input_key.text()
        elif mode == 2:
            plaintext = text
            key = self.main_window.Des_input_key_2.text()
        
        
        if len(key) != 8:                                           # Sprawdzamy poprawność klucza
            QMessageBox.warning(self.main_window, "Błąd", "Klucz musi mieć dokładnie 8 znaków (64 bity).")
            return

        try:
            key_bytes = key.encode('utf-8')                         # Przekształcenie klucza do formatu bajtów
            plaintext_bytes = plaintext.encode('utf-8')             # Przekształcenie tekstu jawnego do formatu bajtów
            padded_data = pad(plaintext_bytes, DES.block_size)      # Padding danych wejściowych - DES pracuje na blokach o długości 8 bajtów
            
            if des_mode == DES.MODE_ECB:                            # Tworzenie obiektu szyfrującego z uwzględnieniem trybu
                cipher = DES.new(key_bytes, des_mode)
            else:                                                   # Generowanie losowego wektora inicjalizującego IV dla trybów CBC, OFB, CFB
                iv = get_random_bytes(8)
                cipher = DES.new(key_bytes, des_mode, iv=iv)
            
            ciphertext = cipher.encrypt(padded_data)                # Szyfrowanie danych
            encrypted_hex = ciphertext.hex()                        # Przekształcenie zaszyfrowanego tekstu na reprezentację heksadecymalną
            
            if des_mode != DES.MODE_ECB:                            # Dla trybów z IV, dołączamy IV do początku zaszyfrowanego tekstu, aby można było go użyć podczas deszyfrowania
                iv_hex = iv.hex()
                encrypted_hex = iv_hex + encrypted_hex

            if mode == 1:
                self.main_window.Des_output.setPlainText(encrypted_hex)     # Wyświetlenie wyniku w polu tekstowym
            elif mode == 2:
                self.main_window.save_content_into_file(2, encrypted_hex)   # Zapisanie wynikow do pliku
        
        except Exception as e:
            QMessageBox.critical(self.main_window, "Błąd", f"Wystąpił błąd podczas szyfrowania: {str(e)}")


    def decrypt_des(self, mode, text):
        # Sprawdzenie, który z radiobuttonów jest zaznaczony
        if self.main_window.des_cbc_radioButton.isChecked():
            des_mode = DES.MODE_CBC
        elif self.main_window.des_cfb_radioButton.isChecked():
            des_mode = DES.MODE_CFB
        elif self.main_window.des_ecb_radioButton.isChecked():
            des_mode = DES.MODE_ECB
        elif self.main_window.des_ofb_radioButton.isChecked():
            des_mode = DES.MODE_OFB
        else:
            QMessageBox.warning(self.main_window, "Błąd", "Wybierz tryb szyfrowania DES.")
            return

        if mode == 1:
            encrypted_hex = text.text()
            key = self.main_window.Des_decode_input_key.text()
        elif mode == 2:
            encrypted_hex = text
            key = self.main_window.Des_decode_input_key_2.text()
        
        if len(key) != 8:                                                   # Sprawdzamy poprawność klucza
            QMessageBox.warning(self.main_window, "Błąd", "Klucz musi mieć dokładnie 8 znaków (64 bity).")
            return

        try:
            key_bytes = key.encode('utf-8')                                 # Przekształcenie klucza do formatu bajtów
            ciphertext = bytes.fromhex(encrypted_hex)                       # Przekształcenie zaszyfrowanego tekstu z heksadecymalnego na bajty
            
            if des_mode != DES.MODE_ECB:                                    # Odczytanie IV, jeśli jest wymagane dla trybów CBC, OFB, CFB
                iv = ciphertext[:8]                                         # Pierwsze 8 bajtów to IV
                ciphertext = ciphertext[8:]                                 # Reszta to zaszyfrowany tekst
                cipher = DES.new(key_bytes, des_mode, iv=iv)
            else:
                cipher = DES.new(key_bytes, des_mode)
            
            decrypted_padded_data = cipher.decrypt(ciphertext)              # Odszyfrowanie danych
            decrypted_data = unpad(decrypted_padded_data, DES.block_size)   # Usunięcie paddingu z odszyfrowanych danych
            
            if mode == 1:
                self.main_window.Des_decode_output.setPlainText(decrypted_data.decode('utf-8'))     # Przekształcenie bajtów na tekst i wyświetlenie w polu tekstowym
            elif mode == 2:
                self.main_window.save_to_file_using_base64(decrypted_data)                          # Zapisanie wynikow do pliku
        
        except ValueError as e:
            QMessageBox.critical(self.main_window, "Błąd", f"Błąd odszyfrowania: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Błąd", f"Wystąpił błąd podczas odszyfrowania: {str(e)}")

