__author__ = 'Darwin Monroy'

from binascii import hexlify, unhexlify


class BaseCodec(object):

    @staticmethod
    def encode(data, alphabet, bs=1, pc='='):
        """
        Encodes the given phrase using the alphabet.

        :param data: value to encode
        :param alphabet: alphabet to use in the encoding
        :return: encoded string
        """

        missing = 0
        p = ''
        data = '{0}'.format(data).encode()
        if bs > 1:
            missing = bs - (len(data) % bs)

            if missing == bs:
                missing = 0

            data += b'\x00' * missing
            p = pc * missing


        # Get the hexadecimal representation of the binary data
        hex_data = hexlify(data).decode('utf8')

        # And the integer representation of the hex_data
        data = int('0x0' + hex_data, 16)

        if data == 0:
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while data:
            rem = data % base
            data = data // base
            arr.append(alphabet[rem])
        arr.reverse()

        if bs == 1 or missing == 0:
            return ''.join(arr)

        return ''.join(arr[:-1* missing] + [p])

    @staticmethod
    def decode(string, alphabet, pc='='):
        """
        Decodes the encoded string using the given alphabet.

        :param encoded: encoded string
        :param alphabet: alphabet to use in the decoding
        :param pc: padding char
        :return: decoded value
        """
        base = len(alphabet)
        strlen = len(string)
        num = 0
        pad = 0
        if pc in string:
            pad = len(string) - string.index(pc)

        if pad > 0:
            string = string[:-1*pad]

        idx = 0
        for char in string:
            power = (strlen - (idx + 1))
            num += alphabet.index(char) * (base ** power)
            idx += 1

        # Convert the integer to bytes
        h = '%x' % num
        if len(h) % 2:
            h = '0' + h
        res = unhexlify(h.encode('utf8'))

        if pad:
            res = res[:-1*pad]

        return res.decode('utf8')
