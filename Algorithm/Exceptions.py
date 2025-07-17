class CVARError(Exception):
    """Base class for CVAR-related exceptions."""
    pass

class InvalidHexInputError(CVARError):
    """Raised when input hex string is invalid."""
    def __init__(self, message="Hex string must contain an even number of characters and valid hex digits."):
        super().__init__(message)


class EncryptionError(CVARError):
    """Raised when encryption fails."""
    def __init__(self, message="Failed to encrypt CVAR string."):
        super().__init__(message)


class DecryptionError(CVARError):
    """Raised when decryption fails."""
    def __init__(self, message="Failed to decrypt CVAR string."):
        super().__init__(message)
