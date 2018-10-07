import base64

from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def extract(usr_info):
    base_info ={}
    base_info['name'] = usr_info['name']
    base_info['public_key'] = usr_info['public_key']
    base_info['signature_algorithm'] = usr_info['signature_algorithm']

    self_signature = usr_info['self_signature']
    public_key = base_info['public_key']

    return base_info,self_signature,public_key

def verify(self_sig , pub_key , hash_value):
    rsa_key = RSA.importKey(pub_key)
    verifier = PKCS1_v1_5.new(rsa_key)
    reslut = verifier.verify(hash_value,self_sig)
    return reslut
