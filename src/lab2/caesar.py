def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""

    ALPHABET_LENGTH = 26

    for ch in plaintext:

        if ch.islower():
            ciphered_ch = chr(ord('a') + (ord(ch) - ord('a') + shift) % ALPHABET_LENGTH)

        elif ch.isupper():
            ciphered_ch = chr(ord('A') + (ord(ch) - ord('A') + shift) % ALPHABET_LENGTH)

        else:
            ciphered_ch = ch

        ciphertext += ciphered_ch

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    ALPHABET_LENGTH = 26

    for ch in ciphertext:

        if ch.islower():
            decrypted_ch = chr(ord('a') + (ord(ch) - ord('a') - shift) % ALPHABET_LENGTH)

        elif ch.isupper():
            decrypted_ch = chr(ord('A') + (ord(ch) - ord('A') - shift) % ALPHABET_LENGTH)

        else:
            decrypted_ch = ch

        plaintext += decrypted_ch

    return plaintext