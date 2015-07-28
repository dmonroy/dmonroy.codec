__author__ = 'Darwin Monroy'

from dmonroy.codec import Base62, Base64
import base64
import random


def test_simple_base62():

    string = 'Testing Base62'

    enc = Base62.encode(string)
    dec = Base62.decode(enc)

    assert string == dec


def test_large_base62():

    for i in range(1,100000):
        string = str(i)
        enc = Base62.encode(string)
        dec = Base62.decode(enc)

        assert string == dec

    start = 0
    for i in range(1, 1000):
        # a big random number
        rn = start + (i * random.randrange(1000, 99999999))

        string = 'IsRandom:%s' % rn
        enc = Base62.encode(string)
        dec = Base62.decode(enc)

        assert string == dec


def test_base64():

    string = 'Testing Base64'
    enc = Base64.encode(string)
    dec = Base64.decode(enc)

    assert string == dec


def test_large_base64():

    for i in range(1,100000):
        string = str(i)
        enc = Base64.encode(string)
        dec = Base64.decode(enc)

        assert string == dec

    start = 0
    for i in range(1, 1000):
        # a big random number
        rn = start + (i * random.randrange(1000, 99999999))

        string = 'IsRandom:%s' % rn
        enc = Base64.encode(string)
        dec = Base64.decode(enc)

        _enc = base64.b64encode(string)
        _dec = base64.b64decode(_enc)
        _dec2 = base64.b64decode(enc)

        assert enc == _enc
        assert string == dec
        assert string == _dec
        assert string == _dec2