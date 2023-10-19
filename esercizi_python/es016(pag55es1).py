"""
Author: Noemi Baruffolo
date: 18/10/2023
es. 001 pag.55 es.1
text: Scrivi un programma in Python in cui inizializzi 4 variabili con un intero, una stringa, un floating point e un booleano.
Stampa i valori delle variabili e i loro tipi (con la funzione type()).
"""
def main():
    intero = 2
    stringa = "ciao"
    reale = 2.5
    booleano = True

    print(f"numero intero: {intero} {type(intero)} stringa: {stringa} {type(stringa)} numero reale: {reale} {type(reale)} booleano: {booleano} {type(booleano)}")
if __name__=="__main__": 
    main()