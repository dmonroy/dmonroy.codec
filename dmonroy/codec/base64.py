from dmonroy.codec.base import BaseCodec

__author__ = 'Darwin Monroy'


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


class Base64(BaseCodec):
    """
    Base64 encoder/decoder implemented with dmonroy.codec.

    DISCLAIMER: This codec is not intended to be a replacement to the core
    `base64` module. This has been developed to make possible to test the encode
    and decode method using a well known binary-to-text encoding schema.
    """

    @staticmethod
    def encode(value):
        """
        Encodes the given value in base64.

        :param value: value to encode
        :param alphabet: alphabet to use in the encoding
        :return: base64 encoded string
        """

        return BaseCodec.encode(value, ALPHABET, bs=3)

    @staticmethod
    def decode(encoded):
        """
        Decodes a base64 encoded string.

        :param encoded: base64 encoded string
        :param alphabet: alphabet to use in the decoding
        :return: decoded value
        """

        return BaseCodec.decode(encoded, ALPHABET)
