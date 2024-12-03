import sys
from PySide6.QtWidgets import QFileDialog
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from cryptography.x509 import CertificateSigningRequestBuilder, Name, NameAttribute
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend


class generateSignaruteWithKeys:
    def __init__(self, main_window):
        self.main_window = main_window

        self.main_window.generateCert_pushButton.clicked.connect(self.generate_certificate)



    def generate_certificate(self):
        name = self.main_window.nameInput_lineEdit.text()
        organizational_unit = self.main_window.organizationalUnitInput_lineEdit.text()
        organization_name = self.main_window.organizationNameInput_lineEdit.text()
        email = self.main_window.emailInput_lineEdit.text()
        country = self.main_window.countryInput_combobox.currentText()
        key_algo = int(self.main_window.keyAlgoInput_comboBox.currentText())
        
        # Validate inputs
        if not name or not organizational_unit or not organization_name or not email or not country or not key_algo:
            print("Wszystkie pola muszą być wypełnione!")
            return
        
        # Generate RSA private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_algo,
            backend=default_backend()
        )
        
        # Generate public key
        public_key = private_key.public_key()
        
        # Generate Certificate Signing Request (CSR)
        subject = Name([
            NameAttribute(NameOID.COMMON_NAME, name),
            NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, organizational_unit),
            NameAttribute(NameOID.ORGANIZATION_NAME, organization_name),
            NameAttribute(NameOID.EMAIL_ADDRESS, email),
            NameAttribute(NameOID.COUNTRY_NAME, country)
        ])
        
        csr = CertificateSigningRequestBuilder().subject_name(subject).add_extension(
            x509.SubjectAlternativeName([x509.RFC822Name(email)]),
            critical=False
        ).sign(private_key, hashes.SHA256(), default_backend())
        
        # Save private key to file
        private_key_path, _ = QFileDialog.getSaveFileName(self.main_window, "Zapisz klucz prywatny", "", "Private Key Files (*.pem)")
        if private_key_path:
            with open(private_key_path, "wb") as key_file:
                key_file.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                ))
        
        # Save public key to file
        public_key_path, _ = QFileDialog.getSaveFileName(self.main_window, "Zapisz klucz publiczny", "", "Public Key Files (*.pem)")
        if public_key_path:
            with open(public_key_path, "wb") as pub_key_file:
                pub_key_file.write(public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
        
        # Save CSR to file
        csr_path, _ = QFileDialog.getSaveFileName(self.main_window, "Zapisz CSR", "", "CSR Files (*.csr)")
        if csr_path:
            with open(csr_path, "wb") as csr_file:
                csr_file.write(csr.public_bytes(serialization.Encoding.PEM))
        
        print("Certyfikat i klucze zostały wygenerowane i zapisane.")
