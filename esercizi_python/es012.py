"""
Author: Noemi Baruffolo
date: 3/10/2023
es. 012
text: chiedere in input i numero di lati e disegnare una stella con quel numero di punte 
"""

import turtle

lati = int(input("Inserisci il numero di lati dispari: "))
lung  = int(input("Inserisci la lunghezza dei lati: "))

window = turtle.Screen() #creazione schermo
arrow = turtle.Turtle() #creazione turtle (cursore)

angolo = 180 - 180/lati

for i in range (0, lati): #len da la lunghezza della lista
    arrow.forward(lung)
    arrow.right(angolo)

window.mainloop() #per tenere aperta la finestra