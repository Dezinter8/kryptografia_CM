import sys
from PySide6.QtWidgets import QFileDialog, QMessageBox
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from cryptography.x509 import CertificateSigningRequestBuilder, Name, NameAttribute
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from datetime import datetime, timedelta


class generateSignaruteWithKeys:
    def __init__(self, main_window):
        self.main_window = main_window

        self.main_window.generateCert_pushButton.clicked.connect(self.generate_certificate)



    def generate_certificate(self):
        # Pobranie danych z formularza
        name = self.main_window.nameInput_lineEdit.text()
        organizational_unit = self.main_window.organizationalUnitInput_lineEdit.text()
        organization_name = self.main_window.organizationNameInput_lineEdit.text()
        email = self.main_window.emailInput_lineEdit.text()
        country = self.main_window.countryInput_combobox.currentText()
        key_algo = int(self.main_window.keyAlgoInput_comboBox.currentText())


        if not name or not organizational_unit or not organization_name or not email or not country or not key_algo:
            QMessageBox.warning(self.main_window, "Błąd", "Wszystkie pola muszą być wypełnione!")
            return

        # Generate RSA private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_algo,
            backend=default_backend()
        )

        # Generate public key
        public_key = private_key.public_key()

        # Dane certyfikatu
        subject = x509.Name([
            x509.NameAttribute(x509.NameOID.COMMON_NAME, name),
            x509.NameAttribute(x509.NameOID.ORGANIZATIONAL_UNIT_NAME, organizational_unit),
            x509.NameAttribute(x509.NameOID.ORGANIZATION_NAME, organization_name),
            x509.NameAttribute(x509.NameOID.EMAIL_ADDRESS, email),
            x509.NameAttribute(x509.NameOID.COUNTRY_NAME, country)
        ])


        # Czas ważności certyfikatu
        not_valid_before = datetime.utcnow()
        not_valid_after = not_valid_before + timedelta(days=365)

        # Budowanie certyfikatu
        certificate = x509.CertificateBuilder().subject_name(subject).issuer_name(subject).public_key(public_key).serial_number(x509.random_serial_number()).not_valid_before(not_valid_before).not_valid_after(not_valid_after).add_extension(x509.SubjectAlternativeName([x509.RFC822Name(email)]), critical=False).sign(private_key, hashes.SHA256(), default_backend())


        # Zapisywanie klucza prywatnego
        private_key_path, _ = QFileDialog.getSaveFileName(self.main_window, "Zapisz klucz prywatny", "", "Private Key Files (*.pem)")
        if private_key_path:
            with open(private_key_path, "wb") as key_file:
                key_file.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                ))

        # Zapisywanie klucza publicznego
        public_key_path, _ = QFileDialog.getSaveFileName(self.main_window, "Zapisz klucz publiczny", "", "Public Key Files (*.pem)")
        if public_key_path:
            with open(public_key_path, "wb") as pub_key_file:
                pub_key_file.write(public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))

        # Zapisywanie certyfikatu
        cert_path, _ = QFileDialog.getSaveFileName(self.main_window, "Zapisz certyfikat", "", "Certificate Files (*.crt)")
        if cert_path:
            with open(cert_path, "wb") as cert_file:
                cert_file.write(certificate.public_bytes(serialization.Encoding.PEM))

        print("Certyfikat i klucze zostały wygenerowane i zapisane.")
