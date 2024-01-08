import random
from time import sleep

import pygame
from pathlib2 import Path

class CarRacing:
    def __init__(self):

        pygame.init()
        self.displayWidth = 800
        self.displayHeight = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None
        self.rootPath = str(Path(__file__).parent)

        self.initialize()

    def initialize(self):

        self.crashed = False
        
        #car
        self.carImg = pygame.image.load(self.rootPath + "/img/porsche.png")
        self.carXCoordinate = (self.displayWidth * 0.45)
        self.carYCoordinate = (self.displayHeight * 0.7)
        self.carWidth = 50

        #enemyCar
        self.enemyCar = pygame.image.load(self.rootPath + "/img/porscheYellow1.png")
        self.enemyCarStartX = random.randrange(310, 450)
        self.enemyCarStartY = -600
        self.enemyCarSpeed = 5
        self.enemyCarWidth = 50
        self.enemyCarHeight = 100

        #background
        self.bgImg = pygame.image.load(self.rootPath + "/img/street.png")
        self.bgX1 = (self.displayWidth / 2) - (360 / 2)
        self.bgX2 = (self.displayWidth / 2) - (360 / 2)
        self.bgY1 = 0
        self.bgY2 = -600
        self.bgSpeed = 3
        self.count = 0

    def car(self, carXCoordinate, carYCoordinate):
        self.gameDisplay.blit(self.carImg, (carXCoordinate, carYCoordinate))

    def racingWindow(self):
        self.gameDisplay = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        pygame.display.set_caption('Car Race')
        self.runCar()

    def runCar(self):

        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                #print(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.carXCoordinate -= 50
                        #print("CAR X COORDINATES: %s" % self.carXCoordinate)
                    if event.key == pygame.K_RIGHT:
                        self.carXCoordinate += 50
                        #print("CAR X COORDINATES: %s" % self.carXCoordinate)
                    #print("x: {x}, y: {y}".format(x=self.carXCoordinate, y=self.carYCoordinate))

            self.gameDisplay.fill(self.black)
            self.backgroundRoad()

            self.runEnemyCar(self.enemyCarStartX, self.enemyCarStartY)
            self.enemyCarStartY += self.enemyCarSpeed

            if self.enemyCarStartY > self.displayHeight:
                self.enemyCarStartY = 0 - self.enemyCarHeight
                self.enemyCarStartX = random.randrange(310, 450)

            self.car(self.carXCoordinate, self.carYCoordinate)
            self.highScore(self.count)
            self.count += 1
            if self.count % 100 == 0:
                self.enemyCarSpeed += 1
                self.bgSpeed += 1

            if self.carYCoordinate < self.enemyCarStartY + self.enemyCarHeight:
                if self.carXCoordinate > self.enemyCarStartX and self.carXCoordinate < self.enemyCarStartX + self.enemyCarWidth or self.carXCoordinate + self.carWidth > self.enemyCarStartX and self.carXCoordinate + self.carWidth < self.enemyCarStartX + self.enemyCarWidth:
                    self.crashed = True
                    self.displayMessage("Game Over !!!")

            if self.carXCoordinate < 310 or self.carXCoordinate > 460:
                self.crashed = True
                self.displayMessage("Game Over !!!")

            pygame.display.update()
            self.clock.tick(60)

    def displayMessage(self, msg):
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, (255, 0, 0))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        self.displayCredit()
        pygame.display.update()
        self.clock.tick(60)
        sleep(1)
        carRacing.initialize()
        carRacing.racingWindow()

    def backgroundRoad(self):
        self.gameDisplay.blit(self.bgImg, (self.bgX1, self.bgY1))
        self.gameDisplay.blit(self.bgImg, (self.bgX2, self.bgY2))

        self.bgY1 += self.bgSpeed
        self.bgY2 += self.bgSpeed

        if self.bgY1 >= self.displayHeight:
            self.bgY1 = -600

        if self.bgY2 >= self.displayHeight:
            self.bgY2 = -600

    def runEnemyCar(self, thingX, thingY):
        self.gameDisplay.blit(self.enemyCar, (thingX, thingY))

    def highScore(self, count):
        font = pygame.font.SysFont("lucidaconsole", 20)
        text = font.render("Score : " + str(count), True, (255, 255, 0))
        self.gameDisplay.blit(text, (0, 0))

    def displayCredit(self):
        font = pygame.font.SysFont("lucidaconsole", 50)  # Aumenta la dimensione del font per renderlo più visibile come titolo
        text = font.render("CAR RACE", True, (255, 255, 0))
        text_width, text_height = font.size("CAR RACE")  # Ottieni la larghezza e altezza del testo
        screen_width = self.displayWidth  # Larghezza dello schermo
        x_coordinate = (screen_width - text_width) / 2  # Calcola la coordinata x centrata
        y_coordinate = 50  # Sposta leggermente verso il basso per renderlo come titolo

        self.gameDisplay.blit(text, (x_coordinate, y_coordinate))

        # Aggiungi le altre informazioni come prima, se necessario
        font = pygame.font.SysFont("lucidaconsole", 14)
        text = font.render("Noemi Baruffolo", True, self.white)
        self.gameDisplay.blit(text, (600, 540))
        text = font.render("4^AROB", True, self.white)
        self.gameDisplay.blit(text, (600, 560))

if __name__ == '__main__':
    carRacing = CarRacing()
    carRacing.racingWindow()