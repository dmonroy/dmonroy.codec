from dmonroy.codec.base import BaseCodec

__author__ = 'Darwin Monroy'


N = '0123456789'
U = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
L = 'abcdefghijklmnopqrstuvwxyz'

class Base62Alphabet(object):
    NUL = N + U + L
    NLU = N + L + U
    LNU = L + N + U
    LUN = L + U + N
    ULN = U + L + N
    UNL = U + N + L


class Base62(BaseCodec):

    @staticmethod
    def encode(num, alphabet=Base62Alphabet.NLU):
        """
        Encodes the given phrase in base62.

        :param data: value to encode
        :param alphabet: alphabet to use in the encoding
        :return: base62 encoded string
        """

        if len(alphabet) != 62:
            raise Exception('Invalid alphabet')

        return BaseCodec.encode(num, alphabet)

    @staticmethod
    def decode(encoded, alphabet=Base62Alphabet.NLU):
        """
        Decodes a base62 encoded string.

        :param encoded: base62 encoded string
        :param alphabet: alphabet to use in the decoding
        :return: decoded value
        """

        if len(alphabet) != 62:
            raise Exception('Invalid alphabet')

        return BaseCodec.decode(encoded, alphabet)