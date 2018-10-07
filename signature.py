import base64

import hash

from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


def Self_Signature(message=None,sig_key=None):
    md5hash = hash.md5hash(message)
    rsakey = RSA.importKey(sig_key)
    signer = PKCS1_v1_5.new(rsakey)
    signature = signer.sign(md5hash)

    # rsakey = RSA.importKey(rsa_private_key)
    # cipher = Cipher_pkcs1_v1_5.new(rsakey)
    # random_generator = Random.new().read
    # text = cipher.decrypt(base64.b64decode(cipher_text), None)
    # print text.decode('utf8')
    return signature