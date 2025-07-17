from Algorithm.Encryptor import Encrypt_CVAR
from Algorithm.Decryptor import Decrypt_CVAR

plain = "r.UserQualitySetting=0"
encrypted = Encrypt_CVAR(plain)
print("Encrypted:", encrypted)

decrypted = Decrypt_CVAR(encrypted)
print("Decrypted:", decrypted)