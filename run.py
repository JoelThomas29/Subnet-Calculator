""" Executes the application """

import input_output
import Calculating_Hosts_and_Subnet as backend_logic
import inputs_validation as validate

#                ********************************      STEP : 1     **************************************
# Getting IP and Subnet Mask . . .  (INPUTS)
## IP
ip_return = input_output.ip_address()
ip = ip_return.rstrip(" ") # Removing next blank spaces if any
ip_digits = ip.split(".") # splitting each address to verify is usability

## Subnet Mask
mask_return = input_output.subnet_mask()
mask = mask_return.rstrip(" ") # Removing next blank spaces if any
mask_digits = mask.split(".") # splitting each address to verify is usability


#                ********************************      STEP : 2     **************************************
# Sending IP input to be validated . . . (VALIDATION LOGIC)
ip_flag = False # A variable to determine if ip entered was usable
check1 = validate.ip_validate(ip_digits)
if check1 == True:
    IP = ip
else:
    ip_flag = True

# Sending Subnet Mask input to be validated . . . (VALIDATION LOGIC)
mask_flag = False # A variable to determine if subnet mask entered was usable
check2 = validate.subnet_validate(mask_digits)
if check2 == True:
    MASK = mask
else:
    mask_flag = True

# Validation result . . . (VALIDATION OUTPUT)
# Exit program if any of the validation fails
input_output.validation_output(ip_flag, mask_flag)


#                ********************************      STEP : 3     **************************************
# Forwarding the values to get the calculated results . . . (CORE LOGIC)
inputs = [IP, MASK]
outputs = backend_logic.hosts_and_subnet(inputs)

# Printing results . . . (FINAL OUTPUT)
input_output.final_output(outputs)


