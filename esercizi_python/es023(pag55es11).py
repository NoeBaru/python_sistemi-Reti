"""
Author: Noemi Baruffolo
date: 18/10/2023
es. 011 pag.55 es.11
text: Scrivi un programma in Python in cui inizializzi la lista x = [0, 1, 2, 3, 5, 6, 7, 8] e poi che:
- crei due nuove liste contenenti ciascuna una delle due metà della lista;
- aggiungi il valore 5 alla lista contenente la prima metà.
"""

def print_list(lista):
    for elemento in lista:
        print(elemento, end=" ") #con end=" "non va a capo dopo ogni elemento, ma mette uno spazio e continua sulla stessa riga
    print("\n")

def main():
    x = [0, 1, 2, 3, 5, 6, 7, 8]

    meta = len(x) // 2 #divisione intera, non risultato esatto della divisione

    sxMeta = x[:meta]
    dxMeta = x[meta:]

    sxMeta.append(dxMeta[0])

    print("La prima meta' e': ", end="")
    print_list(sxMeta)
    print("La seconda meta' e': ", end="")
    print_list(dxMeta)

if __name__=="__main__": 
    main()