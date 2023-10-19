def bin2dec(stringa):
    dec = 0
    for k, carattere in enumerate(stringa[::-1]): 
        if carattere == "1": 
            dec += 2 ** k
    return dec

def dec2bin(numero, nbit):
    numeroBin = bin(numero)[2:]
    return "0" * (nbit - len(numeroBin)) + numeroBin

def IP_dec2bin(stringa):
    pezzi, finale = stringa.split("."), ""
    for cella in pezzi:
        finale += str(dec2bin(int(cella), 8))
    return finale

def IP_bin2dec(stringa):
    finale = ""
    for num in range(0, 32, 8):
        finale += str(bin2dec(stringa[num:num + 8])) + "."
    return finale[:-1]

def controllo_ip_subnet(ip, subnet):
    return IP_dec2bin(ip)[subnet:] == "0" * (32 - subnet)

def calcolo_IP_broadcast(ip, subnet):
    return IP_dec2bin(ip)[:subnet] + "1" * len(IP_dec2bin(ip)[subnet:])

def primo_IP(ip):
    return ip[:-1] + str((int(ip[-1]) + 1))

def ultimo_IP(ip, subnet):
    broadcast = calcolo_IP_broadcast(ip, subnet)
    return broadcast[:-1] + str((int(broadcast[-1]) - 1))

def main():
    IP_rete, subnet_mask, subnet = "0.0.0.0", 33, ""
    while controllo_ip_subnet(IP_rete, subnet_mask) or subnet_mask < 0 or subnet_mask > 32:
        IP_rete, subnet = input("Inserisci l'IP di rete: "), input("Inserisci una subnet mask (/n | n | xxx.xxx.xxx.xxx): ")
        if subnet.__len__() > 3:
            subnet_mask = IP_dec2bin(subnet).count("1")
        elif subnet[0] == "/":
            subnet_mask = int(subnet[1:])
        else:
            subnet_mask = int(subnet)
    
    print(f"IP inserito: {IP_rete} /{subnet_mask}\nSubnet mask: {IP_bin2dec('1' * subnet_mask + '0' * (32 - subnet_mask))}\n"
          f"Host disponibili: {2 ** (32 - subnet_mask) - 2}\nIP di broadcast: {IP_bin2dec(calcolo_IP_broadcast(IP_rete, subnet_mask))}\n"
          f"Primo IP disponibile: {primo_IP(IP_rete)}\nUltimo indirizzo IP disponibile: {IP_bin2dec(ultimo_IP(IP_rete, subnet_mask))}")

if __name__ == "__main__":
    main()
