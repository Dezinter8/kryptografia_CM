import sys
import base64
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog
from Ui.MainWindow import Ui_MainWindow
from encryptions import vigener, transposition, diffieHellman, des, aes, rsa, hmac
from encryptions.signatures import generateSignatureWithKeys, signDocument, verify
from network import Network
from dataStream import DataStream

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.vigener = vigener.Vigener(self)
        self.transposition = transposition.Transposition(self)
        self.des = des.Des(self)
        self.network = Network(self)
        self.aes = aes.Aes(self)
        self.diffieHellman = diffieHellman.DiffieHellman(self)
        self.rsa = rsa.Rsa(self)
        self.generateSignaruteWithKeys = generateSignatureWithKeys.generateSignatureWithKeys(self)
        self.signDocument = signDocument.signDocument(self)
        self.verifySignature = verify.verifySignature(self)
        self.hmac = hmac.Hmac(self)
        self.dataStream = DataStream(self)

        self.podstawieniowy_pushButton.clicked.connect(lambda: self.switch_main_page(0))
        self.transpozycyjny_pushButton.clicked.connect(lambda: self.switch_main_page(1))
        self.des_pushButton.clicked.connect(lambda: self.switch_main_page(2))
        self.aes_pushButton.clicked.connect(lambda: self.switch_main_page(3))
        self.siec_pushButton.clicked.connect(lambda: self.switch_main_page(4))
        self.rsa_pushButton.clicked.connect(lambda: self.switch_main_page(5))
        self.diffieHellman_pushButton.clicked.connect(lambda: self.switch_main_page(6))
        self.generateSignature_pushButton.clicked.connect(lambda: self.switch_main_page(7))
        self.signDocumen_pushButton.clicked.connect(lambda: self.switch_main_page(8))
        self.verifySignature_pushButton.clicked.connect(lambda: self.switch_main_page(9))
        self.hmac_pushButton.clicked.connect(lambda: self.switch_main_page(10))
        self.dataStream_pushButton.clicked.connect(lambda: self.switch_main_page(11))


        # Obsługa przycisków do ładowania zawartości plików
        self.Vigener_input_file.clicked.connect(lambda: self.load_file_content(1, self.Vigener_input_text, 0))
        self.Vigener_decode_input_file.clicked.connect(lambda: self.load_file_content(1, self.Vigener_decode_input_text, 0))
        self.transposition_input_file.clicked.connect(lambda: self.load_file_content(1, self.transposition_input_text, 0))
        self.transposition_decode_input_file.clicked.connect(lambda: self.load_file_content(1, self.transposition_decode_input_text, 0))
        self.Des_input_file.clicked.connect(lambda: self.load_file_content(1, self.Des_input_text, 0))
        self.Des_decode_input_file.clicked.connect(lambda: self.load_file_content(1, self.Des_decode_input_text, 0))
        self.Aes_input_file.clicked.connect(lambda: self.load_file_content(1, self.Aes_input_text, 0))
        self.Aes_decode_input_file.clicked.connect(lambda: self.load_file_content(1, self.Aes_decode_input_text, 0))
        self.rsa_plainText_input_file.clicked.connect(lambda: self.load_file_content(1, self.rsa_plainText, 0))
        self.rsa_cipherText_input_file.clicked.connect(lambda: self.load_file_content(1, self.rsa_cipherText, 0))
        self.messageInput_input_file.clicked.connect(lambda: self.load_file_content(1, self.messageInput_lineEdit, 0))
        self.verifyMessageInput_input_file.clicked.connect(lambda: self.load_file_content(1, self.verifyMessageInput_lineEdit, 0))

        self.Vigener_decode_input_file_2.clicked.connect(lambda: self.load_file_content(2, self.Vigener_decode_file_path, self.vigener))
        self.Des_decode_input_file_2.clicked.connect(lambda: self.load_file_content(2, self.Des_decode_file_path, self.des))
        self.Aes_decode_input_file_2.clicked.connect(lambda: self.load_file_content(2, self.Aes_decode_file_path, self.aes))
        self.rsaDecypher_input_file.clicked.connect(lambda: self.load_file_content(2, self.rsa_fileToDecypher, self.rsa))

        # Obsługa przyciskow do ladowania dowolnych pliow (base64)
        self.Vigener_input_file_2.clicked.connect(lambda: self.load_all_files_as_base64(self.Vigener_file_path, self.vigener))
        self.Des_input_file_2.clicked.connect(lambda: self.load_all_files_as_base64(self.Des_file_path, self.des))
        self.Aes_input_file_2.clicked.connect(lambda: self.load_all_files_as_base64(self.Aes_file_path, self.aes))
        self.rsaCypher_input_file.clicked.connect(lambda: self.load_all_files_as_base64(self.rsa_fileForCypher, self.rsa))


        # Obsługa przycisków do zapisywania zawartości do plików tekstowych
        self.Vigener_output_save.clicked.connect(lambda: self.save_content_to_file(1, self.Vigener_output))
        self.Vigener_decode_output_save.clicked.connect(lambda: self.save_content_to_file(1, self.Vigener_decode_output))
        self.transposition_output_save.clicked.connect(lambda: self.save_content_to_file(1, self.transposition_output))
        self.transposition_decode_output_save.clicked.connect(lambda: self.save_content_to_file(1, self.transposition_decode_output))
        self.Des_output_save.clicked.connect(lambda: self.save_content_to_file(1, self.Des_output))
        self.Des_decode_output_save.clicked.connect(lambda: self.save_content_to_file(1, self.Aes_decode_output))
        self.Aes_output_save.clicked.connect(lambda: self.save_content_to_file(1, self.Aes_output))
        self.Aes_decode_output_save.clicked.connect(lambda: self.save_content_to_file(1, self.Aes_decode_output))
        self.rsa_plainText_save.clicked.connect(lambda: self.save_content_to_file(1, self.rsa_plainText))
        self.rsa_cipherText_save.clicked.connect(lambda: self.save_content_to_file(1, self.rsa_cipherText))
        self.computedHmac_output_save.clicked.connect(lambda: self.save_content_to_file(1, self.computedHmac_output))



    def switch_main_page(self, index):
        self.stackedWidget.setCurrentIndex(index)




    def load_file_content(self, mode,  target_line_edit, target_encryption_metod):
        # Wyświetla okno dialogowe do wyboru pliku
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik tekstowy", "", "Pliki tekstowe (*.txt);;Wszystkie pliki (*)", options=options)
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    if mode == 1:
                        target_line_edit.setText(file_content)
                    elif mode == 2:
                        target_line_edit.setText(file_path)
                        target_encryption_metod.cipher_text_update(file_content)
            except Exception as e:
                print(f"Nie udało się załadować pliku: {e}")

    def save_content_to_file(self, mode, source_text):
        # Wyświetla okno dialogowe do wyboru miejsca zapisania pliku
        options = QFileDialog.Options()
        options |= QFileDialog.DontConfirmOverwrite
        file_path, _ = QFileDialog.getSaveFileName(self, "Zapisz plik tekstowy", "", "Pliki tekstowe (*.txt);;Wszystkie pliki (*)", options=options)
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    if mode==1:
                        file_content = source_text.toPlainText()
                    elif mode==2:
                        file_content = source_text
                    file.write(file_content)
            except Exception as e:
                print(f"Nie udało się zapisać pliku: {e}")




    def load_all_files_as_base64(self, target_line_edit, target_encryption_metod):
        # Wyświetla okno dialogowe do wyboru pliku
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Wszystkie pliki (*)", options=options)
        
        if file_path:
            try:
                with open(file_path, 'rb') as file:                                     # Otwórz plik w trybie binarnym
                    file_content = file.read()                                          # Odczytaj zawartość pliku
                    encoded_content = base64.b64encode(file_content).decode('utf-8')    # Koduj do Base64 i dekoduj na UTF-8
                    target_line_edit.setText(file_path)                                 # Ustaw ścieżkę pliku w linii edycyjnej
                    target_encryption_metod.text_update(encoded_content)                # Dodaj zakodowany plik do zmiennej wewnątrz klasy wykonawczej
            except Exception as e:
                print(f"Nie udało się załadować pliku: {e}")

    def save_to_file_using_base64(self, source_text):
        # Wyświetla okno dialogowe do wyboru miejsca zapisania pliku
        options = QFileDialog.Options()
        options |= QFileDialog.DontConfirmOverwrite
        file_path, _ = QFileDialog.getSaveFileName(self, "Zapisz plik", "", "Wszystkie pliki (*)", options=options)

        if file_path:
            try:
                base64_content = source_text                        # Odczytaj zakodowaną zawartość z pliku
                decoded_content = base64.b64decode(base64_content)  # Dekoduj Base64 do bajtów
                # Zapisz zawartość jako plik binarny
                with open(file_path, 'wb') as file:                 # Otwórz w trybie binarnym
                    file.write(decoded_content)
            except Exception as e:
                print(f"Nie udało się zapisać pliku: {e}")



    def closeEvent(self, event):
        self.network.stop()                             # Zamknięcie i czyszczenie klienta Network
        # for widget in self.findChildren(QWidget):
        #     widget.deleteLater()
        super().closeEvent(event)                       # Wywołanie metody bazowej


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())