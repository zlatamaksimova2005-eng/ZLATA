def decimal_to_hex():

    hex_dict = {i: hex(i) for i in range(16)}
    return hex_dict

if __name__ == '__main__':
    hex_dict = decimal_to_hex()
    print(hex_dict)
