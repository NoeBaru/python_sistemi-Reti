"""
Author: Noemi Baruffolo
date: 21/10/2023
es. 026 pag.73 es.17
text: Utilizza le list comprehension per scrivere un programma che crei una lista con tutte le potenze di due minori o uguali a un
valore inserito dall'utente. Stampa la lista.
"""

import math

def print_list(lista):
    print("La lista e': ", end="")
    for elemento in lista:
        print(elemento, end=" ") #con end=" "non va a capo dopo ogni elemento, ma mette uno spazio e continua sulla stessa riga
    print("\n")

def main():
    numero = int(input("Inserisci un numero: "))
    esponente = int(math.log2(numero))
    potenze = [2**i for i in range(esponente + 1)]
    print_list(potenze)

if __name__=="__main__": 
    main()