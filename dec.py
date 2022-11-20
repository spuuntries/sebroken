import gzip
import zlib
import rncryptor
import plistlib
from tqdm import tqdm
from hashlib import sha256

# Modify the rncryptor post_decrypt_data class to fit the algorithm
class RNCryptor_modified(rncryptor.RNCryptor):
    def post_decrypt_data(self, data):
        data = data[: -(data[-1])]
        return data


def decrypt_SEB(password, newpassword, in_file):
    pbar = tqdm(total=100)

    pbar.set_description("Setting up...")
    cryptor = RNCryptor_modified()
    pbar.update(10)

    pbar.set_description("Loading file...")
    with gzip.open(in_file, "rb") as f:
        file_content = f.read()
    pbar.set_description("File loaded!")
    pbar.update(40)

    pbar.set_description("Decrypting file...")
    decrypted_data = cryptor.decrypt(file_content[4:], password)
    pbar.update(10)

    pbar.set_description("Decompressing file...")
    decompressed_data = zlib.decompress(decrypted_data, 15 + 32)
    pbar.set_description("Decompressed.")
    pbar.update(20)

    pbar.set_description("Loading as plist...")
    parsed = plistlib.loads(decompressed_data)
    pbar.set_description("Loaded.")
    pbar.update(5)

    pbar.set_description("Applying patches...")
    parsed["hashedAdminPassword"] = sha256(str.encode(newpassword)).hexdigest().upper()
    parsed["hashedQuitPassword"] = sha256(str.encode(newpassword)).hexdigest().upper()
    pbar.set_description("Applied.")
    pbar.update(5)

    pbar.set_description("Dumping...")
    newparsed = plistlib.dumps(parsed, sort_keys=False)

    with open(f"{in_file.split('.').pop(0)}.decrypted.seb", "wb") as f:
        f.write(newparsed)
    pbar.update(10)
    pbar.set_description("Done!")
    pbar.close()
