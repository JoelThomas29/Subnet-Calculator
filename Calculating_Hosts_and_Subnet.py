""" Calculates the following :
1. total hosts
2. wildcard mask
3. total subnet
    >  network address
	>  first host address
	>  last host address
	>  broadcast address """

def binary_to_decimal(value):
    list_binary = []
    for bit in range(0, 32, 8):
        temp = value[bit:bit+8]
        list_binary.append(temp)
    list_decimal = []
    for item in list_binary:
        list_decimal.append(str(int(item, 2)))

    return '.'.join(list_decimal)

def hosts_and_subnet(inputs):
    # Converting inputs to binary
    binaries_appended = []
    for entry in inputs:
        binary_inputs = []
        temp = entry.split('.')
        for item in temp:
            a = bin(int(item)).lstrip('0b').zfill(8)
            binary_inputs.append(a)
        binaries_appended.append(''.join(binary_inputs))
    ## binaries_appended[0] = ip in binary   and     binaries_appended[1] = subnet mask in binary

    # Counting host and network bits
    host_bits = binaries_appended[1].count('0') # print value at the end
    network_bits = 32 - host_bits
    total_hosts = abs(((2 ** host_bits) - 2))  # print value at the end

    # Wildcard Mask
    wildcard_initial = []
    for item in inputs[1].split('.'):
        temp = 255 - int(item)
        wildcard_initial.append(temp)

    wildcard_binary_initial = []
    for item in wildcard_initial:
        wildcard_binary_initial.append((bin(item)).lstrip('0b').zfill(8))
    wildcard_binary = ''.join(wildcard_binary_initial)

    # Network and Broadcast Address
    network_address_binary = binaries_appended[0][:network_bits] + '0' * int(host_bits)
    first_ip_binary = binaries_appended[0][:network_bits] + '0' * int(host_bits-1) + '1'
    last_ip_binary = binaries_appended[0][:network_bits] + '1' * int(host_bits-1) + '0'
    broadcast_binary = binaries_appended[0][:network_bits]+'1' * int(host_bits)

    # Getting the above results converted to decimal
    WILDCARD_MASK = binary_to_decimal(wildcard_binary)
    NETWORK_ADDRESS = binary_to_decimal(network_address_binary)
    FIRST_IP = binary_to_decimal(first_ip_binary)
    LAST_IP = binary_to_decimal(last_ip_binary)
    BROADCAST_ADDRESS = binary_to_decimal(broadcast_binary)

    return [host_bits, total_hosts, NETWORK_ADDRESS, FIRST_IP, LAST_IP, BROADCAST_ADDRESS, WILDCARD_MASK]
