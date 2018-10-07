import generator,signature
import storage

key_pairs=generator.RSA_Key_Pairs_Generator(2048)

base_info={
    'name':'SCU',
    'public_key':key_pairs[0],
    'signature_algorithm':'RSA',
}

self_signature = signature.Self_Signature(str(base_info),sig_key=key_pairs[1])

usr_info = base_info
usr_info['self_signature'] = self_signature

writelist = usr_info.values()
storage.writeInfo(writelist)

def Transfer():
    return usr_info