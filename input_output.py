""" This program takes inputs of IP address and subnet mask """
import sys

def ip_address():
    # Take input until right IP is obtained
    ip_input = input("Enter IP address : ")
    return ip_input

def subnet_mask():
    # Take input until right mask is obtained
    mask_input = input("Enter Subnet Mask : ")
    return mask_input

def validation_output(ip_flag, mask_flag):
    if (ip_flag == True) and (mask_flag == True):
        print("Invalid IP and Subnet Mask entered")
        sys.exit()
    elif (ip_flag == True) and (mask_flag == False):
        print("IP address invalid")
        sys.exit()
    elif (ip_flag == False) and (mask_flag == True):
        print("Subnet Mask invalid")
        sys.exit()
    else:
        print("Inputs Validated!!")

def final_output(outputs):
    print("***** Results\n"
      "Host bits : {}\n"
      "Total hosts : {}\n"
      "Network Address : {}\n"
      "First IP address : {}\n"
      "Last IP address : {}\n"
      "Broadcast Address : {}\n"
      "Wildcard Mask : {}".format(outputs[0], outputs[1], outputs[2], outputs[3], outputs[4], outputs[5], outputs[6]))


