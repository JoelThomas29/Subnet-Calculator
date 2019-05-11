""" This program check the validity of the IP address and subnet mask """

import time

def loading_feature():
    for i in range(3):
        print(".", end=' ', flush=True)
        time.sleep(0.5)
    print("")

def ip_address():
    # Take input until right IP is obtained
    while True:
        loading_feature()
        ip_input = input("Enter IP address : ")

        ip = ip_input.rstrip(" ") # Removing next blank spaces if any
        digits = ip.split(".") # splitting each address to verify is usability

        loading_feature()
        # Checking with the criteria if the address is of the right format
        if ( (len(digits) == 4) and (1 <= int(digits[0]) <= 223) and (int(digits[0]) != 127) and (int(digits[0]) != 169 or int(digits[1]) != 254) and (0 <= int(digits[1]) <= 255) and (0 <= int(digits[2]) <= 255) and (0 <= int(digits[3]) <= 255)):
            print("Validated\n")
            break
        else:
            print("Invalid IP address")
            continue
    return ip

def subnet_mask():
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

    # Take input until right mask is obtained
    while True:
        loading_feature()
        mask_input = input("Enter Subnet Mask : ")

        # Defining valid masks
        valid_mask = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        mask = mask_input.rstrip(" ") # Removing next blank spaces if any
        digits = mask.split(".") # splitting each address to verify is usability

        loading_feature()
        # Checking with the criteria if the mask is of the right format
        if ( (len(digits) == 4) and (int(digits[0]) >= 128) and (int(digits[0]) in valid_mask) and (int(digits[1]) in valid_mask) and (int(digits[2]) in valid_mask) and (int(digits[3]) in valid_mask) and (int(digits[0]) >= int(digits[1]) >= int(digits[2]) >= int(digits[3])) and (test(digits) == True)):
            print("Validated\n")
            break
        else:
            print("Invalid subnet mask")
            continue
    return mask

