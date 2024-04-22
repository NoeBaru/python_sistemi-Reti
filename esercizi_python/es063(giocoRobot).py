import sys
import pygame
from pygame.locals import *

def calc_pav():
    with open("pavimento.csv", "r") as f:
        mat = [[int(c) for c in riga.split(", ")] for riga in f.readlines()]
    return mat

def sceltaNodo(nonVisitati, label):
    n_nodi = len(matrice)
    nonVisitati = set([i for i in range (0, n_nodi)])
    label = {i:sys.maxsize for i in range (0, n_nodi)}
    label[nodo_sorgente] = 0
    print(label)
    minlabel = 0
    for nodo in nonVisitati:
        labelNodo = label[nodo]
        if labelNodo < minlabel:
            minlabel = labelNodo
            minNodo = nodo
    return minNodo

def dijkstra(nodo_sorgente, matrice):
    n_nodi = len(matrice)
    nodi_non_visitati = len(set(matrice))
    nonVisitati = set([i for i in range (0, n_nodi)])
    label = {i:sys.maxsize for i in range (0, n_nodi)}
    label[nodo_sorgente] = 0
    print(label)
    while len(nonVisitati) != 0:
        nodoCorrente = sceltaNodo(nonVisitati, label)
        nonVisitati.remove(nodoCorrente)
        for nodoVicino in enumerate(matrice[nodoCorrente]):
            if peso > 0:
                nuovalabel = label[nodoCorrente] + peso
                if nuovalabel < label[nodoVicino]:
                    predecessore[nodoVicino] = nodoCorrente
                    label[nodoVicino] = nuovalabel
    return label, predecessore

def main():
    """
    Author: Noemi Baruffolo
    date: 20/03/2024
    es. 063 gioco robot
    text: robot che si muove con le frecce, controllando se è libero o ha otsacoli, partendo dal dizionario es062

    nella libreria sys c'è sys.maxsize otteniamo il valore numerico più grande che può ottenere il proprio sistema
    """

    lato_x = 100
    lato_y = 100
    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    matrice = [[-1 for _ in range(n_x)] for _ in range(n_y)]
    k = 1
    #inserisci il dizionario dei predecessori cosi da poter vedere i nodi succesivi in dijkstra


    #SETUP per schermo, immagini e font
    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x , n_y * lato_y))
    muro = pygame.image.load("muro.jpeg")
    strada = pygame.image.load("strada.jpeg")
    robot = pygame.image.load("robot.png").convert_alpha()
    font = pygame.font.SysFont("Verdana", 18) 
    
    for riga in pavimento:
        for casella in riga:
            surf1 = pygame.Surface((lato_x, lato_y))
            text = font.render(f"{k}", True, (0,0,0))
            if casella == 1:
                surf1.blit(muro, (0, 0))
                screen.blit(surf1, (lato_x-100, lato_y-100))  
            elif casella == 0:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x-20, lato_y-80))  
                screen.blit(surf1, (lato_x-100, lato_y-100))  
                screen.blit(text, text_pos)
                k += 1
            elif casella == 3:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x-20, lato_y-80))  
                screen.blit(surf1, (lato_x-100, lato_y-100))
                screen.blit(robot, (lato_x-100, lato_y-100)) 
                screen.blit(text, text_pos)
                k += 1
            
            pygame.display.flip()
            lato_x += 100
            
        lato_x = 100
        lato_y += 100

        #screen.blit(robot, (0, 0))
    k = 1
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0:
                matrice[indice_riga][indice_colonna] = k
                k += 1
    
    diz = {}
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            adiacenze = []
            if casella == 0:
                if indice_riga > 0:
                    if matrice[indice_riga-1][indice_colonna] != -1:
                        adiacenze.append(matrice[indice_riga-1][indice_colonna])
                if indice_colonna > 0:
                    if matrice[indice_riga][indice_colonna-1] != -1:
                        adiacenze.append(matrice[indice_riga][indice_colonna-1])
                if indice_riga < n_y-1:
                    if matrice[indice_riga + 1][indice_colonna] != -1:
                        adiacenze.append(matrice[indice_riga+1][indice_colonna])
                if indice_colonna < n_x - 1:
                    if matrice[indice_riga][indice_colonna + 1] != -1:
                        adiacenze.append(matrice[indice_riga][indice_colonna+1])
                    diz[matrice[indice_riga][indice_colonna]] = adiacenze
    
    print(diz)

    #pygame.quit()
    #exit()
    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
    pygame.quit()

if __name__ == "__main__":
    main()