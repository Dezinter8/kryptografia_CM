import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QFileDialog, QLabel
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import PyPDF2

class verifySignature:
    def __init__(self, main_window):
        self.main_window = main_window

        self.main_window.verify_pushButton.clicked.connect(self.verify_signature)

        self.main_window.loadPdf_pushButton_2.clicked.connect(self.load_pdf_file)
        self.main_window.loadCsr_pushButton.clicked.connect(self.load_certificate_file)
        self.main_window.loadPem_pushButton.clicked.connect(self.load_key_file)

    
    def verify_signature(self):
        pdf_file_path = self.main_window.pdfPath_lineEdit_2.text()
        signature_file_path = self.main_window.csrPath_lineEdit.text()
        public_key_path = self.main_window.pemPath_lineEdit.text()
        
        # Validate inputs
        if not pdf_file_path or not signature_file_path or not public_key_path:
            print("Wszystkie pola muszą być wypełnione!")
            return
        
        if not os.path.isfile(pdf_file_path):
            print("Nie znaleziono pliku PDF!")
            return
        
        if not os.path.isfile(signature_file_path):
            print("Nie znaleziono pliku podpisu!")
            return
        
        if not os.path.isfile(public_key_path):
            print("Nie znaleziono klucza publicznego!")
            return
        
        # Load public key
        public_key = None
        with open(public_key_path, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        
        # Read the signature
        with open(signature_file_path, "rb") as sig_file:
            signature = sig_file.read()
        
        # Load PDF and extract text for hashing
        with open(pdf_file_path, 'rb') as input_pdf:
            reader = PyPDF2.PdfReader(input_pdf)
            pdf_hash = hashes.Hash(hashes.SHA256(), backend=default_backend())
            for page in reader.pages:
                pdf_hash.update(page.extract_text().encode())
        
        # Verify the signature
        self.verify_pdf_signature(pdf_hash.finalize(), signature, public_key)
    
    def verify_pdf_signature(self, document_hash, signature, public_key):
        try:
            # Verify the signature using the public key
            public_key.verify(
                signature,
                document_hash,
                padding.PKCS1v15(),
                hashes.SHA256()
            )
            print("Podpis jest prawidłowy.")
        except Exception as e:
            print(f"Podpis jest nieprawidłowy: {str(e)}")






    def load_pdf_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Wybierz plik pdf", "", "PDF Files (*.pdf);;Wszystkie pliki (*)")
        
        if file_path:
            try:
                self.main_window.pdfPath_lineEdit_2.setText(file_path)
            except Exception as e:
                print(f"Nie udało się załadować pliku: {e}")

    def load_certificate_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Wybierz plik certyfikatu", "", "CSR Files (*.csr);;Wszystkie pliki (*)")
        
        if file_path:
            try:
                self.main_window.csrPath_lineEdit.setText(file_path)
            except Exception as e:
                print(f"Nie udało się załadować pliku: {e}")

    def load_key_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Wybierz klucz publiczny", "", "PEM Files (*.pem);;Wszystkie pliki (*)")
        
        if file_path:
            try:
                self.main_window.pemPath_lineEdit.setText(file_path)
            except Exception as e:
                print(f"Nie udało się załadować pliku: {e}")
