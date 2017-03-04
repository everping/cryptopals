# Convert hex to base64
def hex_to_base64(str):
    return str.decode('hex').encode('base64')