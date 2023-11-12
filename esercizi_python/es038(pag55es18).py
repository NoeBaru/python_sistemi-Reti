"""
Author: Noemi Baruffolo
date: 11/11/2023
es. 38 pag55 es18
text: Scrivi un programma in Python che permetta all'utente di inserire due numeri. Crea una lista contenente: i la somma dei quadrati
dei due numeri; i Il quadrato della somma dei numeri; i la differenza tra i quadrati dei due numeri; i il quadrato della differenza tra
i numeri. Stampa la lista ottenuta. 
"""

def sommaQuadrati(n1, n2):
    return n1**2 + n2**2

def quadratoSomma(n1, n2):
    return (n1 + n2)**2

def diffQuadrati(n1, n2):
    return abs(n1**2 - n2**2) #abs per valore assoluto

def quadratoDiff(n1, n2):
    return (n1 - n2)**2

def main():
    n1 = float(input("Inserisci il primo numero: "))
    n2 = float(input("Inserisci il secondo numero: "))
    
    ris = [sommaQuadrati(n1, n2),quadratoSomma(n1, n2),diffQuadrati(n1, n2),quadratoDiff(n1, n2)]
    
    print("Lista:", ris)

if __name__ == '__main__':
    main()