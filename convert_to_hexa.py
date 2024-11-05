import base64

def pem_to_hex(pem_file):
    with open(pem_file, 'r') as f:
        pem_data = f.read()
    # Supprimer les en-têtes PEM
    pem_data = pem_data.replace('-----BEGIN PRIVATE KEY-----', '').replace('-----END PRIVATE KEY-----', '').strip()
    
    # Ajouter le padding si nécessaire
    missing_padding = len(pem_data) % 4
    if missing_padding != 0:
        pem_data += '=' * (4 - missing_padding)
    
    # Décoder la clé en base64 puis en binaire
    binary_data = base64.b64decode(pem_data)
    # Convertir en hexadécimal
    return binary_data.hex()

#result = str(input("Key file -> "))
# Utilisation
#cle_privee_hex = pem_to_hex(result)
#print(cle_privee_hex)
