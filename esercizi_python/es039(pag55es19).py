"""
Author: Noemi Baruffolo
date: 11/11/2023
es. 39 pag55 es19
text: Scrivi un programma in Python che permetta all'utente di inserire due numeri qualsiasi.
Crea un dizionario in cui salvi la media aritmetica e la media geometrica dei due numeri. Stampa il dizionario
"""

def calcMediaAritmetica(n1, n2):
    return (n1 + n2) / 2

def calcMediaGeometrica(n1, n2):
    return (n1 * n2) ** 0.5

def main():
    n1 = float(input("Inserisci il primo numero: "))
    n2 = float(input("Inserisci il secondo numero: "))
    
    mediaAritmetica = calcMediaAritmetica(n1, n2)
    mediaGeometrica = calcMediaGeometrica(n1, n2)
    
    ris = {"media aritmetica": mediaAritmetica, "media geometrica": mediaGeometrica}
    
    print("Dizionario:", ris)
if __name__ == '__main__':
    main()