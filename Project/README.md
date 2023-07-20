# The Final Project

## Part 1 - Vigenère Cracker

Write a script to input a Vigenère-encrypted ciphertext and print the plaintext and key. Find out how to perform cryptanalysis on the Vignère cipher using Google or elsewhere.

### Constraints
The input ciphertext will only contain lower case letters, spaces and punctuations. The spaces and punctuations are not encrypted. The key length would be less than or equal to 12 characters. You may use Python, C or C++ to write your script.

### Verifying your solution
You can use [these three sample test cases](./samples.txt) to verify your code. 

### Submission instruction
Create a file `script.py`/`script.c`/`script.cpp` which solves the challenge. Create a README file with clear instructions on how to execute your script.

## Part 2 - RSA Digital Signatures

Write a script called ```sign.py``` that takes in a the name of a text file as input and prints out the digital signature of that file as follows:
- It must first get the SHA-256 hash of the file (as bytes).
- Then it must create a random semiprime `N` to be used in the RSA digital signature.
- Then it signs the hash using RSA digital signature with `N` above and `e = 65537`.
- Finally, it returns `(N, e)` as a tuple and the the signature (in hex)

Create a separate script called ```verifier.py``` that takes in tha name of a text file, N, e, and a signature in hex and verifies the digital signature of the contents of the text file and returns ```accept``` or ```reject``` depending on whether the signature is valid or not.

### Submission Link
Add all files related to your project submission in a public GitHub repository or a publicly viewable Google Drive Folder. Submit the link to the GitHub repository or Google Drive Folder here: https://forms.gle/KCgXNanqxDV5n1LY9
