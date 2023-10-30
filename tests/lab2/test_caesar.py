import pytest

from src.lab2.caesar import encrypt_caesar,decrypt_caesar


@pytest.mark.parametrize('plain_text, shift, ciphertext', [
    ("HELLO", 3, "KHOOR"),
    ("PYTHON",3,"SBWKRQ"),
    ("HELLO",4,"LIPPS"),
    ("PYTHON",4,"TCXLSR"),
    ("ABC123",3,"DEF123")
])

def test_cases(plain_text,shift, ciphertext):
    answer = encrypt_caesar(plain_text, shift)
    assert ciphertext == answer