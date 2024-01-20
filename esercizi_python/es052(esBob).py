import turtle
import random

class Punto(): #modo per fare una struttura perché classe senza metodo
    def __init__(self, x, y): #costruttore
        self.x = x
        self.y = y

def move_turtle(t, direction):
    if direction == 0:
        t.setheading(90)  #nord
    elif direction == 1:
        t.setheading(270)  #sud
    elif direction == 2:
        t.setheading(0)  #est
    elif direction == 3:
        t.setheading(180)  #ovest
    t.forward(10)

def main():
    """
    Author: Noemi Baruffolo
    date: 9/01/2024
    es. 52 Bob
    text: Il nostro amico Bob dopo alcune commissioni in giro per la città di Flatland deve rientrare a casa.
          Purtroppo Bob soffre di momentanee perdite di memoria! Questa volta la sua amnesia dura ben 60 minuti
          e durante questi 60 minuti Bob adotta la seguente strategia per tentare di rientrare a casa. Ogni
          minuto decide a caso tra:
          1. procedere 10 m verso Nord
          2. procedere 10 m verso Sud
          3. procedere 10 m verso Est
          4. procedere 10 m verso Ovest
          Simula l'intero percorso compiuto da Bob, supponendo che il punto di partenza abbia coordinate (0,0) e
          salvalo all'interno di un dizionario opportunamente strutturato. Disegna il percorso compiuto da Bob
          dentro una schermata di pygame oppure turtle, decidi tu quale libreria usare.
          Infine salva il percorso di Bob dentro un file .csv opportunamente strutturato.
          BONUS: ogni volta in cui Bob passa in un punto della città di Flatland in cui è già passato, stampa a schermo le coordinate
          del punto.
    """
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width = 600, height = 600)    
    percorso = {0: Punto(0,0)}
    old = set()
    
    for tempo in range(0, 60):
        #simulare movimenti casuali
        #disegnare percorso con turtle
        for _ in range(60):
            direction = random.randint(0, 3)  #direzione scelta casualmente
            move_turtle(t, direction)
            x, y = t.pos()
    
        #BONUS: controllo passaggio punto già visitato
            if (x, y) in old:
                print(f"Coordinate già visitate: ({percorso[minuto].x}, {percorso[minuto].y})")
        
        #scrittura sul file dle percorso
        #COLONNE: minuto, x, y
        with open("bobPercorso.csv", "w") as file:
            file.write("min, X, Y")
            #ciclo sul dizionario percorso
            for minuto in percorso:
                posX = percorso[minuto].x
                file.write(f"{minuto}, {x}, {y}")
    
if __name__ == '__main__':
    main()