"""
Author: Noemi Baruffolo
date: 25/10/2023
es. 033 rubrica
text: fare ciclo dove riempiamo il dizionario caricato da file e poi lo stampiamo
"""

def main():
    file = open("rubrica.txt", "r")
    righe = file.readlines()
    file.close()
    rubrica = {}

    for riga in righe:
        #restituisce i campi
        campi = riga.split(", ")

        #sostiuisco il carattere \n con uno a scelta
        numTell = int(campi[1].replace("\n", ""))
        nome = campi[0]

        #uso numTell come chiave
        rubrica[numTell] = nome
    print(rubrica)

if __name__ == "__main__":
    main()