import gzip
import zlib
import rncryptor  # https://github.com/RNCryptor/RNCryptor

# Modify the rncryptor post_decrypt_data class to fit the algorithm
class RNCryptor_modified(rncryptor.RNCryptor):
    def post_decrypt_data(self, data):
        data = data[: -(data[-1])]
        return data


def recrypt_SEB(password):
    cryptor = RNCryptor_modified()
    with open("decrypted.seb", "rb") as f:
        file_content = f.read()
    compressed_sets = gzip.compress(file_content)
    recrypted_data = str.encode("pswd") + cryptor.encrypt(compressed_sets, password)
    compressed_data = gzip.compress(recrypted_data)

    with open("rencrypted.seb", "wb") as f:
        f.write(compressed_data)


recrypt_SEB(input("Input encryption password: "))
