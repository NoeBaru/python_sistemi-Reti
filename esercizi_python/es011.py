"""
Author: Noemi Baruffolo
date: 3/10/2023
es. 010
text: fare i poligioni, ciascuno con colori diversi tutti nella stessa schermata usando comandi come turtle.penup
"""

import turtle

numP = int(input("Inserisci il numero di poligoni: "))
lung = int(input("Inserisci la lunghezza del primo lato: "))
spazioVuoto = 70  # Spazio tra i poligoni
poligoniRiga = 3  # Numero di poligoni per ogni riga

window = turtle.Screen()
arrow = turtle.Turtle()
colori = ["red", "green", "blue", "orange", "purple", "yellow"]

x = -((numP - poligoniRiga) * (lung + (spazioVuoto * 2))) / 2
y = 0

for i in range(3, numP + 3):
    colore = colori[i % len(colori)]
    arrow.penup()
    arrow.goto(x, y)
    arrow.pendown()
    arrow.color(colore)
    arrow.begin_fill()
    for _ in range(i):
        arrow.forward(lung)
        arrow.left(360 / i)
    arrow.end_fill()
    x += lung + spazioVuoto

    if (i - 2) % poligoniRiga == 0:
        x = -((numP - poligoniRiga) * (lung + spazioVuoto)) / 2
        y -= 2 * lung

window.mainloop()