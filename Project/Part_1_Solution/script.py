
from collections import Counter
import numpy as np

# English letter frequencies from A to Z
ef = np.array([
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094,
    0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929,
    0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
    0.01974, 0.00074
])
max_key_length_to_test = 20

def calculate_ic(text):
    text = text.lower()
    letter_freq = {chr(i + ord('a')): 0 for i in range(26)}
    total_letters = 0

    for char in text:
        if char.isalpha():
            letter_freq[char] += 1
            total_letters += 1

    ic = sum((freq * (freq - 1)) / (total_letters * (total_letters - 1)) for freq in letter_freq.values())
    return ic

def find_key_length(ciphertext, max_key_length):
    ic_values = []

    for key_length in range(1, max_key_length + 1):
        substrings = [''] * key_length

        for i, char in enumerate(ciphertext):
            substrings[i % key_length] += char

        ic = sum(calculate_ic(substring) for substring in substrings) / key_length
        ic_values.append(ic)

    # Find the index of the highest IC value to get the most probable key length
    most_probable_key_length = ic_values.index(max(ic_values)) + 1
    return most_probable_key_length

def find_key(ciphertext, exact_key_length):
    a = np.zeros((26,26), float)
    N = len(ciphertext)/exact_key_length
    a = np.zeros((26,26), float)
    N = len(ciphertext)/exact_key_length
    key = ''
    for y in range(exact_key_length):
        for i in range(97, 123):
            for j in range(y, len(ciphertext), exact_key_length):
                a[i-97][(ord(ciphertext[j]) - i)%26]+=1
        a = a/N
        vals = [np.linalg.norm(a[i]-ef) for i in range(26)]
        key+=chr(vals.index(min(vals))+97)
    return key

cipher = input("Enter the cypher text")

ciphertext = ''
for i in range(len(cipher)):
    if ord(cipher[i])>=97 and ord(cipher[i])<=122:
        ciphertext += cipher[i]


exact_key_length = find_key_length(ciphertext, max_key_length_to_test)
keyword = find_key(ciphertext, exact_key_length)
plaintext = ''
j = 0
for i in range(len(cipher)):
    if ord(cipher[i])>=97 and ord(cipher[i])<=122:
        c = keyword[j%len(keyword)]
        plaintext += chr(97 + (ord(cipher[i]) - ord(c))%26)
        j+=1
    else:
        plaintext += cipher[i]
print(plaintext)

    