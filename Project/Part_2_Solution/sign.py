# sign.py

import sys
import hashlib
import random
import sympy

def generate_semiprime(bits):
    while True:
        p = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
        q = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
        N = p * q
        if p != q and N.bit_length() == bits:
            return N, p, q

def generate_private_exponent(e, p, q):
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)  # Modular inverse of e modulo phi
    return d

def sign_file(file_name):
    # Read the file and get the SHA-256 hash
    with open(file_name, 'rb') as file:
        file_content = file.read()
    file_hash = hashlib.sha256(file_content).digest()

    # Generate a random semiprime N and its prime factors p and q
    N, p, q = generate_semiprime(2048)

    # Use e = 65537 for RSA
    e = 65537

    # Generate the private exponent d
    d = generate_private_exponent(e, p, q)

    # Calculate the signature using RSA
    signature = pow(int.from_bytes(file_hash, byteorder='big'), d, N)

    return (N, e), hex(signature)[2:]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sign.py <file_name>")
    else:
        file_name = sys.argv[1]
        keys, signature = sign_file(file_name)
        print("Keys:", keys)
        print("Signature:", signature)
