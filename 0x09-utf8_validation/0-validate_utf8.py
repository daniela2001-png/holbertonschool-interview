#!/usr/bin/python3
def validUTF8(data):
    """
    """
    try:
        int.from_bytes(data, byteorder='big')
    except Exception as e:
        return False
    return True
