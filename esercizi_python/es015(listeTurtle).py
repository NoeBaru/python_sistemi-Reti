"""
Author: Noemi Baruffolo
date: 3/10/2023
es. 013 turtle  e liste
text: chiedere in input il comando da dare (F, R, L)
forward 100^ F
right 90^ R
left 90^ L
"""

import turtle

def print_list(lista):
    print("La lista e': ", end="")
    for elemento in lista:
        print(elemento, end=" ") #con end=" "non va a capo dopo ogni elemento, ma mette uno spazio e continua sulla stessa riga
    print("\n")

def main():
    #per prendere in input la lista
    lista = []
    possibleCommand = ['F', 'R', 'L']
    command = 'F' #per far partire il while
    window = turtle.Screen() #creazione schermo
    arrow = turtle.Turtle() #creazione turtle (cursore)
    angolo = 90
    lung = 100


    while command in possibleCommand:
        command = input("Inserisci un comando (F: forward, R: right, L: left o -1 per interrompere): ")
    #in python tutto e' un oggetto (mantra di python)
        if command in possibleCommand:
            lista.append(command) #aggiunge num alla lista
    for command in lista:
        if lista == 'F':
            arrow.forward(lung)
        if lista == 'R':
            arrow.right(angolo)
        if lista == 'L':
            arrow.left(angolo)
    window.mainloop() #per tenere aperta la finestra

if __name__=="__main__": 
    main()