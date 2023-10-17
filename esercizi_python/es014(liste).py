"""
Author: Noemi Baruffolo
date: 3/10/2023
es. 013
text: lista
"""

def print_list(lista):
    print("La lista e': ", end="")
    for elemento in lista:
        print(elemento, end=" ") #con end=" "non va a capo dopo ogni elemento, ma mette uno spazio e continua sulla stessa riga
    print("\n")

def main():
    l = [1, 2, 3, 4, 'c', 3.14, "python"] #possono contenere tipi di variabili diversi, i vettori no
    r = [10, 11, 12]
    #print(lista) stampa tutta la lista
    #print(lista[-1]) stampa l'ultima cella della lista
    print_list(l[::-1])
    #print_list(l(l + r)) concatena le liste
    #print_list(l(3 * r)) moltiplica la lista per 3

    #per prendere in input la lista
    lista = []
    num = 1 #per far partire il while
    while num > 0:
        num = int(input("Inserisci un numero (-1 per interrompere): "))
    #in python tutto e' un oggetto (mantra di python)
        if num > 0:
            lista.append(num) #aggiunge num alla lista
    
    print_list(lista)

if __name__=="__main__": 
    main()