with open('nginx_logs.txt') as f:
    IP_addresses = []
    for line in f:
        splitted = line.split()
        IP_address = splitted[0]
        IP_addresses.append(IP_address)
    unique_addresses = set(IP_addresses)
    spammer = None
    counter = 0
    for unique_IP in unique_addresses:
        if IP_addresses.count(unique_IP) > counter:
            counter = IP_addresses.count(unique_IP)
            spammer = unique_IP
    print('IP спамера: ', spammer)


