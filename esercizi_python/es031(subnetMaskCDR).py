"""
Author: Noemi Baruffolo
date: 30/10/2023
es. 031 subnetMaskCDR
text: chiedere un numero n in CDR <= 31 con subnet decinmale puntata
"""

def main():
    n = int(input("inserisci una subnet mask in notazione CDR: "))
    subnet = ("1"*n + "0"*(32-n))
    group1 = subnet[0:8]
    group2 = subnet[8:16]
    group3 = subnet[16:24]
    group4 = subnet[24:32]
    group1 = int(group1, 2)
    group2 = int(group2, 2)
    group3 = int(group3, 2)
    group4 = int(group4, 2) #int(stringa.2) per convertire la stringa in binario
    ip = print(f"{group1}.{group2}.{group3}.{group4}")

if __name__ == "__main__":
    main()