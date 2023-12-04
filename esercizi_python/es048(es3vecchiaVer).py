def main():
    """
    Author: Noemi Baruffolo
    date: 4/12/2023
    es. 048 es3 vecchia ver
    text: Data la lista ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    crea un file “mask.txt” in cui salvi le subnet mask associate a ciascun indirizzo IP.
    """
    ip_addresses = ["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    #file = open("mask.txt", "w")
    
    with open("mask.txt", "w") as file: #così si crea l'oggetto e lo tiene aperto per tutto il codice che contiene(identato)
    
        for ip_address in ip_addresses:
            ip, subnet_mask = ip_address.split("/")  #split ritorna una lista di stringhe
            subnet_mask_int = int(subnet_mask)
            subnet_mask_bin = '1' * subnet_mask_int + '0' * (32- subnet_mask_int)
            subnet_mask_bin = subnet_mask_bin[:8] + '.' + subnet_mask_bin[8:16] + '.' + subnet_mask_bin[16:24] + '.' + subnet_mask_bin[24:]
            print('.'.join([subnet_mask_bin[i:i+8] for i in range(0,32,8)]))
            file.write(f"{ip} - subnet Mask({subnet_mask}): {subnet_mask_bin}\n")
            #file.close()

if __name__ == '__main__':
    main()