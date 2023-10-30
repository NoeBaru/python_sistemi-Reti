"""
Author: Noemi Baruffolo
date: 25/10/2023
es. 030 subnetting
text: text:  scrivi un programma che dato un ip (es. 192.168.1.0)  trasformi i gruppi in binario e al contrario
"""

def completa8bit(strbin):
    b = strbin[2:]
    lung = len(b)
    "0"*(8 - lung) + b

def main():
    address = "192.168.0.1"
    groups = address.split(".")

    groups = [int(group) for group in groups]  #converte la lista in interi
    print(groups)
    print(completa8bit(groups[0]))
    groups_bin = [completa8bit(strbin) for strbin in groups]
    print(groups_bin)
    print(".".join(groups_bin)) #.join è il contrario di split

    """
    for group in groups:
        numero_binario = bin(group)[2:]  #rimuove i primi due caratteri (0b)

        print(f"Il numero binario corrispondente a {group} è: {numero_binario}")
    """

if __name__ == "__main__":
    main()
