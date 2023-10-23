"""
Author: Noemi Baruffolo
date: 21/10/2023
es. 027 pag.73 es.18
text: Utilizza le list comprehension per scrivere un programma che crei una lista con tutti i quadrati perfetti minori di 200 che siano
dispari. Stampa la lista.
"""

import math

def print_list(lista):
    print("I quadrati perfetti dispari fino a 200 sono: ", end="")
    for elemento in lista:
        print(elemento, end=" ") #con end=" "non va a capo dopo ogni elemento, ma mette uno spazio e continua sulla stessa riga
    print("\n")

def main():
    # quadrati = [i*i for i in range (0, 1000) if ((i*i) % 2 != 0) and (i**2 < 200)] #meno pulito, usa più memoria, meglio usare radice 
    quadrati = [i*i for i in range (0, int(math.sqrt(200)) + 1) if (i*i) % 2 != 0]
    print_list(quadrati)
    
if __name__=="__main__": 
    main()