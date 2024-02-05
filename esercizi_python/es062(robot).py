import csv
import pygame

def leggiFilCsv(nomeFile):
    matrice = []
    with open(nomeFile, 'r') as file:
        lettoreCsv = csv.reader(file)
        for riga in lettoreCsv:
            matrice.append([int(valore) for valore in riga])
    return matrice

def disegnaMat(matrice):
    righe = len(matrice)
    colonne = len(matrice[0])
    dimensioneCella = 170
    blackColor = (255, 255, 255)
    whiteColor = (0, 0, 0)

    pygame.init()
    finestra = pygame.display.set_mode((colonne * dimensioneCella, righe * dimensioneCella))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        finestra.fill((255, 255, 255)) #nero

        for riga in range(righe):
            for colonna in range(colonne):
                colore = whiteColor if matrice[riga][colonna] == 1 else blackColor #bianco, altrimenti nero
                pygame.draw.rect(finestra, colore, (colonna * dimensioneCella, riga * dimensioneCella, dimensioneCella, dimensioneCella))

        pygame.display.update()

def main():
    """
    Author: Noemi Baruffolo
    date: 05/02/2024
    es. 062 robot
    text: fare file csv contenente
    0, 0, 0, 1
    0, 1, 0, 0
    1, 0, 0, 1
    1, 0, 1, 1
    che deve essere aperto dal programma e deve creare una matrice.
    (facoltativo) una volta ottenuta la matrice, disegnarlo in pygame
    """
    nomeFile = 'es062.csv'
    matrice = leggiFilCsv(nomeFile)
    disegnaMat(matrice)

if __name__ == "__main__":
    main() 