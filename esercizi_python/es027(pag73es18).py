"""
Author: Noemi Baruffolo
date: 21/10/2023
es. 027 pag.73 es.18
text: Utilizza le list comprehension per scrivere un programma che crei una lista con tutti i quadrati perfetti minori di 200 che siano
dispari. Stampa la lista.
"""

def print_list(lista):
    print("La lista e': ", end="")
    for elemento in lista:
        print(elemento, end=" ") #con end=" "non va a capo dopo ogni elemento, ma mette uno spazio e continua sulla stessa riga
    print("\n")

def main():
    quadrati = [i*i for i in range (1, 15) if (i*i) % 2 != 0]
    print_list(quadrati)
    
if __name__=="__main__": 
    main()