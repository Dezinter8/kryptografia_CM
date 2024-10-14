class Vigener:
    def __init__(self):
        # self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   # Definicja alfabetu
        self.alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"   # Definicja polskiego alfabetu
        self.alphabet_lower = self.alphabet.lower()
        self.alphabet_length = len(self.alphabet)

    def vigenere_cipher(self, tekst, klucz):
        if not tekst or not klucz:
            return "Proszę wprowadzić zarówno tekst, jak i klucz."
        return self.encrypt(tekst, klucz)

    def decode_vigenere(self, zaszyfrowany_tekst, klucz):
        if not zaszyfrowany_tekst or not klucz:
            return "Proszę wprowadzić zarówno zaszyfrowany tekst, jak i klucz."
        return self.decrypt(zaszyfrowany_tekst, klucz)



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

        return zaszyfrowany_tekst


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

        return odszyfrowany_tekst
