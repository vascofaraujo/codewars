def round_to_interval(number):
    if number > 255:
        return 255
    if number < 0:
        return 0
    return number


def convert_to_hex(value):
    if len(hex(value)) == 3:
        return hex(value)[0]+hex(value)[2]
    return hex(value)[2:]

def rgb(r,g,b):
    r,g,b = round_to_interval(r), round_to_interval(g), round_to_interval(b)

    string = convert_to_hex(r) + convert_to_hex(g) + convert_to_hex(b)

    return string.upper()
              
