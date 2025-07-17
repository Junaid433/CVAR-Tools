from .Exceptions import EncryptionError

def Encrypt_CVAR(plain_text: str, key: int = 0x79) -> str:
    try:
        if not plain_text.strip():
            raise EncryptionError("Input cannot be empty")
        return ''.join(f"{ord(c) ^ key:02x}" for c in plain_text)
    except Exception as e:
        raise EncryptionError(str(e))
