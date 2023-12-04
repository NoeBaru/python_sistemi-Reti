import turtle

def main():
    """
    Author: Noemi Baruffolo
    date: 27/11/2023
    es. 047 es2 vecchia ver
    text: Crea un programma Python che disegni una griglia 4 x 4 a maglie quadrate di lato 10, come quella a fianco, mediante il modulo
    turtle. Utilizza il minor numero di righe di codice.
    """
    
    pen = turtle.Turtle()
    
    #costanti in maiuscolo
    LATO = 10  #lung del lato di ogni quad
    SPAZIO = 10  #spazio tra i quad
    NQ = 4 #num quad
    GRADI = 90

    pen.penup()
    for cont in range(NQ):
        for i in range(NQ):
            pen.goto(i * SPAZIO, -cont * SPAZIO)
            pen.pendown()
            for _ in range(NQ):
                pen.forward(LATO)
                pen.right(GRADI)
            pen.penup()
    turtle.mainloop() #per tenere aperta la finestra

if __name__ == '__main__':
    main()