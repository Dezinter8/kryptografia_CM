import sys
import os
from PySide6.QtWidgets import QFileDialog, QMessageBox
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import PyPDF2
from encryptions.signatures.GenerateCert import certificates

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
        
        # Załadowanie głównego certyfikatu
        try:
            with open(certificate_file_path, "rb") as cert_file:
                cert_data = cert_file.read()
                certificate = x509.load_pem_x509_certificate(cert_data, default_backend())
                public_key = certificate.public_key()  # Klucz publiczny z certyfikatu
        except Exception as e:
            QMessageBox.warning(self.main_window, "Błąd", f"Błąd ładowania certyfikatu: {str(e)}")
            return
        
        # Wczytanie podpisu
        try:
            with open(signature_file_path, "rb") as sig_file:
                signature = sig_file.read()
        except Exception as e:
            QMessageBox.warning(self.main_window, "Błąd", f"Błąd ładowania podpisu: {str(e)}")
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
            QMessageBox.warning(self.main_window, "Błąd", f"Błąd przy odczycie pliku PDF: {str(e)}")
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


        # Wczytanie łańcucha certyfikacji z certificates.py
        try:
            # Ładowanie Root CA
            root_private_key = serialization.load_pem_private_key(
                certificates.ROOT_CA_PRIVATE_KEY.encode('utf-8'),
                password=None,
                backend=default_backend()
            )
            root_certificate = x509.load_pem_x509_certificate(
                certificates.ROOT_CA_CERT.encode('utf-8'),
                backend=default_backend()
            )

            # Ładowanie Intermediate CA
            intermediate_private_key = serialization.load_pem_private_key(
                certificates.INTERMEDIATE_CA_PRIVATE_KEY.encode('utf-8'),
                password=None,
                backend=default_backend()
            )
            intermediate_certificate = x509.load_pem_x509_certificate(
                certificates.INTERMEDIATE_CA_CERT.encode('utf-8'),
                backend=default_backend()
            )

            # Tworzenie listy certyfikatów w łańcuchu
            cert_chain = [certificate, intermediate_certificate, root_certificate]

            # Walidacja łańcucha certyfikatów
            chain_validation_result = self.validate_certificate_chain(cert_chain)
        except Exception as e:
            QMessageBox.warning(self.main_window, "Błąd", f"Błąd ładowania łańcucha certyfikatów: {str(e)}")
            return


        # Wyświetlanie wyników w GUI
        cert_info = self.get_full_chain_info(cert_chain)
        self.main_window.verifyOutput_textEdit.setPlainText(f"{verification_result}\n\n{chain_validation_result}\n\nMetadane certyfikatów:\n\n{cert_info}")


    def validate_certificate_chain(self, cert_chain):
        """
        Walidacja łańcucha certyfikatów.
        cert_chain: Lista certyfikatów od końcowego do Root CA.
        """
        try:
            for i in range(len(cert_chain) - 1):
                issuer_cert = cert_chain[i + 1]
                subject_cert = cert_chain[i]

                # Sprawdzenie, czy issuer cert jest emitentem subject cert
                if subject_cert.issuer != issuer_cert.subject:
                    return f"Błąd w łańcuchu: Issuer certyfikatu '{subject_cert.subject}' nie odpowiada Subject certyfikatu emitującego '{issuer_cert.subject}'."

                # Weryfikacja podpisu certyfikatu subject przy użyciu issuer_public_key
                issuer_public_key = issuer_cert.public_key()
                issuer_public_key.verify(
                    subject_cert.signature,
                    subject_cert.tbs_certificate_bytes,
                    padding.PKCS1v15(),
                    subject_cert.signature_hash_algorithm,
                )
            return "Łańcuch certyfikacji jest prawidłowy."
        except Exception as e:
            return f"Łańcuch certyfikacji jest nieprawidłowy: {str(e)}"

    def get_full_chain_info(self, cert_chain):
        """
        Zbiera informacje ze wszystkich certyfikatów w łańcuchu.
        cert_chain: Lista certyfikatów od końcowego do Root CA.
        """
        info = []
        for idx, cert in enumerate(cert_chain):
            cert_number = len(cert_chain) - idx  # Aby Root CA był pierwszy
            info.append(f"=== Certyfikat {cert_number} ===")
            info.append(self.get_certificate_info(cert))
            info.append("\n")
        return "\n".join(info)


    def get_certificate_info(self, certificate):
        """
        Wydobycie podstawowych informacji z certyfikatu i rozpisanie ich na sekcje.
        """
        subject = certificate.subject
        issuer = certificate.issuer

        cert_info = []
        cert_info.append("Dane podmiotu:")
        cert_info.append(f"  Imię i nazwisko: {self.get_attribute_value(subject, NameOID.COMMON_NAME)}")
        cert_info.append(f"  Organizacja: {self.get_attribute_value(subject, NameOID.ORGANIZATION_NAME)}")
        cert_info.append(f"  Jednostka organizacyjna: {self.get_attribute_value(subject, NameOID.ORGANIZATIONAL_UNIT_NAME)}")
        cert_info.append(f"  E-mail: {self.get_attribute_value(subject, NameOID.EMAIL_ADDRESS)}")
        cert_info.append(f"  Kraj: {self.get_attribute_value(subject, NameOID.COUNTRY_NAME)}")

        cert_info.append("\nDane emitenta:")
        cert_info.append(f"  Imię i nazwisko: {self.get_attribute_value(issuer, NameOID.COMMON_NAME)}")
        cert_info.append(f"  Organizacja: {self.get_attribute_value(issuer, NameOID.ORGANIZATION_NAME)}")
        cert_info.append(f"  Jednostka organizacyjna: {self.get_attribute_value(issuer, NameOID.ORGANIZATIONAL_UNIT_NAME)}")
        cert_info.append(f"  E-mail: {self.get_attribute_value(issuer, NameOID.EMAIL_ADDRESS)}")
        cert_info.append(f"  Kraj: {self.get_attribute_value(issuer, NameOID.COUNTRY_NAME)}")

        cert_info.append(f"\nNumer seryjny: {certificate.serial_number}")
        cert_info.append(f"Ważny od: {certificate.not_valid_before}")
        cert_info.append(f"Ważny do: {certificate.not_valid_after}")
        cert_info.append(f"Algorytm podpisu: {certificate.signature_algorithm_oid._name}")

        # Publiczny klucz
        public_key = certificate.public_key()
        public_key_info = self.get_public_key_info(public_key)
        cert_info.append(f"\nKlucz publiczny: {public_key_info}")

        return "\n".join(cert_info)

    def get_attribute_value(self, name, oid):
        """
        Pomaga w wyciąganiu wartości atrybutów z certyfikatu.
        """
        try:
            return name.get_attributes_for_oid(oid)[0].value
        except IndexError:
            return "Brak danych"

    def get_public_key_info(self, public_key):
        """
        Zwraca informacje o kluczu publicznym.
        """
        if isinstance(public_key, rsa.RSAPublicKey):
            numbers = public_key.public_numbers()
            return f"RSA ({numbers.e}, {numbers.n})"
        else:
            return "Inny typ klucza publicznego"









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
