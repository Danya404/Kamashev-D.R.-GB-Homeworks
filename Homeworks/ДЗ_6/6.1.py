with open('nginx_logs.txt') as f:
    for line in f:
        splitted = line.split()
        print((splitted[0], splitted[5].replace('"', ''), splitted[6]))
