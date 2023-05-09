import base64
encoded_s = "Y3Rme2doaWRyYV9pc19hd2Vzb21lfQ=="
decoded_s = base64.b64decode(encoded_s).decode('utf-8')
print(decoded_s)
