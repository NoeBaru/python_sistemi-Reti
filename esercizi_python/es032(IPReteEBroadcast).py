"""
Author: Noemi Baruffolo
date: 25/10/2023
es. 032 IPReteEBroadcast
text: Es: fare un programma che chieda all'utente un indirizzo IP e una subnet mask in notazione CIDR: calcolare IP di rete e IP di broadcast.
"""

def main():
    ip = input("Inserisci un indirizzo IP: ")
    n = int(input("Inserisci una subnet mask in notazione CIDR: "))
    
    groups = ip.split('.') #per dividere l'IP in gruppetti guardando i punti
    groups = [int(group) for group in groups]
    
    subnet = ('1' * n + '0' * (32 - n)) #per calcolare l'IP di reete
    network_groups = [str(groups[i] & int(subnet[i * 8:(i + 1) * 8], 2)) for i in range(4)]
    
    broadcast_groups = [str(groups[i] | (255 - int(subnet[i * 8:(i + 1) * 8], 2))) for i in range(4)] #per calcolare IP broadcast
    
    network_ip = '.'.join(network_groups) #.join fa il contrario di split
    broadcast_ip = '.'.join(broadcast_groups)
    
    print(f"Indirizzo IP di rete: {network_ip}")
    print(f"Indirizzo IP di broadcast: {broadcast_ip}")

if __name__ == '__main__':
    main()