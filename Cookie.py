import pickle
import base64

class profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user_profile = profile('admin', 'admin_password')
serialized = pickle.dumps(user_profile)
encoded = base64.b64encode(serialized).decode('utf-8')

cookie = ''
for i in range(len(encoded)):
    cookie += chr(ord(encoded[i]) ^ 0x03)

print(cookie)
