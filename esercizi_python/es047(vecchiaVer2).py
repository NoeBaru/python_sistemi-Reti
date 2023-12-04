"""
Author: Noemi Baruffolo
date: 27/11/2023
es. 047 es2 vecchia ver
text: Crea un programma Python che disegni una griglia 4 x 4 a maglie quadrate di lato 10, come quella a fianco, mediante il modulo
turtle. Utilizza il minor numero di righe di codice.
"""

import turtle

def main():
    screen = turtle.Screen()
    pen = turtle.Turtle()

    lato = 10  #lung del lato di ogni quad
    spazio = 10  #spazio tra i quad

    pen.penup()
    for i in range(4):
        for j in range(4):
            pen.goto(j * spazio, -i * spazio)
            pen.pendown()
            for _ in range(4):
                pen.forward(lato)
                pen.right(90)
            pen.penup()
    turtle.mainloop() #per tenere aperta la finestra

if __name__ == '__main__':
    main()