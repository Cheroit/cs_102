import random
import string
import unittest

import pytest

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

@pytest.mark.parametrize('plaintext, keyword, ciphertext', [
    ("PYTHON", "A", "PYTHON"),
    ("python","a","python" ),
    ("python","abcdef","pzvkss"),
    ("","a",""),
    ("123","a","123")
])

def test_cases(plaintext,keyword,ciphertext):
    answer = encrypt_vigenere(plaintext, keyword)
    assert ciphertext == answer


@pytest.mark.parametrize('ciphertext, keyword, plaintext', [
    ("PYTHON", "A", "PYTHON"),
    ("python","a","python" ),
    ("pzvkss","abcdef","python"),
    ("","a",""),
    ("123","a","123")
])

def test_cases(ciphertext,keyword,plaintext):
    answer = decrypt_vigenere(ciphertext, keyword)
    assert plaintext == answer

def test_randomized():
    kwlen = random.randint(4, 24)
    keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
    plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
    ciphertext = encrypt_vigenere(plaintext, keyword)
    assert plaintext==decrypt_vigenere(ciphertext,keyword)
#    assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))

