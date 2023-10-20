"""
Author: Noemi Baruffolo
date: 18/10/2023
es. 010 pag.55 es.10
text: Scrivi un programma in Python nel quale assegni alla variabile lista_voti una lista con tutti i tuoi voti (almeno 6 voti).
Sfrutta l' indicizzazione per:
- stampare la lista senza il primo e l' ultimo voto;
- sostituire il quarto voto con un 10;
- stampare i primi 3 voti della lista.
"""

def print_list(lista):
    print("La lista e': ", end="")
    for elemento in lista:
        print(elemento, end=" ") #con end=" "non va a capo dopo ogni elemento, ma mette uno spazio e continua sulla stessa riga
    print("\n")

def main():
    lista_voti = []
    cont = 0

    while True:
        voto = int(input("Inserisci un voto (-1 per interrompere): "))
        if (voto < 0 and cont >= 6):
            break
        lista_voti.append(voto)
        cont += 1

    print("Lista senza il primo e l'ultimo voto: ")
    print_list(lista_voti[1:-1])

    lista_voti[3] = 10

    print("Primi 3 voti della lista: ")
    print_list(lista_voti[:3])

if __name__=="__main__": 
    main()