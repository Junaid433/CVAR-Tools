from .Exceptions import InvalidHexInputError, DecryptionError

def Decrypt_CVAR(encrypted_hex: str, key: int = 0x79) -> str:
    try:
        if len(encrypted_hex) % 2 != 0:
            raise InvalidHexInputError()
        decrypted_chars = []
        for i in range(0, len(encrypted_hex), 2):
            hex_byte = encrypted_hex[i:i+2]
            try:
                byte = int(hex_byte, 16)
            except ValueError:
                raise InvalidHexInputError("Invalid hex characters found.")
            decrypted_byte = byte ^ key
            decrypted_chars.append(chr(decrypted_byte))
        return ''.join(decrypted_chars)
    except Exception as e:
        raise DecryptionError(str(e))
