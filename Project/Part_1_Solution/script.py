cipher = input("Enter the cypher text")
keyword = input("Enter the keyword")
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

    