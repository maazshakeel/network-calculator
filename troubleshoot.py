ip_address = '10.10.10.1'

last_octet = int(ip_address.split('.')[3]) + 1
array = ip_address.split('.')
array[3] = last_octet
print(array)
