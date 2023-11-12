"""
Author: Noemi Baruffolo
date: 11/11/2023
es. 37 pag55 es15
text: Scrivi un programma in Python che permetta all'utente di inserire il suo nome (tramite input()) e che stampi il nome in cui tutti
i caratteri tranne il primo sono sostituiti da un *.
"""

def main():
    nome = input("Inserisci il nome: ")
    nomeNuovo = nome[0] + '*' * (len(nome) - 1)
        
    print("Nome modificato:", nomeNuovo)
    
if __name__ == '__main__':
    main()