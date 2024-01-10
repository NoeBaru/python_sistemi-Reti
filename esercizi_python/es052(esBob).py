import turtle
import csv
import random

def move_turtle(t, direction):
    if direction == 1:
        t.setheading(90)  #nord
    elif direction == 2:
        t.setheading(270)  #sud
    elif direction == 3:
        t.setheading(0)  #est
    elif direction == 4:
        t.setheading(180)  #ovest
    t.forward(10)

def main():
    """
    Author: Noemi Baruffolo
    date: 9/01/2024
    es. Bob
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
    screen.setup(width=600, height=600)

    coordinates = [(0, 0)]  #coordinate iniziali
    old = set()
    old.add((0, 0))
    
    for _ in range(60):
        direction = random.randint(1, 4)  #direzione scelta casualmente
        move_turtle(t, direction)
        x, y = t.pos()
        if (x, y) in old:
            print(f"Coordinate già visitate: ({x}, {y})")
        old.add((x, y))
        coordinates.append((x, y))

    t.hideturtle()
    screen.update()

    with open('bobCoordinate.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['X', 'Y'])
        csv_writer.writerows(coordinates)

    turtle.done()

if __name__ == '__main__':
    main()