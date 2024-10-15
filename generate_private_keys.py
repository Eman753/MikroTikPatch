#!/usr/bin/python3

from ecdsa import SigningKey, NIST384p
from nacl.signing import SigningKey as Ed25519SigningKey

# Génération clé KCDSA (EC-KCDSA)
kcdsa_private_key = SigningKey.generate(curve=NIST384p)
kcdsa_public_key = kcdsa_private_key.get_verifying_key()

# Sauvegarde des clés KCDSA
with open("kcdsa_private_key.pem", "wb") as f:
    f.write(kcdsa_private_key.to_pem())

with open("kcdsa_public_key.pem", "wb") as f:
    f.write(kcdsa_public_key.to_pem())

# Génération clé EdDSA (Ed25519)
eddsa_private_key = Ed25519SigningKey.generate()
eddsa_public_key = eddsa_private_key.verify_key

# Sauvegarde des clés EdDSA
with open("eddsa_private_key.pem", "wb") as f:
    f.write(eddsa_private_key.encode())

with open("eddsa_public_key.pem", "wb") as f:
    f.write(eddsa_public_key.encode())
