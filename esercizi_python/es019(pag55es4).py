"""
Author: Noemi Baruffolo
date: 18/10/2023
es. 004 pag.55 es.4
text: Scrivi un programma in Python che, assegnata una parola a una variabile stringa, stampi le lettere iniziali e finali della parola.
"""
def main():
    stringa = "ciao"
    print(f"{stringa[0]} {stringa[-1]}")
if __name__=="__main__": 
    main()