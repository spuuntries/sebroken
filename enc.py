import gzip
import rncryptor
from tqdm import tqdm

# Modify the rncryptor post_decrypt_data class to fit the algorithm
class RNCryptor_modified(rncryptor.RNCryptor):
    def post_decrypt_data(self, data):
        data = data[: -(data[-1])]
        return data


def recrypt_SEB(password, in_file, out_file):
    pbar = tqdm(total=100)

    pbar.set_description("Setting up...")
    cryptor = RNCryptor_modified()
    pbar.update(20)

    pbar.set_description("Loading file...")
    with open(in_file, "rb") as f:
        file_content = f.read()
    pbar.set_description("File loaded!")
    pbar.update(20)

    pbar.set_description("Compressing contents...")
    compressed_sets = gzip.compress(file_content)
    pbar.set_description("Compressed!")
    pbar.update(20)

    pbar.set_description("Padding and encrypting contents...")
    recrypted_data = str.encode("pswd") + cryptor.encrypt(compressed_sets, password)
    pbar.set_description("Encrypted!")
    pbar.update(20)

    pbar.set_description("Compressing...")
    compressed_data = gzip.compress(recrypted_data)

    with open(out_file, "wb") as f:
        f.write(compressed_data)
    pbar.set_description("Compressed!")
    pbar.update(20)

    pbar.set_description("Done!")
    pbar.close()
