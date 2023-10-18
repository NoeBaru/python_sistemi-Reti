"""
Author: Noemi Baruffolo
date: 18/10/2023
es. 012 pag.55 es.12
text:  Scrivi un programma in Python in cui applichi l' operatore di concatenazione delle stringhe alle seguenti due liste:
a = [0, 1, 2, 3] e b = [4, 5, 6, 7]. Stampa la lista finale.
"""
def print_list(lista):
    print("La lista e': ", end="")
    for elemento in lista:
        print(elemento, end=" ") #con end=" "non va a capo dopo ogni elemento, ma mette uno spazio e continua sulla stessa riga
    print("\n")

def main():
    a = [0, 1, 2, 3]
    b = [4, 5, 6, 7]

    a += b
    
    print_list(a)

if __name__=="__main__": 
    main()