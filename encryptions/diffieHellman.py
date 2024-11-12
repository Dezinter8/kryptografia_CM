import random
from PySide6.QtWidgets import QMessageBox

class DiffieHellman:
    def __init__(self, main_window):
        self.main_window = main_window
        
        # Podłącz sygnał przycisku do metody diffie_hellman
        self.main_window.calculate_diffieHellman_pushButton.clicked.connect(self.diffie_hellman)

    def is_prime(self, n):
        """Sprawdza, czy liczba jest pierwsza."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def prime_factors(self, n):
        """Zwraca unikalne czynniki pierwsze liczby n."""
        factors = set()
        # Sprawdź dzielniki 2
        while n % 2 == 0:
            factors.add(2)
            n = n // 2
        # Sprawdź inne liczby pierwsze
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n = n // i
            i += 2
        if n > 2:
            factors.add(n)
        return factors

    def find_primitive_root(self, p):
        """Znajduje pierwotny generator modulo p."""
        if not self.is_prime(p):
            return None
        phi = p - 1
        factors = self.prime_factors(phi)
        for g in range(2, p):
            flag = False
            for factor in factors:
                if pow(g, phi // factor, p) == 1:
                    flag = True
                    break
            if not flag:
                return g
        return None

    def diffie_hellman(self):
        try:
            # Pobierz wartości z pól tekstowych i konwertuj na int
            a = int(self.main_window.a_input_lineEdit.text())
            b = int(self.main_window.b_input_lineEdit.text())
            g = int(self.main_window.g_input_lineEdit.text())
            p = int(self.main_window.p_input_lineEdit.text())
        except ValueError:
            QMessageBox.warning(self.main_window, "Błąd", "Proszę wprowadzić poprawne liczby całkowite.")
            return

        # Sprawdź, czy p jest liczbą pierwszą
        if not self.is_prime(p):
            QMessageBox.warning(self.main_window, "Błąd", "Liczba p musi być liczbą pierwszą.")
            return

        # Opcjonalnie: Sprawdź, czy g jest pierwotnym generatorem modulo p
        primitive_root = self.find_primitive_root(p)
        if primitive_root is None:
            QMessageBox.warning(self.main_window, "Błąd", f"Nie znaleziono pierwotnego generatora dla p = {p}.")
            return
        if g != primitive_root:
            reply = QMessageBox.question(
                self.main_window,
                "Ostrzeżenie",
                f"Wartość g = {g} nie jest pierwotnym generatorem dla p = {p}. Czy chcesz kontynuować?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.No:
                return

        # Oblicz klucze publiczne
        A = pow(g, a, p)
        B = pow(g, b, p)

        # Oblicz wspólny tajny klucz
        s_alice = pow(B, a, p)
        s_bob = pow(A, b, p)

        if s_alice != s_bob:
            QMessageBox.critical(self.main_window, "Błąd", "Wspólne klucze tajne nie są zgodne!")
            return

        s = s_alice  # Wspólny tajny klucz

        # Przygotuj wynik do wyświetlenia
        output = (
            f"Parametry publiczne:\n"
            f" p = {p}\n"
            f" g = {g}\n\n"
            f"Klucze prywatne:\n"
            f" Alicja: a = {a}\n"
            f" Bob: b = {b}\n\n"
            f"Klucze publiczne:\n"
            f" Alicja: A = g^a mod p = {A}\n"
            f" Bob: B = g^b mod p = {B}\n\n"
            f"Wspólny tajny klucz:\n"
            f" Alicja: s = B^a mod p = {s_alice}\n"
            f" Bob: s = A^b mod p = {s_bob}\n\n"
            f"Udane uzgodnienie klucza tajnego: {s}"
        )

        # Wyświetl wynik w polu textEdit
        self.main_window.diffieHellman_output.setPlainText(output)
