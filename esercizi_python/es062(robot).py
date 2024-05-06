'''un  robot può spostarsi su un pavimento con ostacoli; bisogna definire una mappa (in un file csv)
fare matrice numerata con celle libere, poi dizionario di adiacenze(a partire da matrice numerata)'''

import pygame
from pygame.locals import *
from sys import maxsize
import random
import csv

class Grafo:
    def __init__():
        pass

'''funzione che restituisce il nodo con label minore'''
def sceltaNodo(non_visitati, label):
    minLabel = maxsize
    minNodo = None
    for nodo in non_visitati:
        labelNodo = label[nodo]
        if labelNodo <= minLabel:
            minLabel = labelNodo
            minNodo = nodo
    return minNodo

def dijkstra(nodo_sorgente, matrice):
    n_nodi = len(matrice)
    non_visitati = set([n for n in range(0,n_nodi)]) #all'inizio nessun nodo è visitato
    predecessore = {}
    label = {i:maxsize for i in range(0,n_nodi)}
    label[nodo_sorgente] = 0
    #print(label)
    nodoCorrente = sceltaNodo(non_visitati, label)
    while len(non_visitati)>0:
        nodoCorrente = sceltaNodo(non_visitati, label)
        non_visitati.remove(nodoCorrente)
        for nodo_vicino, peso in enumerate(matrice[nodoCorrente]):
            if peso > 0:
                nuova_label = label[nodoCorrente] + peso
                if nuova_label < label[nodo_vicino]:
                    predecessore[nodo_vicino] = nodoCorrente
                    label[nodo_vicino] = nuova_label
    return label, predecessore
    
    

def calc_pav():
    with open("maze.csv", "r") as f:
        mat = [[int(c) for c in riga.split(",")] for riga in f.readlines()]
    return mat

def get_input(dir_x, dir_y, casella_player, diz, indice_x, indice_y, matrice, robot, screen, strada):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dir_x = 1
        dir_y = 0
        muovi(casella_player, dir_x, dir_y, diz, indice_x, indice_y, matrice, robot, screen, strada)
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dir_x = -1
        dir_y = 0
        muovi(casella_player, dir_x, dir_y, diz, indice_x, indice_y, matrice, robot, screen, strada)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dir_x = 0
        dir_y = -1
        muovi(casella_player, dir_x, dir_y, diz, indice_x, indice_y, matrice, robot, screen, strada)
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dir_x = 0
        dir_y = 1
        muovi(casella_player, dir_x, dir_y, diz, indice_x, indice_y, matrice, robot, screen, strada)
    else:
        dir_x = 0
        dir_y = 0


def muovi(casella_p, dir_x, dir_y, diz, indice_x, indice_y, matrice, robot, screen, strada):
    nuova_casella = matrice[indice_y+dir_y][indice_x+dir_x]
    print(nuova_casella)
    lato_x = indice_x * 100
    lato_y = indice_y * 100
    if(nuova_casella in diz[casella_p]):
        print("puo muovere")
        print(maxsize)
        surf1 = pygame.Surface((100, 100))
        surf1.blit(strada, (0, 0))
        screen.blit(robot, ((lato_x-100)+dir_x, (lato_y-100)+dir_y))

def generate_maze(rows, cols):
    maze = [[0] * cols for _ in range(rows)]
    start_row = random.randint(0, rows - 1)
    start_col = random.randint(0, cols - 1)
    maze[start_row][start_col] = 3  # Imposta la partenza

    for row in range(rows):
        for col in range(cols):
            if maze[row][col] != 3:  # Ignora la cella di partenza
                maze[row][col] = random.choice([0, 1])  # Imposta 0 o 1 casualmente

    return maze

def save_maze_to_csv(maze, filename):
    with open(filename, 'w', newline='') as csvfile:
        maze_writer = csv.writer(csvfile)
        for row in maze:
            maze_writer.writerow(row)    

def main():
    """
    Author: Noemi Baruffolo
    date: 05/02/2024
    es. 062 robot
    text: fare file csv contenente
    3, 0, 0, 1, 0, 1
    0, 1, 0, 0, 0, 0
    1, 0, 0, 1, 1, 1
    1, 0, 1, 1, 1, 0
    0, 0, 1, 1, 0, 0
    0, 0, 1, 0, 0, 0
    che deve essere aperto dal programma e deve creare una matrice.
    (facoltativo) una volta ottenuta la matrice, disegnarlo in pygame. Per ogni cella libera trovare se intorno è libera o meno
    """

    #coordinate correnti, spostamento a livello grafico del robot, aggiustare muovi

    lato_x = 100
    lato_y = 100
    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    matrice = [[-1 for _ in range(n_x)] for _ in range(n_y)]
    k = 1

    casella_player = 0
    dir_x = 0
    dir_y = 0

    #SETUP per schermo, immagini e font
    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x , n_y * lato_y))
    muro = pygame.image.load("muro.png")
    strada = pygame.image.load("strada.jpg")
    robot = pygame.image.load("robot.jpg").convert_alpha()
    font = pygame.font.SysFont("Verdana", 18) 
    
    for ind_y,riga in enumerate(pavimento):
        for ind_x, casella in enumerate(riga):
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
                casella_player = k
                indice_x = ind_x
                indice_y = ind_y
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

    k = 1
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0 or casella == 3:
                matrice[indice_riga][indice_colonna] = k
                k += 1

    diz = {}
    adiacenze = []
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0 or casella == 3:
                if indice_riga != 0: #tocca il soffitto (controllo tutti tranne soffitto)
                    if matrice[indice_riga - 1 ][indice_colonna] != -1:
                        adiacenze.append(matrice[indice_riga-1][indice_colonna])
                if indice_riga != n_y - 1: #tocca parete sotto 
                    if matrice[indice_riga + 1][indice_colonna] != -1:
                        adiacenze.append(matrice[indice_riga+1][indice_colonna])   
                if indice_colonna != 0: #tocca sinistra
                    if matrice[indice_riga][indice_colonna - 1] != -1:
                        adiacenze.append(matrice[indice_riga][indice_colonna-1])
                if indice_colonna != n_x - 1: #tocca destra 
                    if matrice[indice_riga][indice_colonna + 1] != -1:
                        adiacenze.append(matrice[indice_riga][indice_colonna+1])               
                diz[matrice[indice_riga][indice_colonna]] = adiacenze
                adiacenze = []
    
    print(diz)
    print(indice_x)
    print(indice_y)
    print(matrice)

    #pygame.quit()
    #exit()
    done = False
    while not done:
        for ev in pygame.event.get():
            get_input(dir_x, dir_y, casella_player, diz, indice_x, indice_y, matrice, robot, screen, strada)
            #print(dir_x, dir_y)
            if ev.type == QUIT:
                done = True
    pygame.quit()


    rows = 5
    cols = 5
    maze = generate_maze(rows, cols)
    save_maze_to_csv(maze, 'maze.csv')
    print("Labirinto generato e salvato in 'maze.csv'")

    '''matrice = [[0, 4, 0], [4, 0, 3], [0, 3, 0]]
    sorg = int(input("inserisci il nodo sorgente: "))
    label, pred = dijkstra(sorg, matrice)
    print(label, pred)
    dest = int(input("inserisci il nodo di destinazione: "))
    lista = [dest]
    prec = pred[dest]
    lista.append(prec)
    while prec != sorg:
        prec = pred[prec]
        lista.append(prec)
    lista = lista[::-1]   
    print(lista)'''

if __name__ == "__main__":
    main()