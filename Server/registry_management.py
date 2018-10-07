import random,generator,signature,serverStorage
import pandas as pd

def isInRe(client):
    name_column = serverStorage.readRegistry()
    if client['name'] in name_column:
        return True
    return False

def registry(client):
    reg_info = client

    CA_key_pairs = generator.RSA_Key_Pairs_Generator(2048)

    reg_info['pub_key_ca']=CA_key_pairs[0]
    reg_info['pri_key_ca']=CA_key_pairs[1]

    sequence_num = random.randint(0,10000)
    reg_info['sequence_num']=sequence_num

    serverStorage.writeRegistry(reg_info.values())

    CA = {
        'user_info':client,
        'sequence_number': sequence_num,
        'CA_name':'SCU_simple_CA_system',
        'CA_algotithm':'RSA',
        'expire_date':'2020.12.31',
    }
    CA_signature = signature.Self_Signature(str(CA),CA_key_pairs[1])
    CA['CA_signature']=CA_signature

    return CA

def deleteClient(client):
    regInfo = pd.read_csv('registry.csv')
    deletedInfo = regInfo.ix[ regInfo[0] == client['name'] ]
    deletedInfo.to_csv('registry.csv', index=False)

def manage_main(ver_rst , client):
    if ver_rst == True:
        if isInRe(client):
            return 'OK'
        else:
            return registry(client)
    else:
        if isInRe(client):
            deleteClient(client)
            return 'Wrong'
        else:
            return 'Wrong'