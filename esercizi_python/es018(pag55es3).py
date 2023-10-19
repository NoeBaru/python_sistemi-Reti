"""
Author: Noemi Baruffolo
date: 18/10/2023
es. 003 pag.55 es.3
text: Scrivi un programma in Python in cui:

- inizializzi due variabili, prima e seconda, con due numeri interi diversi a tua scelta;
- stampi i valori delle variabili usando una sola f-string;
- scambi i valori tra le due variabili;
- stampi i nuovi valori delle variabili usando una sola f-string.
"""
def main():
    prima, seconda = 1, 2
    print(f"Primo: {prima} e secondo: {seconda}")
    
    prima, seconda = seconda, prima
    print(f"Primo: {prima} e secondo: {seconda}")

if __name__=="__main__": 
    main()