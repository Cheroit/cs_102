import pytest

from src.lab2.rsa import generate_keypair, encrypt, decrypt


@pytest.mark.parametrize('p, q, message', [
    (263, 269, 'hello123'),
    (229, 269, 'hello123asdfsafd'),
    (199, 271, 'dhsakjfhewlif')
])
def test_cases(p, q, message):
    public, private = generate_keypair(p, q)
    encrypted_msg = encrypt(private, message)
    answer = decrypt(public, encrypted_msg)
    assert message == answer
