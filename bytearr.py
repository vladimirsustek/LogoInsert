

a = bytearray([0x20, 0x30, 0x30])


def _printByteArray(arr):
    converted = ''
    for b in arr:
        converted += str(hex(b)) + ' '
    return converted


print(_printByteArray(a))