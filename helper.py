def bit_to_hex(s):
    return hex(int(s, 2))[2:]


def hex_to_bit(hex_msg):
    return bin(int(hex_msg, 16))[2:].zfill(len(hex_msg)*4)


def hex_to_string(hex_msg):
    return bytearray.fromhex(hex_msg).decode(encoding="Latin1")


def string_to_hex(msg):
    return ''.join('{:02x}'.format(x) for x in msg.encode('ascii'))


def hexprint(lst):
    for x in lst:
        print(hex(x))