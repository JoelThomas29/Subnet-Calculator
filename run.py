""" Executes the application """

from Validating_IP_and_SubnetMask import *
import Calculating_Hosts_and_Subnet as calculate

# Getting IP and Subnet Mask and validating
ip = ip_address()
mask = subnet_mask()

# Forwarding the values to get the calculated results
inputs = [ip, mask]
calculate.hosts_and_subnet(inputs)

