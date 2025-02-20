import base64

encoded_str = "uRzRpUeBeQvqorr3QfpniQ=="
decoded_bytes = base64.b64decode(encoded_str)
print(decoded_bytes)

hex_str = decoded_bytes.hex()
print(hex_str)