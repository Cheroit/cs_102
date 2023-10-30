def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    ALPHABET_LENGTH = 26

    len_keyword = len(keyword)
    len_plaintext = len(plaintext)

    if len_keyword < len_plaintext:
        n_repeat = (len_plaintext // len_keyword) + 1
        keyword = keyword * n_repeat
        keyword = keyword[:len_plaintext]

    for ch1, ch2 in zip(plaintext, keyword):
        # for i in range(len(plaintext)):
        #     ch1 = plaintext[i]
        #     ch2 = keyword[i]

        if ch1.islower() and ch2.islower():
            ciphered_ch = chr(ord('a') + (ord(ch1) - ord('a') + ord(ch2) - ord('a')) % ALPHABET_LENGTH)

        elif ch1.isupper() and ch2.islower():
            ciphered_ch = chr(ord('A') + (ord(ch1) - ord('A') + ord(ch2) - ord('a')) % ALPHABET_LENGTH)

        elif ch1.islower() and ch2.isupper():
            ciphered_ch = chr(ord('a') + (ord(ch1) - ord('a') + ord(ch2) - ord('A')) % ALPHABET_LENGTH)

        elif ch1.isupper() and ch2.isupper():
            ciphered_ch = chr(ord('A') + (ord(ch1) - ord('A') + ord(ch2) - ord('A')) % ALPHABET_LENGTH)

        else:
            ciphered_ch = ch1

        ciphertext += ciphered_ch

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    ALPHABET_LENGTH = 26

    len_keyword = len(keyword)
    len_ciphertext = len(ciphertext)

    if len_keyword < len_ciphertext:
        n_repeat = (len_ciphertext // len_keyword) + 1
        keyword = keyword * n_repeat
        keyword = keyword[:len_ciphertext]

    for ch1, ch2 in zip(ciphertext, keyword):

        if ch1.islower() and ch2.islower():
            ciphered_ch = chr(ord('a') + (ord(ch1) - ord('a') - ord(ch2) + ord('a')) % ALPHABET_LENGTH)

        elif ch1.islower() and ch2.isupper():
            ciphered_ch = chr(ord('a') + (ord(ch1) - ord('a') - ord(ch2) + ord('A')) % ALPHABET_LENGTH)

        elif ch1.isupper() and ch2.islower():
            ciphered_ch = chr(ord('A') + (ord(ch1) - ord('A') - ord(ch2) + ord('a')) % ALPHABET_LENGTH)

        elif ch1.isupper() and ch2.isupper():
            ciphered_ch = chr(ord('A') + (ord(ch1) - ord('A') - ord(ch2) + ord('A')) % ALPHABET_LENGTH)

        else:
            ciphered_ch = ch1

        plaintext += ciphered_ch

    return plaintext