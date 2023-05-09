ciphertext = "qfti'{ B~!Mj\"@M!|Q`KbF#\"|o"
key = 0x12
plaintext = ""

for char in ciphertext:
    plaintext += chr(ord(char) ^ key)

print(plaintext)
