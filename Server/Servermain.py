import Server.Extraction_and_Verification as EX_VE
import hash,registry_management
import Client.CA_Registry

info = Client.CA_Registry.Transfer()

[C_base_info,C_self_signature,C_public_key] = EX_VE.extract(info)

C_info_md5hash = hash.md5hash(str(C_base_info))

verification_result = EX_VE.verify(C_self_signature,C_public_key,C_info_md5hash)

result = registry_management.manage_main(verification_result,info)

print result