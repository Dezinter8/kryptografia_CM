class Transposition:
    def __init__(self):
        pass

    def transposition_cipher(self, plaintext, key):
        if not plaintext or not key:
            return "Proszę wprowadzić zarówno tekst, jak i klucz."
        return self.encrypt(plaintext, key)

    def decode_transposition(self, ciphertext, key):
        if not ciphertext or not key:
            return "Proszę wprowadzić zarówno zaszyfrowany tekst, jak i klucz."
        return self.decrypt(ciphertext, key)


    def encrypt(self, plaintext, key):
        key_length = len(key)
        columns = [''] * key_length                         # Obliczamy ilość kolumn
        for index, char in enumerate(plaintext):            # Rozdzielamy tekst na kolumny
            columns[index % key_length] += char
        sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])  # Sortujemy klucz i odczytujemy kolumny w odpowiedniej kolejności
        ciphertext = ''.join(columns[i] for i in sorted_key_indices)

        return ciphertext

    def decrypt(self, ciphertext, key):
        key_length = len(key)
        num_cols = len(ciphertext) // key_length
        num_shaded = len(ciphertext) % key_length

        col_lengths = [num_cols + 1 if i < num_shaded else num_cols for i in range(key_length)]     # Określenie długości kolumn, biorąc pod uwagę "zaciemnione" komórki (puste)
        columns = [''] * key_length                                                                 # Rozdzielamy zaszyfrowany tekst na kolumny w odpowiedniej kolejności
        sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])

        index = 0
        for i in sorted_key_indices:
            columns[i] = ciphertext[index:index + col_lengths[i]]
            index += col_lengths[i]

        plaintext = ''                              # Odtwarzamy oryginalny tekst wierszami
        for row in range(num_cols + 1):
            for col in range(key_length):
                if row < len(columns[col]):
                    plaintext += columns[col][row]

        return plaintext
