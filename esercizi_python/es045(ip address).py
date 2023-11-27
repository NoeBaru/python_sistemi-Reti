"""
Author: Noemi Baruffolo
date: 23/11/2023
es. 045 IP address
text: Chiedere all'utente un indirizzo IPv4 e una subnet mask usando le classi:
- stampare se è privato o di loopBack
- se IP valido stampare tutti gli IP utilizzabili, altrimenti finisce il programma
"""

import ipaddress

def main():
    ipv4 = input("Inserisci un IPV4: ")
    subnet = input("Inserisci una subnet mask: ")
    
    ipv4pieno = ipv4 + subnet
    ip = ipaddress.IPv4Address(ipv4)
    
    if ip.is_private:
        print("E' privato")
    if ip.is_loopback:
        print("E' loopback")
    ipRete = ipaddress.IPv4Network(ipv4pieno, strict = False) #crea una rete a partire da un IP. False perché puoi dare un IP qualunque della rete e lui si calcola un IP 
    if ipv4pieno == str(ipRete):
        print(f"E' di rete perché l'indirizzo {ipv4pieno} coincide con {ipRete}")
    else:
        print(f"Non e' di rete perché l'indirizzo {ipv4pieno} non coincide con {ipRete}")
    print(f"indirizzo di rete: {ipRete}")
    hosts = list(ipRete.hosts())
    print(f"il primo IP utilizzabile e' {hosts[0]} e l'ultimo {hosts[-1]}")
if __name__ == '__main__':
    main()