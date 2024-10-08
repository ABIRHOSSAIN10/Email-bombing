import base64
import zlib
import os

def encode_file(input_file, output_file):
    # Read the original code from the input file
    with open(input_file, 'r') as f:
        code = f.read()

    # Compress and then encode
    compressed = zlib.compress(code.encode('utf-8'))
    encoded = base64.b64encode(compressed).decode('utf-8')

    # Prepare the obfuscated code for execution
    obfuscated_code = (
        "import base64, zlib; "
        "exec(zlib.decompress(base64.b64decode(b'{}')).decode('utf-8'))"
    ).format(encoded.replace("'", "\\'").replace('"', '\\"'))

    # Write the obfuscated code to the output file
    with open(output_file, 'w') as f:
        f.write(obfuscated_code)

    # Make it executable (only works on Unix-like systems)
    os.chmod(output_file, 0o755)




import marshal, base64, zlib, bz2
from Crypto.Cipher import AES, Blowfish, ChaCha20
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.Padding import unpad, pad
from Crypto.Random import get_random_bytes

def rsa_encrypt_large(data, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = bytearray()
    for i in range(0, len(data), 214):
        chunk = data[i:i+214]
        encrypted.extend(cipher.encrypt(chunk))
    return bytes(encrypted)

# Generate RSA keys (for demonstration, save/export private key securely in a real scenario)
key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

def encode_python_file(file_path, output_path):
    with open(file_path, 'r') as f:
        code = f.read()

    aes_key = get_random_bytes(16)
    blowfish_key = get_random_bytes(16)
    chacha_key = get_random_bytes(32)

    # Step 1: Marshal, Compress, and Encrypt the Data
    data = bz2.compress(zlib.compress((code.encode())))
   

    # Step 2: AES Encryption
    aes_iv = get_random_bytes(16)
    data = aes_iv + AES.new(aes_key, AES.MODE_CBC, iv=aes_iv).encrypt(pad(data, AES.block_size))

    # Step 3: Blowfish Encryption
    blowfish_iv = get_random_bytes(8)
    data = blowfish_iv + Blowfish.new(blowfish_key, Blowfish.MODE_CBC, iv=blowfish_iv).encrypt(pad(data, Blowfish.block_size))

    # Step 4: ChaCha20 Encryption
    chacha_nonce = get_random_bytes(12)
    data = chacha_nonce + ChaCha20.new(key=chacha_key, nonce=chacha_nonce).encrypt(data)

    # Step 5: RSA Encryption for the keys
    encrypted_key = rsa_encrypt_large(aes_key + blowfish_key + chacha_key, public_key)

    # Base64 encode the data for embedding
    data = base64.b64encode(encrypted_key + data).decode('utf-8')

    # Export the private key to a PEM string (You can adjust this to export the key elsewhere)
    private_key_pem = private_key.export_key().decode('utf-8')
    # Generate the execution code with decryption logic
    exec_code = f"""
import marshal as O00O0O000
import base64 as O0O00O0O0
import zlib as O0O0O00O0
import bz2 as O00O000O0
from Crypto.Cipher import AES as O0O00000O0
from Crypto.Cipher import Blowfish as O0O0O00000
from Crypto.Cipher import ChaCha20 as O00O0O0000O
from Crypto.PublicKey import RSA as O0O00O0000
from Crypto.Cipher import PKCS1_OAEP as O0O0O0O0O0
from Crypto.Util.Padding import unpad as O00O0OOO0
def O0O00O00O00(OO00OO000O0O00OOO0000O, O00OO0OO0OOO0O000O):
    O0O000OO0O = O0O0O0O0O0.new(O00OO0OO0OOO0O000O)
    OOO0O00000 = bytearray()
    O000000OO0 = 256
    for O0O0000OO0 in range(0, len(OO00OO000O0O00OOO0000O), O000000OO0):
        OOO0OO0O0O = OO00OO000O0O00OOO0000O[O0O0000OO0:O0O0000OO0+O000000OO0]
        OOO0O00000.extend(O0O000OO0O.decrypt(OOO0OO0O0O))
    return bytes(OOO0O00000)
O0O0O00O0O = '''{private_key_pem}'''
O00OO0OO0OOO0O000O = O0O00O0000.import_key(O0O0O00O0O)
data = O0O00O0O0.b64decode("{data}")
O0000000O0 = data[:256]
O0OO0000O0 = data[256:]
O0O00000O0_key, O0O0O00000_key, O0O0OO00OOO0000OO0O0OO0OO = O0O00O00O00(O0000000O0, O00OO0OO0OOO0O000O)[:16], O0O00O00O00(O0000000O0, O00OO0OO0OOO0O000O)[16:32], O0O00O00O00(O0000000O0, O00OO0OO0OOO0O000O)[32:64]
O0O0OO0000 = O0OO0000O0[:12]
O0OO0000O0 = O00O0O0000O.new(key=O0O0OO00OOO0000OO0O0OO0OO, nonce=O0O0OO0000).decrypt(O0OO0000O0[12:])
O0OO0O00OO = O0OO0000O0[:8]
O0OO0000O0 = O0O0O00000.new(O0O0O00000_key, O0O0O00000.MODE_CBC, iv=O0OO0O00OO).decrypt(O0OO0000O0[8:])
O0OO0000O0 = O00O0OOO0(O0OO0000O0, O0O0O00000.block_size)
O0OO0O0000 = O0OO0000O0[:16]
O0OO0000O0 = O0O00000O0.new(O0O00000O0_key, O0O00000O0.MODE_CBC, iv=O0OO0O0000).decrypt(O0OO0000O0[16:])
O0OO0000O0 = O00O0OOO0(O0OO0000O0, O0O00000O0.block_size)
exec(O0O0O00O0.decompress(O00O000O0.decompress(O0OO0000O0)))
"""
    # Save the encrypted Python file
    with open(output_path, 'w') as f:
        f.write(exec_code)
    print(f"Encoded file saved to {output_path}")
file_to_encode = './testrc.py'
output_encoded_file = 'sl.py'
for i in range(5):
	for i in range(20):
		encode_file('sl.py', 'sl.py')  	
	encode_python_file(file_to_encode, output_encoded_file)
	file_to_encode = './sl.py'
