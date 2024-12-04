import sys
import os
from PySide6.QtWidgets import QFileDialog, QMessageBox
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import PyPDF2

class verifySignature:
    def __init__(self, main_window):
        self.main_window = main_window

        self.main_window.verify_pushButton.clicked.connect(self.verify_signature)

        self.main_window.loadPdf_pushButton_2.clicked.connect(self.load_pdf_file)
        self.main_window.loadSig_pushButton.clicked.connect(self.load_signature_file)
        self.main_window.loadCsr_pushButton.clicked.connect(self.load_certyficate_file)

    
    def verify_signature(self):
        pdf_file_path = self.main_window.pdfPath_lineEdit_2.text()
        signature_file_path = self.main_window.signaturePath_lineEdit.text()
        certificate_file_path  = self.main_window.certificatePath_lineEdit.text()
        
        # Walidacja wejściowych ścieżek
        if not pdf_file_path or not signature_file_path or not certificate_file_path:
            QMessageBox.warning(self.main_window, "Błąd", "Wszystkie pola muszą być wypełnione!")
            return
        
        if not os.path.isfile(pdf_file_path):
            QMessageBox.warning(self.main_window, "Błąd", "Nie znaleziono pliku PDF!")
            return
        
        if not os.path.isfile(signature_file_path):
            QMessageBox.warning(self.main_window, "Błąd", "Nie znaleziono pliku podpisu!")
            return
        
        if not os.path.isfile(certificate_file_path):
            QMessageBox.warning(self.main_window, "Błąd", "Nie znaleziono pliku certyfikatu!")
            return
        
        # Załadowanie certyfikatu
        try:
            with open(certificate_file_path, "rb") as cert_file:
                cert_data = cert_file.read()
                certificate = x509.load_pem_x509_certificate(cert_data, default_backend())
                public_key = certificate.public_key()  # Klucz publiczny z certyfikatu
        except Exception as e:
            QMessageBox.warning(self.main_window, "Błąd", "Błąd ładowania certyfikatu: {str(e)}")
            return
        
        # Wczytanie podpisu
        try:
            with open(signature_file_path, "rb") as sig_file:
                signature = sig_file.read()
        except Exception as e:
            QMessageBox.warning(self.main_window, "Błąd", "Błąd ładowania podpisu: {str(e)}")
            return

        # Wczytanie pliku PDF i obliczenie jego skrótu (hash)
        try:
            with open(pdf_file_path, 'rb') as input_pdf:
                reader = PyPDF2.PdfReader(input_pdf)
                pdf_hash = hashes.Hash(hashes.SHA256(), backend=default_backend())
                for page in reader.pages:
                    # Wyciąganie tekstu z każdej strony PDF
                    page_text = page.extract_text()
                    if page_text:
                        pdf_hash.update(page_text.encode())
                document_hash = pdf_hash.finalize()
        except Exception as e:
            QMessageBox.warning(self.main_window, "Błąd", "Błąd przy odczycie pliku PDF: {str(e)}")
            return
        
        # Weryfikacja podpisu
        try:
            public_key.verify(
                signature,
                document_hash,
                padding.PKCS1v15(),
                hashes.SHA256()
            )
            verification_result = "Podpis jest prawidłowy."
        except Exception as e:
            verification_result = f"Podpis jest nieprawidłowy: {str(e)}"

        # Wyświetlanie wyników w GUI
        cert_info = self.get_certificate_info(certificate)
        self.main_window.verifyOutput_textEdit.setPlainText(f"{verification_result}\n\nMetadane certyfikatu:\n\n{cert_info}")



    def get_certificate_info(self, certificate):
        # Wydobycie podstawowych informacji z certyfikatu i rozpisanie ich na sekcje
        subject = certificate.subject
        issuer = certificate.issuer
        
        cert_info = []
        cert_info.append("Dane podmiotu:")
        cert_info.append(f"  Imię i nazwisko: {self.get_attribute_value(subject, 'commonName')}")
        cert_info.append(f"  Organizacja: {self.get_attribute_value(subject, 'organizationName')}")
        cert_info.append(f"  Jednostka organizacyjna: {self.get_attribute_value(subject, 'organizationalUnitName')}")
        cert_info.append(f"  E-mail: {self.get_attribute_value(subject, 'emailAddress')}")
        cert_info.append(f"  Kraj: {self.get_attribute_value(subject, 'countryName')}")
        
        cert_info.append("\nDane emitenta:")
        cert_info.append(f"  Imię i nazwisko: {self.get_attribute_value(issuer, 'commonName')}")
        cert_info.append(f"  Organizacja: {self.get_attribute_value(issuer, 'organizationName')}")
        cert_info.append(f"  Jednostka organizacyjna: {self.get_attribute_value(issuer, 'organizationalUnitName')}")
        cert_info.append(f"  E-mail: {self.get_attribute_value(issuer, 'emailAddress')}")
        cert_info.append(f"  Kraj: {self.get_attribute_value(issuer, 'countryName')}")
        
        cert_info.append(f"\nNumer seryjny: {certificate.serial_number}")
        cert_info.append(f"Ważny od: {certificate.not_valid_before_utc}")
        cert_info.append(f"Ważny do: {certificate.not_valid_after_utc}")
        cert_info.append(f"Algorytm szyfrujący: {certificate.signature_algorithm_oid._name}")
        
        # Możemy dodać publiczny klucz
        cert_info.append(f"\nKlucz publiczny: {certificate.public_key().public_numbers()}")
        
        return "\n".join(cert_info)

    def get_attribute_value(self, name, attribute):
        # Pomaga w wyciąganiu wartości atrybutów z certyfikatu
        for attr in name:
            if attr.oid._name == attribute:
                return attr.value
        return "Brak danych"









    def load_pdf_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Wybierz plik pdf", "", "PDF Files (*.pdf);;Wszystkie pliki (*)")
        
        if file_path:
            try:
                self.main_window.pdfPath_lineEdit_2.setText(file_path)
            except Exception as e:
                QMessageBox.warning(self.main_window, "Błąd", "Nie udało się załadować pliku: {e}")

    def load_signature_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Wybierz plik podpisu", "", "SIG Files (*.sig);;Wszystkie pliki (*)")
        
        if file_path:
            try:
                self.main_window.signaturePath_lineEdit.setText(file_path)
            except Exception as e:
                QMessageBox.warning(self.main_window, "Błąd", "Nie udało się załadować pliku: {e}")

    def load_certyficate_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Wybierz plik certyfikatu", "", "CRT Files (*.crt);;Wszystkie pliki (*)")
        
        if file_path:
            try:
                self.main_window.certificatePath_lineEdit.setText(file_path)
            except Exception as e:
                QMessageBox.warning(self.main_window, "Błąd", "Nie udało się załadować pliku: {e}")
