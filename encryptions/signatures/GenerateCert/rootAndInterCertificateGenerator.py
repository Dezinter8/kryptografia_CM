# CertificateGenerator.py

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta
import os

def generate_root_ca(name, organizational_unit, organization_name, email, country, key_size=4096):
    # Generowanie klucza prywatnego Root CA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )

    # Budowanie subject i issuer (self-signed)
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, name),
        x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, organizational_unit),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization_name),
        x509.NameAttribute(NameOID.EMAIL_ADDRESS, email),
        x509.NameAttribute(NameOID.COUNTRY_NAME, country)
    ])

    # Okres ważności: 10 lat
    not_valid_before = datetime.utcnow()
    not_valid_after = not_valid_before + timedelta(days=3650)

    # Budowanie certyfikatu
    certificate = x509.CertificateBuilder(
    ).subject_name(subject
    ).issuer_name(issuer
    ).public_key(private_key.public_key()
    ).serial_number(x509.random_serial_number()
    ).not_valid_before(not_valid_before
    ).not_valid_after(not_valid_after
    ).add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True
    ).add_extension(
        x509.KeyUsage(
            key_cert_sign=True,
            crl_sign=True,
            digital_signature=False,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=False,
            content_commitment=False,
            encipher_only=False,
            decipher_only=False
        ),
        critical=True
    ).sign(private_key, hashes.SHA256(), default_backend())

    return private_key, certificate

def generate_intermediate_ca(root_private_key, root_certificate, name, organizational_unit, organization_name, email, country, key_size=2048):
    # Generowanie klucza prywatnego Intermediate CA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )

    # Budowanie subject
    subject = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, name),
        x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, organizational_unit),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization_name),
        x509.NameAttribute(NameOID.EMAIL_ADDRESS, email),
        x509.NameAttribute(NameOID.COUNTRY_NAME, country)
    ])

    # Issuer to Root CA
    issuer = root_certificate.subject

    # Okres ważności: 5 lat
    not_valid_before = datetime.utcnow()
    not_valid_after = not_valid_before + timedelta(days=1825)

    # Budowanie certyfikatu
    certificate = x509.CertificateBuilder(
    ).subject_name(subject
    ).issuer_name(issuer
    ).public_key(private_key.public_key()
    ).serial_number(x509.random_serial_number()
    ).not_valid_before(not_valid_before
    ).not_valid_after(not_valid_after
    ).add_extension(
        x509.BasicConstraints(ca=True, path_length=0), critical=True
    ).add_extension(
        x509.KeyUsage(
            key_cert_sign=True,
            crl_sign=True,
            digital_signature=False,
            key_encipherment=False,
            data_encipherment=False,
            key_agreement=False,
            content_commitment=False,
            encipher_only=False,
            decipher_only=False
        ),
        critical=True
    ).sign(root_private_key, hashes.SHA256(), default_backend())

    return private_key, certificate

def pem_encode_private_key(private_key):
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode('utf-8')

def pem_encode_certificate(certificate):
    return certificate.public_bytes(serialization.Encoding.PEM).decode('utf-8')

def main():
    print("Generowanie certyfikatów Root CA i Intermediate CA")

    # Dane dla Root CA
    print("\n=== Dane dla Root CA ===")
    root_name = input("Nazwa (Common Name): ")
    root_ou = input("Jednostka organizacyjna (Organizational Unit): ")
    root_on = input("Nazwa organizacji (Organization Name): ")
    root_email = input("Email: ")
    root_country = input("Kraj (Country): ")

    # Generowanie Root CA
    print("\nGenerowanie Root CA...")
    root_private_key, root_certificate = generate_root_ca(
        name=root_name,
        organizational_unit=root_ou,
        organization_name=root_on,
        email=root_email,
        country=root_country,
        key_size=4096
    )
    print("Root CA wygenerowany.")

    # Dane dla Intermediate CA
    print("\n=== Dane dla Intermediate CA ===")
    inter_name = input("Nazwa (Common Name): ")
    inter_ou = input("Jednostka organizacyjna (Organizational Unit): ")
    inter_on = input("Nazwa organizacji (Organization Name): ")
    inter_email = input("Email: ")
    inter_country = input("Kraj (Country): ")

    # Generowanie Intermediate CA
    print("\nGenerowanie Intermediate CA...")
    intermediate_private_key, intermediate_certificate = generate_intermediate_ca(
        root_private_key=root_private_key,
        root_certificate=root_certificate,
        name=inter_name,
        organizational_unit=inter_ou,
        organization_name=inter_on,
        email=inter_email,
        country=inter_country,
        key_size=2048
    )
    print("Intermediate CA wygenerowany.")

    # Kod do zapisania w certificates.py
    certificates_content = f'''# certificates.py

ROOT_CA_PRIVATE_KEY = """{pem_encode_private_key(root_private_key)}"""

ROOT_CA_CERT = """{pem_encode_certificate(root_certificate)}"""

INTERMEDIATE_CA_PRIVATE_KEY = """{pem_encode_private_key(intermediate_private_key)}"""

INTERMEDIATE_CA_CERT = """{pem_encode_certificate(intermediate_certificate)}"""
'''

    # Zapisywanie do certificates.py
    output_path = os.path.join(os.path.dirname(__file__), 'certificates.py')
    with open(output_path, 'w') as cert_file:
        cert_file.write(certificates_content)

    print(f"\ncertificates.py został wygenerowany i zapisany w katalogu projektu: {output_path}")

if __name__ == "__main__":
    main()
