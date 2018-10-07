from Crypto.Hash.MD5 import MD5Hash

def md5hash(data=None):
    hashInstance = MD5Hash()
    hashInstance.new(data=data)
    return hashInstance

#print md5hash('hfsjkadhfdjs')