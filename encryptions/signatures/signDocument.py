import sys
import PyPDF2
from PySide6.QtWidgets import QFileDialog, QMessageBox
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import os

class signDocument:
    def __init__(self, main_window):
        self.main_window = main_window

        self.main_window.signDocument_pushButton.clicked.connect(self.sign_pdf)
        
        self.main_window.loadPdf_pushButton.clicked.connect(self.load_pdf_file)
        self.main_window.loadPrivateKey_pushButton.clicked.connect(self.load_key_file)



    def sign_pdf(self):
        pdf_file_path = self.main_window.pdfPath_lineEdit.text()
        private_key_path = self.main_window.privateKeyPath_lineEdit.text()
        
        # Validate inputs
        if not pdf_file_path or not private_key_path:
            QMessageBox.warning(self.main_window, "Błąd", "Wszystkie pola muszą być wypełnione!")
            return
        
        if not os.path.isfile(pdf_file_path):
            QMessageBox.warning(self.main_window, "Błąd", "Nie znaleziono pliku PDF!")
            return
        
        if not os.path.isfile(private_key_path):
            QMessageBox.warning(self.main_window, "Błąd", "Nie znaleziono klucza prywatnego!")
            return
        
        # Load private key
        private_key = None
        with open(private_key_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        
        # Sign the PDF document
        self.add_signature_to_pdf(pdf_file_path, private_key)
        
        
    def add_signature_to_pdf(self, pdf_file_path, private_key):
        try:
            with open(pdf_file_path, 'rb') as input_pdf:
                reader = PyPDF2.PdfReader(input_pdf)
                writer = PyPDF2.PdfWriter()

                # Kopiowanie stron z pliku PDF
                for page in reader.pages:
                    writer.add_page(page)

                # Tworzenie podpisu (obliczanie skrótu dokumentu)
                pdf_hash = hashes.Hash(hashes.SHA256(), backend=default_backend())
                for page in reader.pages:
                    pdf_hash.update(page.extract_text().encode())

                signature = private_key.sign(
                    pdf_hash.finalize(),
                    padding.PKCS1v15(),
                    hashes.SHA256()
                )

                # Zapisanie podpisanego pliku PDF
                signed_pdf_path, _ = QFileDialog.getSaveFileName(self.main_window, "Zapisz podpisany PDF", "", "PDF Files (*.pdf)")
                if signed_pdf_path:
                    with open(signed_pdf_path, 'wb') as output_pdf:
                        writer.write(output_pdf)

                    # Zapisanie podpisu w osobnym pliku
                    signature_file_path = signed_pdf_path.replace(".pdf", "_signature.sig")
                    with open(signature_file_path, 'wb') as sig_file:
                        sig_file.write(signature)

                    print("Dokument został podpisany i zapisany.")
        except Exception as e:
            QMessageBox.warning(self.main_window, "Błąd", "Nie udało się podpisać dokumentu: {str(e)}")

















    def load_pdf_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Wybierz plik pdf", "", "PDF Files (*.pdf);;Wszystkie pliki (*)")
        
        if file_path:
            try:
                self.main_window.pdfPath_lineEdit.setText(file_path)
            except Exception as e:
                print(f"Nie udało się załadować pliku: {e}")


    def load_key_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Wybierz klucz prywatny", "", "PEM Files (*.pem);;Wszystkie pliki (*)")
        
        if file_path:
            try:
                self.main_window.privateKeyPath_lineEdit.setText(file_path)
            except Exception as e:
                print(f"Nie udało się załadować pliku: {e}")
