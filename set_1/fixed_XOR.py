import binascii
from Crypto.Util.strxor import strxor


def xor_strings(str1, str2):
    """
    Conver hex strings to bianry, XOR them, and convert back to hex
    """

    str1 = binascii.unhexlify(str1)
    str2 = binascii.unhexlify(str2)
    return binascii.hexlify(strxor(str1, str2)).decode()
