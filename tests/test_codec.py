__author__ = 'Darwin Monroy'

from dmonroy.codec import Base62, Base64
import base64


def test_base62():

    string = 'Testing Base62'

    enc = Base62.encode(string)
    dec = Base62.decode(enc)

    assert string == dec


def test_base64():

    string = 'Testing Base64'
    enc = Base64.encode(string)
    dec = Base64.decode(enc)

    assert string == dec

    for i in range(1, 10000):
        a = base64.b64encode(b'%s' % i)
        b = Base64.encode(i)
        assert a == b, u'For value "%s", %s != %s' % (i, a, b)
