import turtle

def disegnaQuad(lato, pen):
    pen.pendown()
    pen.forward(lato)
    pen.right(90)
    pen.forward(lato)
    pen.right(90)
    pen.forward(lato)
    pen.right(90)
    pen.forward(lato)
    pen.right(90)
    pen.penup()

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
    
    for i in range(NQ):
        for j in range(NQ):
            pen.goto(LATO * (j),  LATO * (i))
            disegnaQuad(LATO, pen)
            
            print(LATO*j, LATO*i)
            
    turtle.mainloop() #per tenere aperta la finestra

if __name__ == '__main__':
    main()