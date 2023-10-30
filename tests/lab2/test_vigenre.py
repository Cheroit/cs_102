import pytest

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

@pytest.mark.parametrize('plaintext, keyword, ciphertext', [
    ("PYTHON", "A", "PYTHON"),
    ("python","a","python" ),
    ("python","abcdef","pzvkss")
])

def test_cases(plaintext,keyword,ciphertext):
    answer = encrypt_vigenere(plaintext, keyword)
    assert ciphertext == answer