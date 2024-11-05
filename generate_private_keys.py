#!/usr/bin/python3

from convert_to_hexa import *
from testedd import *
import os
import subprocess

from ecdsa import SigningKey, NIST384p
from nacl.signing import SigningKey as Ed25519SigningKey

# Génération clé KCDSA (EC-KCDSA)
kcdsa_private_key = SigningKey.generate(curve=NIST384p)
kcdsa_public_key = kcdsa_private_key.get_verifying_key()

def export_to_bash(variable_name, variable_value):
    # Exporter la variable dans l'environnement Bash
    bash_command = f"export {variable_name}={variable_value}"
    subprocess.run(bash_command, shell=True, executable='/bin/bash')

# Sauvegarde des clés KCDSA
with open("kcdsa_private_key.pem", "wb") as f:
    f.write(kcdsa_private_key.to_pem())

converted_key = pem_to_hex('kcdsa_private_key.pem')

export_to_bash('CUSTOM_LICENSE_PRIVATE_KEY',converted_key)

print("Clef KCDSA privée : "+converted_key)

print("")

with open("kcdsa_public_key.pem", "wb") as f:
    f.write(kcdsa_public_key.to_pem())

converted_key = pem_to_hex('kcdsa_public_key.pem')

export_to_bash('CUSTOM_LICENSE_PUBLIC_KEY',converted_key)

print("Clef KCDSA publique : "+converted_key)

print("")

# Génération clé EdDSA (Ed25519)
eddsa_private_key = Ed25519SigningKey.generate()
eddsa_public_key = eddsa_private_key.verify_key

# Sauvegarde des clés EdDSA
with open("eddsa_private_key.pem", "wb") as f:
    f.write(eddsa_private_key.encode())

converted_key = bin_to_hex('eddsa_private_key.pem')

export_to_bash('CUSTOM_NPK_SIGN_PRIVATE_KEY',converted_key)

print("Clef EDDSA privée : "+converted_key)

print("")

with open("eddsa_public_key.pem", "wb") as f:
    f.write(eddsa_public_key.encode())

converted_key = bin_to_hex('eddsa_public_key.pem')

export_to_bash('CUSTOM_NPK_SIGN_PUBLIC_KEY',converted_key)

print("Clef EDDSA publique : "+converted_key)