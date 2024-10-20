from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PySide6.QtWidgets import QMessageBox

class Des:
    def __init__(self, main_window):
        self.main_window = main_window

        # Obsługa przycisków zmieniających tryb pracy des
        self.main_window.des_ecb_button.clicked.connect(lambda: self.switch_des_page(0))
        self.main_window.des_cbc_button.clicked.connect(lambda: self.switch_des_page(1))
        self.main_window.des_ofb_button.clicked.connect(lambda: self.switch_des_page(2))
        self.main_window.des_cfb_button.clicked.connect(lambda: self.switch_des_page(3))

        # Obsługa przycisków wywołujących szyfrowanie
        self.main_window.Des_ecb_button.clicked.connect(lambda: self.encrypt_des(DES.MODE_ECB, self.main_window.Des_ecb_input_text, self.main_window.Des_ecb_input_key, self.main_window.Des_ecb_output))
        self.main_window.Des_cbc_button.clicked.connect(lambda: self.encrypt_des(DES.MODE_CBC, self.main_window.Des_cbc_input_text, self.main_window.Des_cbc_input_key, self.main_window.Des_cbc_output))
        self.main_window.Des_ofb_button.clicked.connect(lambda: self.encrypt_des(DES.MODE_OFB, self.main_window.Des_ofb_input_text, self.main_window.Des_ofb_input_key, self.main_window.Des_ofb_output))
        self.main_window.Des_cfb_button.clicked.connect(lambda: self.encrypt_des(DES.MODE_CFB, self.main_window.Des_cfb_input_text, self.main_window.Des_cfb_input_key, self.main_window.Des_cfb_output))

        # Obsługa przycisków wywołujących deszyfrowanie
        self.main_window.Des_ecb_decode_button.clicked.connect(lambda: self.decrypt_des(DES.MODE_ECB, self.main_window.Des_ecb_decode_input_text, self.main_window.Des_ecb_decode_input_key, self.main_window.Des_ecb_decode_output))
        self.main_window.Des_cbc_decode_button.clicked.connect(lambda: self.decrypt_des(DES.MODE_CBC, self.main_window.Des_cbc_decode_input_text, self.main_window.Des_cbc_decode_input_key, self.main_window.Des_cbc_decode_output))
        self.main_window.Des_ofb_decode_button.clicked.connect(lambda: self.decrypt_des(DES.MODE_OFB, self.main_window.Des_ofb_decode_input_text, self.main_window.Des_ofb_decode_input_key, self.main_window.Des_ofb_decode_output))
        self.main_window.Des_cfb_decode_button.clicked.connect(lambda: self.decrypt_des(DES.MODE_CFB, self.main_window.Des_cfb_decode_input_text, self.main_window.Des_cfb_decode_input_key, self.main_window.Des_cfb_decode_output))


    def switch_des_page(self, index):
        self.main_window.stackedWidget_des.setCurrentIndex(index)


    def encrypt_des(self, mode, text, key, output):
        plaintext = text.text()
        key = key.text()
        if len(key) != 8:                                       # Sprawdzamy poprawność klucza
            QMessageBox.warning(self.main_window, "Błąd", "Klucz musi mieć dokładnie 8 znaków (64 bity).")
            return

        try:
            key_bytes = key.encode('utf-8')                     # Przekształcenie klucza do formatu bajtów
            plaintext_bytes = plaintext.encode('utf-8')         # Przekształcenie tekstu jawnego do formatu bajtów
            padded_data = pad(plaintext_bytes, DES.block_size)  # Padding danych wejściowych - DES pracuje na blokach o długości 8 bajtów
            
            if mode == DES.MODE_ECB:                            # Tworzenie obiektu szyfrującego z uwzględnieniem trybu
                cipher = DES.new(key_bytes, mode)
            else:                                               # Generowanie losowego wektora inicjalizującego IV dla trybów CBC, OFB, CFB
                iv = get_random_bytes(8)
                cipher = DES.new(key_bytes, mode, iv=iv)
            
            ciphertext = cipher.encrypt(padded_data)            # Szyfrowanie danych
            encrypted_hex = ciphertext.hex()                    # Przekształcenie zaszyfrowanego tekstu na reprezentację heksadecymalną
            
            if mode != DES.MODE_ECB:                            # Dla trybów z IV, dołączamy IV do początku zaszyfrowanego tekstu, aby można było go użyć podczas deszyfrowania
                iv_hex = iv.hex()
                encrypted_hex = iv_hex + encrypted_hex

            output.setPlainText(encrypted_hex)                  # Wyświetlenie wyniku w polu tekstowym
        
        except Exception as e:
            QMessageBox.critical(self.main_window, "Błąd", f"Wystąpił błąd podczas szyfrowania: {str(e)}")


    def decrypt_des(self, mode, text, key, output):
        encrypted_hex = text.text()
        key = key.text()
        if len(key) != 8:                                                   # Sprawdzamy poprawność klucza
            QMessageBox.warning(self.main_window, "Błąd", "Klucz musi mieć dokładnie 8 znaków (64 bity).")
            return

        try:
            key_bytes = key.encode('utf-8')                                 # Przekształcenie klucza do formatu bajtów
            ciphertext = bytes.fromhex(encrypted_hex)                       # Przekształcenie zaszyfrowanego tekstu z heksadecymalnego na bajty
            
            if mode != DES.MODE_ECB:                                        # Odczytanie IV, jeśli jest wymagane dla trybów CBC, OFB, CFB
                iv = ciphertext[:8]                                         # Pierwsze 8 bajtów to IV
                ciphertext = ciphertext[8:]                                 # Reszta to zaszyfrowany tekst
                cipher = DES.new(key_bytes, mode, iv=iv)
            else:
                cipher = DES.new(key_bytes, mode)
            
            decrypted_padded_data = cipher.decrypt(ciphertext)              # Odszyfrowanie danych
            decrypted_data = unpad(decrypted_padded_data, DES.block_size)   # Usunięcie paddingu z odszyfrowanych danych
            output.setPlainText(decrypted_data.decode('utf-8'))             # Przekształcenie bajtów na tekst i wyświetlenie w polu tekstowym
        
        except ValueError as e:
            QMessageBox.critical(self.main_window, "Błąd", f"Błąd odszyfrowania: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self.main_window, "Błąd", f"Wystąpił błąd podczas odszyfrowania: {str(e)}")
