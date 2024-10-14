import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Ui.MainWindow import Ui_MainWindow
from encryptions.vigener import Vigener
from encryptions.transposition import Transposition

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vigener = Vigener()
        self.transposition = Transposition()

        self.podstawieniowy_pushButton.clicked.connect(self.switch_to_vigener_page)
        self.transpozycyjny_pushButton.clicked.connect(self.switch_to_transposition_page)
        
        self.Vigener_button.clicked.connect(self.handle_vigenere)
        self.Vigener_decode_button.clicked.connect(self.handle_vigenere_decode)

        self.transposition_button.clicked.connect(self.handle_transposition)
        self.transposition_decode_button.clicked.connect(self.handle_transposition_decode)


    def switch_to_vigener_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_transposition_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def handle_vigenere(self):
        text = self.Vigener_input_text.text()
        key = self.Vigener_input_key.text()
        encrypted_text = self.vigener.vigenere_cipher(text, key)
        self.Vigener_output.setPlainText(encrypted_text)

    def handle_vigenere_decode(self):
        encrypted_text = self.Vigener_decode_input_text.text()
        key = self.Vigener_decode_input_key.text()
        decrypted_text = self.vigener.decode_vigenere(encrypted_text, key)
        self.Vigener_decode_output.setPlainText(decrypted_text)

    def handle_transposition(self):
        input_text = self.transposition_input_text.text()
        key = self.transposition_input_key.text()
        encrypted_text = self.transposition.transposition_cipher(input_text, key)
        self.transposition_output.setPlainText(encrypted_text)

    def handle_transposition_decode(self):
        encoded_text = self.transposition_decode_input_text.text()
        key = self.transposition_decode_input_key.text()
        decrypted_text = self.transposition.decode_transposition(encoded_text, key)
        self.transposition_decode_output.setPlainText(decrypted_text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())