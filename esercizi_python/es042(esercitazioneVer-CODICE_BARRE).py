"""
Author: Noemi Baruffolo
date: 13/11/2023
es. 042 "codiceBarre"
text: Un codice a barre è definito da una sequenza di barre nere oppure bianche secondo questi requisiti:
le barre nere corrispondono a un'1 e le barre bianche corrispondono a uno 0;
le barre sono disegnate su sfondo bianco;
una barra nera è rappresentata mediante una linea nera spessa 4 pixel e lunga 100 pixel;
una barra bianca è rappresentata mediante una linea bianca spessa 4 pixel e lunga 100 pixel;
barre adiacenti sono separate tra loro da uno spessore di un pixel;
un codice a barre è composto in totale da 64 barre.
Il codice a barre è utilizzato per codificare stringhe alfanumeriche di 8 caratteri.
Ogni carattere della stringa alfanumerica è convertito nel suo codice ASCII (vedi funzione ord()) e successivamente nella sua rappresentazione binaria, quindi nel complesso 8 caratteri corrispondono a 64 bit totali. Non devono essere presenti caratteri che hanno codice ASCII maggiore di 255.
Crea un programma in linguaggio Python 3 nel quale:
sia presente una classe Barcode che implementi il codice a barre sopra descritto;
la classe abbia un metodo che disegni il codice a barre a partire dalla stringa alfanumerica di 8 caratteri, utilizzando il modulo turtle;
sia presente una funzione main() che testi la classe.
"""

def main():
    pass #non fa niente, così non da errori nel codice
if __name__ == '__main__':
    main()