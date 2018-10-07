from Crypto import Random
from Crypto.PublicKey import RSA

def RSA_Key_Pairs_Generator(key_bits):
    random_generator = Random.new().read
    rsa_keys= RSA.generate(key_bits,random_generator)
    private_pem=rsa_keys.exportKey('PEM')
    public_pem=rsa_keys.publickey().exportKey('PEM')

    return public_pem,private_pem

#print RSA_Key_Pairs_Generator()
