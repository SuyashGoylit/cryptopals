from base64 import b64encode

def hex_to_base_64(hex_str: str) -> str:
    base_64 = b64encode(bytes.fromhex(hex_str)).decode()
    return base_64

if __name__ == '__main__':
    hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print(hex_to_base_64(hex_str))  # Output: 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'