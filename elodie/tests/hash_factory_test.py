from . import helper
from elodie.hash_factory import HashFactory
from elodie.hash_factory import SHA256
from elodie.hash_factory import XX64
from elodie.hash_factory import XX32

def test_sha256():
    
    hash = HashFactory(SHA256)
    src = helper.get_file('plain.jpg')
    checksum = hash.digest(src)

    assert checksum == 'd5eb755569ddbc8a664712d2d7d6e0fa1ddfcdb378475e4a6758dc38d5ea9a16', 'Checksum for plain.jpg did not match'

def test_xxh64():
    
    hash = HashFactory(XX64)
    src = helper.get_file('plain.jpg')
    checksum = hash.digest(src)

    assert checksum == '44f126656d9f5400', 'Checksum for plain.jpg did not match'

def test_xxh32():
    
    hash = HashFactory(XX32)
    src = helper.get_file('plain.jpg')
    checksum = hash.digest(src)

    assert checksum == '1b6539d6', 'Checksum for plain.jpg did not match'