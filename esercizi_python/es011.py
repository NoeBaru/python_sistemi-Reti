"""
Author: Noemi Baruffolo
date: 3/10/2023
es. 011
text: fare i poligioni, ciascuno con colori diversi tutti nella stessa schermata usando comandi come turtle.penup
"""

import turtle

def disegnaPoligono(arrow, num, lato):
    gradi = 360 / num
    arrow.begin_fill() #inizia il riempimento della freccia
    for i in range(0, num):
        arrow.forward(lato)
        arrow.left(gradi)
    arrow.end_fill #la freccia termina il riempimento


def posizionaArrow(arrow, num, lato, x, y):
    arrow.penup() # si muove la freccia senza disegnare
    if(num % 3 == 0):
        x = -100
        y = y + lato * 4
    else:
        x = x + lato * 4
    arrow.goto(x, y)
    arrow.pendown()
    return x, y

def main():
    x = 0
    y = -100

    min = 3
    max = 12

    lato = int(input("Inserisci la lato altezza del primo lato: "))

    window = turtle.Screen()
    arrow = turtle.Turtle()

    #arrow = arrow.shape("turtle") per fare la forma della tartaruga
    arrow.color("violet") #imposto il colore

    arrow.speed("slow") #velocità della freccia


    for num in range(min, max):
        x, y = posizionaArrow(arrow, num, lato)
        disegnaPoligono(arrow, num, lato)

    window.mainloop()

if __name__=="__main__": 
    main()