from PySide6.QtWidgets import QMessageBox

class Vigener:
    def __init__(self, main_window):
        self.main_window = main_window

        # self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   # Definicja alfabetu
        self.alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"   # Definicja polskiego alfabetu
        self.alphabet_lower = self.alphabet.lower()
        self.alphabet_length = len(self.alphabet)

        self.loaded_text = ''
        self.loaded_cipher_text = ''

        self.main_window.vigener_textMode_button.clicked.connect(lambda: self.switch_vigener_pages(0))
        self.main_window.vigener_allfilesmode_button.clicked.connect(lambda: self.switch_vigener_pages(1))
        self.main_window.vigener_networkmode_button.clicked.connect(lambda: self.switch_vigener_pages(2))


        self.main_window.Vigener_button.clicked.connect(lambda: self.vigenere_cipher(1))
        self.main_window.Vigener_decode_button.clicked.connect(lambda: self.decode_vigenere(1))

        self.main_window.Vigener_button_2.clicked.connect(lambda: self.vigenere_cipher(2))
        self.main_window.Vigener_decode_button_2.clicked.connect(lambda: self.decode_vigenere(2))
        


    def switch_vigener_pages(self, index):
        self.main_window.Vigener_stackedWidget.setCurrentIndex(index)


    def text_update(self, text):
        self.loaded_text = text
        print("tekst zostal zczytany")

    def cipher_text_update(self, text):
        self.loaded_cipher_text = text
        print("zaszyfrowany tekst zostal zczytany")


    def vigenere_cipher(self, mode):
        if mode == 1: # Działanie szyfrowania dla trybu normalnego
            plaintext = self.main_window.Vigener_input_text.text()
            key = self.main_window.Vigener_input_key.text()

            if not plaintext or not key:
                QMessageBox.warning(self.main_window, "Błąd", "Proszę wprowadzić zarówno tekst, jak i klucz.")
                return
            # Sprawdzenie, czy klucz zawiera tylko dozwolone znaki
            if any(znak not in self.alphabet and znak not in self.alphabet_lower for znak in key):
                QMessageBox.warning(self.main_window, "Błąd", "Klucz zawiera niedozwolone znaki. Proszę użyć tylko liter polskiego alfabetu.")
                return
            
            self.encrypt(1, plaintext, key)

        elif mode == 2: # Działanie szyfrowania dla trybu base64
            plaintext = self.loaded_text
            key = self.main_window.Vigener_input_key_2.text()

            if not plaintext or not key:
                QMessageBox.warning(self.main_window, "Błąd", "Proszę wprowadzić zarówno tekst, jak i klucz.")
                return
            # Sprawdzenie, czy klucz zawiera tylko dozwolone znaki
            if any(znak not in self.alphabet and znak not in self.alphabet_lower for znak in key):
                QMessageBox.warning(self.main_window, "Błąd", "Klucz zawiera niedozwolone znaki. Proszę użyć tylko liter polskiego alfabetu.")
                return
            
            self.encrypt(2, plaintext, key)


            
        

    def decode_vigenere(self, mode):
        if mode == 1: # Działanie deszyfrowania dla trybu normalnego
            ciphertext = self.main_window.Vigener_decode_input_text.text()
            key = self.main_window.Vigener_decode_input_key.text()

            if not ciphertext or not key:
                QMessageBox.warning(self.main_window, "Błąd", "Proszę wprowadzić zarówno zaszyfrowany tekst, jak i klucz.")
                return
            # Sprawdzenie, czy klucz zawiera tylko dozwolone znaki
            if any(znak not in self.alphabet and znak not in self.alphabet_lower for znak in key):
                QMessageBox.warning(self.main_window, "Błąd", "Klucz zawiera niedozwolone znaki. Proszę użyć tylko liter polskiego alfabetu.")
                return
            
            self.decrypt(1, ciphertext, key)
        
        elif mode == 2: # Działanie deszyfrowania dla trybu base64
            ciphertext = self.loaded_cipher_text
            key = self.main_window.Vigener_decode_input_key_2.text()

            if not ciphertext or not key:
                QMessageBox.warning(self.main_window, "Błąd", "Proszę wprowadzić zarówno zaszyfrowany tekst, jak i klucz.")
                return
            # Sprawdzenie, czy klucz zawiera tylko dozwolone znaki
            if any(znak not in self.alphabet and znak not in self.alphabet_lower for znak in key):
                QMessageBox.warning(self.main_window, "Błąd", "Klucz zawiera niedozwolone znaki. Proszę użyć tylko liter polskiego alfabetu.")
                return
            
            self.decrypt(2, ciphertext, key)


    def encrypt(self, mode, tekst, klucz):
        zaszyfrowany_tekst = ""
        klucz_index = 0
        klucz = klucz.lower()

        for znak in tekst:
            if znak.lower() in self.alphabet_lower:
                # Określenie alfabetu
                is_upper = znak.isupper()
                current_alphabet = self.alphabet if is_upper else self.alphabet_lower

                # Wyliczenie indeksów
                text_index = current_alphabet.index(znak) + 1
                key_index = self.alphabet_lower.index(klucz[klucz_index % len(klucz)].lower())

                # Szyfrowanie
                zaszyfrowany_znak = current_alphabet[(text_index + key_index) % self.alphabet_length]
                zaszyfrowany_tekst += zaszyfrowany_znak
                klucz_index += 1
            else:
                zaszyfrowany_tekst += znak

        if mode == 1:
            self.main_window.Vigener_output.setPlainText(zaszyfrowany_tekst)
        elif mode == 2:
            self.main_window.save_content_into_file(2, zaszyfrowany_tekst)


    def decrypt(self, mode, zaszyfrowany_tekst, klucz):
        odszyfrowany_tekst = ""
        klucz_index = 0
        klucz = klucz.lower()

        for znak in zaszyfrowany_tekst:
            if znak.lower() in self.alphabet_lower:
                # Określenie alfabetu
                is_upper = znak.isupper()
                current_alphabet = self.alphabet if is_upper else self.alphabet_lower

                # Wyliczenie indeksów
                text_index = current_alphabet.index(znak)
                key_index = self.alphabet_lower.index(klucz[klucz_index % len(klucz)].lower()) + 1

                # Deszyfrowanie
                odszyfrowany_znak = current_alphabet[(text_index - key_index) % self.alphabet_length]
                odszyfrowany_tekst += odszyfrowany_znak
                klucz_index += 1
            else:
                odszyfrowany_tekst += znak

        if mode == 1:
            self.main_window.Vigener_decode_output.setPlainText(odszyfrowany_tekst)
        elif mode == 2:
            self.main_window.save_to_file_using_base64(odszyfrowany_tekst)
