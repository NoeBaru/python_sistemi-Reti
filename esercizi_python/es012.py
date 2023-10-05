"""
Author: Noemi Baruffolo
date: 3/10/2023
es. 012
text: chiedere in input n e disegnare una stella a n punte 
"""

import turtle

lati = int(input("Inserisci il numero di lati: "))
lung  = int(input("Inserisci la lunghezza dei lati: "))

window = turtle.Screen() #creazione schermo
arrow = turtle.Turtle() #creazione turtle (cursore)

for i in range (0, lati): #len da la lunghezza della lista
    arrow.forward(lung)
    arrow.right(180 - 180/lati)

window.mainloop() #per tenere aperta la finestra