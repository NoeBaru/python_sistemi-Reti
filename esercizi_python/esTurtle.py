import turtle #esempio di un modulo built-in (nativo: già dentro Python. Non native devi scaricarleda internet)
#turtle, nome storico, perche' apre una finestra grafica con la tartaruga (cursore) che permette di disegnare. Un tempo di chiamava logo questo linguaggio
finestra = turtle.Screen()
alice = turtle.Turtle() #creazione turtle (cursore)
alice.forward(100) #100 pixel
alice.left(30) #va a sinistra
alice.forward(50) #inclinazione di gradi

finestra.mainloop() #per tenere aperta la finestra