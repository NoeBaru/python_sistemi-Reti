"""
Author: Noemi Baruffolo
date: 3/10/2023
es. 010
text: chiedere all'utente un numero n e con Turtle disegnare n lati per creare un poligono regolare
"""

import turtle

lati = int(input("Inserisci il numero di lati: "))
lung  = int(input("Inserisci la lunghezza dei lati: "))

window = turtle.Screen() #creazione schermo
arrow = turtle.Turtle() #creazione turtle (cursore)

arrow.speed(3) #velocita'

arrow.begin_fill()
for i in range (0, lati): #len da la lunghezza della lista
    arrow.forward(lung)
    arrow.left(360/lati) # va a sinistra
    arrow.color('purple')
arrow.end_fill()

window.mainloop() #per tenere aperta la finestra