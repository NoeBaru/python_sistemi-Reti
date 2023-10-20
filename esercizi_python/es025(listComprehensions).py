"""
Author: Noemi Baruffolo
date: 18/10/2023
es. 025 list comprehension
text:  lista con i primi quadrati perfetti, lista con i numeri interi fino al 10, lista di stringhe di cui stampo solo quelle con
l'iniziale c. Genero lista di voti a caso
"""

import random 

def print_list(lista):
    print("La lista e': ", end="")
    for elemento in lista:
        print(elemento, end=" ") #con end=" "non va a capo dopo ogni elemento, ma mette uno spazio e continua sulla stessa riga
    print("\n")

def main():
    quadrati = [i*i for i in range (1, 6)]
    print_list(quadrati)

    numeri_interi = [i for i in range(1, 11)]
    print_list(numeri_interi)

    stringhe = ["computer", "cellulare", "laptop"]

    stringhe_c = [parola for parola in stringhe if parola[0] == 'c'] #parola per parola in stringhe se parola di 0 (letera iniziale) è uguale a c
    print_list(stringhe_c)

    voti = [random.randint(2,10) for _ in range (0, 10)] #_ se ho una variabile che non serve a niente nel codice, così risparmio memoria
    print_list(voti)
    
    voti_insuff = [voto for voto in voti if voto < 6] #cicla il for di prima e controlla che il voto sia minore di 6 e lo stampa
    print_list(voti_insuff)

if __name__=="__main__": 
    main()