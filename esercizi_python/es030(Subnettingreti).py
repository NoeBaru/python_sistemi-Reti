"""
Author: Noemi Baruffolo
date: 25/10/2023
es. 030 subnetting
text: text:  scrivi un programma che dato un ip (es. 192.168.1.0)  trasformi i gruppi in binario e al contrario
"""

def main():
    address = "192.168.0.1"
    groups = address.split(".")

    groups = [int(group) for group in groups]  # Converte la lista in interi

    for group in groups:
        numero_binario = bin(group)[2:]  # Rimuove i primi due caratteri

        print(f"Il numero binario corrispondente a {group} è: {numero_binario}")

if __name__ == "__main__":
    main()
