from PySide6.QtWidgets import QMessageBox

class Vigener:
    def __init__(self, main_window):
        self.main_window = main_window

        # self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   # Definicja alfabetu
        self.alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"   # Definicja polskiego alfabetu
        self.alphabet_lower = self.alphabet.lower()
        self.alphabet_length = len(self.alphabet)


        self.main_window.Vigener_button.clicked.connect(self.vigenere_cipher)
        self.main_window.Vigener_decode_button.clicked.connect(self.decode_vigenere)



    def vigenere_cipher(self):
        plaintext = self.main_window.Vigener_input_text.text()
        key = self.main_window.Vigener_input_key.text()

        if not plaintext or not key:
            QMessageBox.warning(self.main_window, "Błąd", "Proszę wprowadzić zarówno tekst, jak i klucz.")
            return
        # Sprawdzenie, czy klucz zawiera tylko dozwolone znaki
        if any(znak not in self.alphabet and znak not in self.alphabet_lower for znak in key):
            QMessageBox.warning(self.main_window, "Błąd", "Klucz zawiera niedozwolone znaki. Proszę użyć tylko liter polskiego alfabetu.")
            return

        self.encrypt(plaintext, key)

    def decode_vigenere(self):
        ciphertext = self.main_window.Vigener_decode_input_text.text()
        key = self.main_window.Vigener_decode_input_key.text()

        if not ciphertext or not key:
            QMessageBox.warning(self.main_window, "Błąd", "Proszę wprowadzić zarówno zaszyfrowany tekst, jak i klucz.")
            return
        # Sprawdzenie, czy klucz zawiera tylko dozwolone znaki
        if any(znak not in self.alphabet and znak not in self.alphabet_lower for znak in key):
            QMessageBox.warning(self.main_window, "Błąd", "Klucz zawiera niedozwolone znaki. Proszę użyć tylko liter polskiego alfabetu.")
            return
        
        self.decrypt(ciphertext, key)



    def encrypt(self, tekst, klucz):
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

        self.main_window.Vigener_output.setPlainText(zaszyfrowany_tekst)
    


    def decrypt(self, zaszyfrowany_tekst, klucz):
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

        self.main_window.Vigener_decode_output.setPlainText(odszyfrowany_tekst)
