import pytest

from src.lab2.caesar import encrypt_caesar,decrypt_caesar


@pytest.mark.parametrize('plain_text, shift, ciphertext', [
    ("HELLO", 3, "KHOOR"),
    ("PYTHON",3,"SBWKRQ"),
    ("HELLO",4,"LIPPS"),
    ("PYTHON",4,"TCXLSR"),
    ("ABC123",3,"DEF123"),
    ("123",3,"123"),
    ("",3,"")
])

def test_cases(plain_text,shift, ciphertext):
    answer = encrypt_caesar(plain_text, shift)
    assert ciphertext == answer


@pytest.mark.parametrize('ciphertext, shift, plain_text', [
    ("KHOOR", 3, "HELLO"),
    ("SBWKRQ",3,"PYTHON"),
    ("LIPPS",4,"HELLO"),
    ("TCXLSR",4,"PYTHON"),
    ("DEF123",3,"ABC123"),
    ("",3,"")
])

def test_cases(ciphertext,shift, plain_text):
    answer = decrypt_caesar(ciphertext, shift)
    assert plain_text == answer