"""
Author: Noemi Baruffolo
date: //
es. 
text: la turtle deve andare dove vuole l'utente (nord, sud, est o ovest) di 100px
"""

import turtle

def nord():
    gradi = 90
    return gradi

def sud():
    gradi = 270
    return gradi

def ovest():
    gradi = 180
    return gradi

def est():
    gradi = 0
    return gradi

def main():
    dizionario = {"N": nord, "S": sud, "O": ovest, "E": est}
    
    while (True):
        if direzione in dizionario:
            direzione = input("Inserisci N per nord, S per sud, O per ovest ed E per est: ")
    
            window = turtle.Screen() #creazione schermo
            arrow = turtle.Turtle() #creazione turtle (cursore)
            angolo = dizionario[direzione]()
            lung = 100
            arrow.setheading(angolo)
            arrow.forward(lung)
        else:
            print("Errore!")
    window.mainloop() #per tenere aperta la finestra
    
if __name__ == '__main__':
    main()