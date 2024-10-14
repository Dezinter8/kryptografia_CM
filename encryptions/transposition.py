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
        # plaintext = plaintext.replace(" ", "")          # Usunięcie spacji z tekstu jawnego, aby ułatwić szyfrowanie
        num_columns = len(key)                          # Ustalenie liczby kolumn na podstawie długości klucza
        num_rows = len(plaintext) // num_columns        # Obliczenie liczby wierszy na podstawie długości tekstu i liczby kolumn
        
        if len(plaintext) % num_columns != 0:
            num_rows += 1                               # Dodanie dodatkowego wiersza, jeśli są pozostałe znaki
        
        grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]  # Wypełnienie tabeli (lista list) znakami z tekstu jawnego
        index = 0
        for r in range(num_rows):
            for c in range(num_columns):
                if index < len(plaintext):
                    grid[r][c] = plaintext[index]
                    index += 1
                else:
                    grid[r][c] = 'X'                    # Uzupełnienie znakiem 'X', jeśli brakuje znaków
                                                        # Tworzenie permutacji kolumn na podstawie klucza
                                                        # Przypisanie każdej literze/znakowi klucza numer porządkowy po posortowaniu
        sorted_key = sorted(list(key))
        column_order = [sorted_key.index(k) for k in key]
                                                        # Odczytanie kolumny według określonej kolejności
        ciphertext = ""
        for col in column_order:
            for row in range(num_rows):
                ciphertext += grid[row][col]
        
        return ciphertext


    def decrypt(self, ciphertext, key):
        # ciphertext = ciphertext.replace(" ", "")        # Usunięcie spacji z tekstu zaszyfrowanego
        num_columns = len(key)                          # Ustalenie liczby kolumn na podstawie długości klucza
        
        num_rows = len(ciphertext) // num_columns       # Obliczenie liczby wierszy na podstawie długości zaszyfrowanego tekstu i liczby kolumn
        if len(ciphertext) % num_columns != 0:
            num_rows += 1                               # Dodanie dodatkowego wiersza, jeśli są pozostałe znaki
        
        grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]      # Utworzenie pustej tabeli do odczytywania kolumnami
        sorted_key = sorted(list(key))                  # Tworzenie permutacji kolumn na podstawie klucza
        column_order = [sorted_key.index(k) for k in key]
        full_columns = len(ciphertext) % num_columns    # Określanie liczby znaków w każdej kolumnie
        min_col_size = len(ciphertext) // num_columns
        col_sizes = [min_col_size + 1 if i < full_columns else min_col_size for i in range(num_columns)]
        
        index = 0                                       # Wypełnienie tabeli znakami z zaszyfrowanego tekstu zgodnie z kolejnością kolumn
        for col in column_order:
            for row in range(col_sizes[col]):
                grid[row][col] = ciphertext[index]
                index += 1
        
        plaintext = ""                                  # Odczytanie tabeli wierszami, aby odtworzyć tekst jawny
        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] != 'X':                   # Pomijamy znaki 'X' użyte jako dopełnienie
                    plaintext += grid[r][c]
        
        return plaintext
