""" This program validates IP and Subnet mask entered by the user """

def ip_validate(digits):
    """ Checking with the criteria if the address is of the right format """

    if ( (len(digits) == 4) and (1 <= int(digits[0]) <= 223) and (int(digits[0]) != 127) and (int(digits[0]) != 169 or int(digits[1]) != 254) and (0 <= int(digits[1]) <= 255) and (0 <= int(digits[2]) <= 255) and (0 <= int(digits[3]) <= 255)):
        return True
    else:
        return False

def subnet_validate(digits):
    """  Checking with the criteria if mask is of the right format """

    # Additional validation required
    def test(digits):
        if (int(digits[0]) < 255) and (int(digits[1]) == int(digits[2]) == int(digits[3]) == 0):
            return True
        elif (int(digits[0]) == 255 and int(digits[1]) < 255) and (int(digits[2]) == int(digits[3]) == 0):
            return True
        elif (int(digits[0]) == int(digits[1]) == 255 and int(digits[2]) < 255) and (int(digits[3]) == 0):
            return True
        elif (int(digits[0]) == int(digits[1]) == int(digits[2]) == 255) and (int(digits[3]) >= 0):
            return True
        else:
            return False

    # Defining valid masks
    valid_mask = [255, 254, 252, 248, 240, 224, 192, 128, 0]

    if ( (len(digits) == 4) and (int(digits[0]) >= 128) and (int(digits[0]) in valid_mask) and (int(digits[1]) in valid_mask) and (int(digits[2]) in valid_mask) and (int(digits[3]) in valid_mask) and (int(digits[0]) >= int(digits[1]) >= int(digits[2]) >= int(digits[3])) and (test(digits) == True)):
        return True
    else:
        return False
