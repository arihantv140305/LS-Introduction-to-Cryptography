# verifier.py

import sys
import hashlib

def verify_signature(file_name, N, e, signature_hex):
    # Read the file and get the SHA-256 hash
    with open(file_name, 'rb') as file:
        file_content = file.read()
    file_hash = hashlib.sha256(file_content).digest()

    # Convert the signature from hex to int
    signature = int(signature_hex, 16)

    # Verify the signature using RSA
    decrypted_signature = pow(signature, e, N)

    # Check if the decrypted signature matches the hash
    return decrypted_signature == int.from_bytes(file_hash, byteorder='big')

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python verifier.py <file_name> <N> <e> <signature_hex>")
    else:
        file_name = sys.argv[1]
        N = int(sys.argv[2])
        e = int(sys.argv[3])
        signature_hex = sys.argv[4]

        result = verify_signature(file_name, N, e, signature_hex)
        if result:
            print("Accept")
        else:
            print("Reject")
