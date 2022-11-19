import gzip
import zlib
import rncryptor  # https://github.com/RNCryptor/RNCryptor
import plistlib
from hashlib import sha256

# Modify the rncryptor post_decrypt_data class to fit the algorithm
class RNCryptor_modified(rncryptor.RNCryptor):
    def post_decrypt_data(self, data):
        data = data[: -(data[-1])]
        return data


def decrypt_SEB(password, newpassword):
    cryptor = RNCryptor_modified()
    with gzip.open("encrypted.seb", "rb") as f:
        file_content = f.read()
    decrypted_data = cryptor.decrypt(file_content[4:], password)
    decompressed_data = zlib.decompress(decrypted_data, 15 + 32)
    parsed = plistlib.loads(decompressed_data)
    parsed["hashedAdminPassword"] = sha256(str.encode(newpassword)).hexdigest().upper()
    parsed["hashedQuitPassword"] = sha256(str.encode(newpassword)).hexdigest().upper()
    newparsed = plistlib.dumps(parsed, sort_keys=False)

    with open("decrypted.seb", "wb") as f:
        f.write(newparsed)


decrypt_SEB(input("Input password: "), input("New password: "))
