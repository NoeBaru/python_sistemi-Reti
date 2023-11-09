"""
Author: Noemi Baruffolo
date: 07/11/2023
es. 034
text: chiedere all'utente che operazione fare, chiedere due numeri e fare l'operazione
"""
def somma(n1, n2):
    return n1 + n2

def prodotto(n1, n2):
    return n1 * n2

def differenza(n1, n2):
    return n1 - n2

def divisione(n1, n2):
    return n1 / n2

def main():    
    dizionario = {"+": somma, "*": prodotto, "-": differenza, "/": divisione}
    operazione = input("Inserisci + per somma, * per prodotto, - per differenza e / per divisione: ")
    if operazione in dizionario:
        n1 = float(input("Inserisci il primo numero: "))
        n2 = float(input("Inserisci il secondo numero: "))
        
        print(dizionario[operazione](n1, n2)) #l'elemento del dizionario è una funzione, quindi possiamo richiamarla come tale
    else:
        print("Errore!")
    
if __name__ == '__main__':
    main()