import base64


def hex_to_base64(hex_string):
    """
    Convert a hex string to base64
    """
    return base64.b64encode(bytes.fromhex(hex_string)).decode("utf-8")

