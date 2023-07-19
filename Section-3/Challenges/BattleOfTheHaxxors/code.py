iv = 72
enc_flag = b"[REDACTED_FLAG]"
key = [4, 0, 1, 5, 2, 7, 6, 3]

length = len(enc_flag)
assert length == 32
print(hex(iv))

output = [None]*length
for i in range(length):
	x = enc_flag[i]
	x = x ^ iv
	acc = 0
	for j in range(8):
		b = (x >> j) & 1
		acc |= (b << key[j])
	iv = acc
	output[i] = acc

print(b''.join(map(lambda x: chr(x).encode(), output)).hex())
