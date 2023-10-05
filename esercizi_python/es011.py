"""
Author: Noemi Baruffolo
date: 3/10/2023
es. 010
text: fare i poligioni, ciascuno con colori diversi tutti nella stessa schermata
"""

import turtle

lati = int(input("Inserisci il numero di lati: "))
lung  = int(input("Inserisci la lunghezza dei lati: "))

window = turtle.Screen() #creazione schermo
arrow = turtle.Turtle() #creazione turtle (cursore)

for i in range (0, lati): #len da la lunghezza della lista
    arrow.forward(360/lati)
    arrow.left(lung) # va a sinistra

window.mainloop() #per tenere aperta la finestra