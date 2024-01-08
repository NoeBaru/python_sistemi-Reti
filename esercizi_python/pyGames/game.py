import random  #importa il modulo random per generare numeri casuali
from time import sleep  #importa sleep per aggiungere un ritardo al gioco

import pygame  #importa il modulo Pygame per creare il gioco
from pathlib2 import Path  #importa Path da pathlib2 per ottenere il percorso del file

class CarRacing:
    def __init__(self):
        pygame.init()  #inizializza Pygame
        self.displayWidth = 800  #larghezza della finestra di gioco
        self.displayHeight = 600  #altezza della finestra di gioco
        self.black = (0, 0, 0)  #colore nero in formato RGB
        self.white = (255, 255, 255)  #colore bianco in formato RGB
        self.clock = pygame.time.Clock()  #clock di Pygame per impostare la velocità del gioco
        self.gameDisplay = None  #variabile per la finestra di gioco
        self.rootPath = str(Path(__file__).parent)  #ottiene il percorso della directory del file Python

        self.initialize()  #chiama il metodo initialize al momento dell'inizializzazione dell'oggetto

    def initialize(self):
        self.crashed = False  #flag per indicare se il gioco è finito o meno

        #car
        self.carImg = pygame.image.load(self.rootPath + "/img/porsche.png")  #carica l'immagine della macchina del giocatore
        self.carXCoordinate = (self.displayWidth * 0.45)  #coordinata x iniziale della macchina del giocatore
        self.carYCoordinate = (self.displayHeight * 0.7)  #coordinata y iniziale della macchina del giocatore
        self.carWidth = 50  #larghezza della macchina del giocatore

        #enemy Car
        self.enemyCar = pygame.image.load(self.rootPath + "/img/porscheYellow1.png")  #carica l'immagine della macchina nemica
        self.enemyCarStartX = random.randrange(310, 450)  #posizione iniziale x casuale della macchina nemica
        self.enemyCarStartY = -600  #posizione iniziale y della macchina nemica fuori dallo schermo
        self.enemyCarSpeed = 5  #velocità della macchina nemica
        self.enemyCarWidth = 50  #larghezza della macchina nemica
        self.enemyCarHeight = 100  #altezza della macchina nemica

        #background
        self.bgImg = pygame.image.load(self.rootPath + "/img/street.png")  #carica l'immagine dello sfondo
        self.bgX1 = (self.displayWidth / 2) - (360 / 2)  #posizione iniziale x del primo sfondo
        self.bgX2 = (self.displayWidth / 2) - (360 / 2)  #posizione iniziale x del secondo sfondo
        self.bgY1 = 0  #posizione iniziale y del primo sfondo
        self.bgY2 = -600  #posizione iniziale y del secondo sfondo
        self.bgSpeed = 3  #velocità di scorrimento dello sfondo
        self.count = 0  #conteggio per il punteggio del giocatore

    #metodo per disegnare la macchina del giocatore sulla schermata di gioco
    def car(self, carXCoordinate, carYCoordinate):
        self.gameDisplay.blit(self.carImg, (carXCoordinate, carYCoordinate))

    #metodo per impostare la finestra di gioco
    def racingWindow(self):
        self.gameDisplay = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        pygame.display.set_caption('Car Race')  #imposta il titolo della finestra di gioco
        self.runCar()  #avvia la funzione principale del gioco

    #funzione principale del gioco
    def runCar(self):
        while not self.crashed:
            for event in pygame.event.get():  #itera sugli eventi in coda (es. tastiera, mouse, etc.)
                if event.type == pygame.QUIT:  #se l'evento è l'uscita dalla finestra
                    self.crashed = True  #imposta il "flag" a vero per terminare il gioco

                if event.type == pygame.KEYDOWN:  #se viene rilevata la pressione di un tasto
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a: #se premuto il tasto freccia sinistra o 'A', sposta la macchina del giocatore a sinistra
                        self.carXCoordinate -= 50
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: #se premuto il tasto freccia destra o 'D', sposta la macchina del giocatore a destra
                        self.carXCoordinate += 50

            self.gameDisplay.fill(self.black)  #riempie lo sfondo con il colore nero
            self.backgroundRoad()  #mostra lo sfondo

            pygame.display.update()  #aggiorna la schermata
            self.clock.tick(60)  #imposta il clock del gioco a 60 FPS

            self.runEnemyCar(self.enemyCarStartX, self.enemyCarStartY) #disegna la macchina nemica sulla schermata di gioco alle coordinate specificate
            self.enemyCarStartY += self.enemyCarSpeed #incrementa la coordinata y della macchina nemica per fare l'effetto di movimento di caduta dall'alto

            if self.enemyCarStartY > self.displayHeight: #verifica se la macchina nemica è scesa oltre la parte inferiore della schermata 
                self.enemyCarStartY = 0 - self.enemyCarHeight #reimposta la coordinata Y della macchina nemica in cima alla finestra di gioco
                self.enemyCarStartX = random.randrange(310, 450) #imposta casualmente la coordinata X della macchina nemica all'interno dell'intervallo specificato
            
            #incrementa il punteggio e con il suo aumentare incrementa la velocità delle macchine
            self.car(self.carXCoordinate, self.carYCoordinate) #disegna la macchina del giocatore nella posizione corrente determinata dalle coordinate 
            self.highScore(self.count) #aggiorna il punteggio mostrato a schermo con il valore attuale
            self.count += 1 #incrementa il contatore del punteggio
            if self.count % 100 == 0: #ogni volta che il punteggio raggiunge un multiplo di 100, aumenta la velocità della macchina nemica  e dello sfondo
                self.enemyCarSpeed += 1
                self.bgSpeed += 1
                
            #controlla le collisioni
            if self.carYCoordinate < self.enemyCarStartY + self.enemyCarHeight:
                if self.carXCoordinate > self.enemyCarStartX and self.carXCoordinate < self.enemyCarStartX + self.enemyCarWidth or self.carXCoordinate + self.carWidth > self.enemyCarStartX and self.carXCoordinate + self.carWidth < self.enemyCarStartX + self.enemyCarWidth:
                    self.crashed = True
                    self.displayMessage("Game Over !!!")

            if self.carXCoordinate < 310 or self.carXCoordinate > 460:
                self.crashed = True
                self.displayMessage("Game Over !!!")

            pygame.display.update() #aggiorna la schermata del gioco con le modifiche apportate
            self.clock.tick(60) #imposta il clock del gioco a 60 frame al secondo 
            
    #metodo per mostrare un messaggio e riavviare il gioco dopo un certo tempo
    def displayMessage(self, msg):
        font = pygame.font.SysFont("comicsansms", 72, True)  #imposta il font e la dimensione del testo
        text = font.render(msg, True, (255, 0, 0))  #crea il testo del messaggio in rosso
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))  #posiziona il testo al centro
        self.displayCredit()  #mostra i crediti di chi ha fatto iol gioco
        pygame.display.update()  #aggiorna la schermata
        self.clock.tick(60)  #imposta il clock del gioco a 60 FPS
        sleep(2)  #attendere due secondi prima di riavviare il gioco
        carRacing.initialize()  #reinizializza il gioco
        carRacing.racingWindow()  #avvia di nuovo la finestra di gioco

    #metodo per gestire il movimento dello sfondo
    def backgroundRoad(self):
        self.gameDisplay.blit(self.bgImg, (self.bgX1, self.bgY1))  #mostra lo sfondo
        self.gameDisplay.blit(self.bgImg, (self.bgX2, self.bgY2))  #mostra un altro pezzo dello sfondo

        self.bgY1 += self.bgSpeed  #muove lo sfondo verso il basso
        self.bgY2 += self.bgSpeed  #muove un altro pezzo dello sfondo verso il basso

        #se una macchina nemica scende e raggiunge il fondo della finestra, la riporta all'inizio
        if self.bgY1 >= self.displayHeight:
            self.bgY1 = -600
        if self.bgY2 >= self.displayHeight:
            self.bgY2 = -600

    #funzione per gestire il movimento della macchina nemica
    def runEnemyCar(self, thingX, thingY):
        self.gameDisplay.blit(self.enemyCar, (thingX, thingY))

    #funzione per gestire il punteggio
    def highScore(self, count):
        font = pygame.font.SysFont("lucidaconsole", 20) #imposta il font della scritta
        text = font.render("Score : " + str(count), True, (255, 255, 0)) #scrive in giallo
        self.gameDisplay.blit(text, (0, 0))

    #funzione per gestire la visualizzazione dei crediti
    def displayCredit(self):
        font = pygame.font.SysFont("lucidaconsole", 50)  #dimensione e font titolo
        text = font.render("CAR RACE", True, (255, 255, 0)) #colore giallo del titolo del gioco
        text_width, text_height = font.size("CAR RACE")  #per ottenere la larghezza e altezza del testo
        screen_width = self.displayWidth  #larghezza dello schermo
        x_coordinate = (screen_width - text_width) / 2  #calcola la coordinata x centrata
        y_coordinate = 50  #sposta leggermente verso il basso per renderlo come titolo

        self.gameDisplay.blit(text, (x_coordinate, y_coordinate))

        #autore e classe del videogioco
        font = pygame.font.SysFont("lucidaconsole", 14)
        text = font.render("Noemi Baruffolo", True, self.white)
        self.gameDisplay.blit(text, (600, 540))
        text = font.render("4^AROB", True, self.white)
        self.gameDisplay.blit(text, (600, 560))

if __name__ == '__main__':
    carRacing = CarRacing()
    carRacing.racingWindow()