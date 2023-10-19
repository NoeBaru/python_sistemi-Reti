"""
Author: Noemi Baruffolo
date: 18/10/2023
es. 005 pag.55 es.5
text: Scrivi un programma in Python che, assegnata una parola a una variabile stringa, stampi tutta la parola tranne le lettere
iniziali e finali della parola.
"""
def main():
    stringa = "ciao"
    print(f"{stringa[1:-1]}")
if __name__=="__main__": 
    main()