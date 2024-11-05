def bin_to_hex(pem_file):
    with open(pem_file, 'rb') as f:  # Ouverture en mode binaire
        binary_data = f.read()
    # Conversion des données binaires en hexadécimal
    return binary_data.hex()


# Utilisation
#result = str(input("Key file ->"))
#cle_privee_hex = pem_to_hex(result)
#print(cle_privee_hex)
