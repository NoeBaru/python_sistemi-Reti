"""
robot che si può spostare con ostacoli

definire una mappa (es. con un file csv)
0 se piastrella libera, 1 se occupata
0 e 1 vanno in un file csv
che dato il file, creare la matrice che rappresenta il pavimento
facoltativo: disegnarlo poi in pygame
scrivere una funzione che numeri le celle libere
in questo modo: 
0 1 -1 2
-1 3 4 5
poi da questa matrice restituire il dizionario delle adiacenze
"""
import pygame
import sys

LATOX = 100
LATOY = 100

class Cella():
    def __init__(self, n):
        self.size = (LATOX, LATOY)
        self.num = n
        self.numerata = True
        if n != 0:
            self.color = "red"
            self.numerata = False
        else:
            self.color = "green"
        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.color)


def mat2d_adiacenze(m: list[list]):
    return {i: [j for j, n in enumerate(m[i]) if n != 0] for i in range(len(m))}

def matrice_da_file(nome_file: str):
    mat = []
    with open(nome_file, "r") as file:
        for riga in file.readlines():
            t = riga.split(", ")
            mat.append([int(stringa[0]) for stringa in t])
    return mat

def disegna_matrice(screen: pygame.Surface, mat: list[list[Cella]]):
    text = pygame.font.Font(size = LATOX // 2)
    numero_in_cella = 0
    for i, riga in enumerate(mat):
        y = LATOY * i
        for j, cella in enumerate(riga):
            screen.blit(cella.surf, (LATOX * j, y))
            if cella.numerata:
                surf = text.render(f"{numero_in_cella}", True, "black")
                rect = surf.get_rect()
                rect.topleft= (LATOX * j + 8, y + 8)
                screen.blit(surf, rect)
                numero_in_cella += 1
    pygame.display.update()


def matrice_numerata(mat):
    mat_numerata = []
    numero_cella = 0
    for riga in mat:
        nuova_riga = []
        for cella in riga:
            if cella != 0:
                nuova_riga.append(-1)
            else:
                nuova_riga.append(numero_cella)
                numero_cella += 1
        mat_numerata.append(nuova_riga)
    return mat_numerata

def celleLibereAdiacenti(mappa):
    diz = {}
    for i, riga in enumerate(mappa):
        for j, colonna in enumerate(riga):
            if mappa[i][j] > -1:
                diz[mappa[i][j]] = []
                if i > 0:
                    if mappa[i - 1][j] > -1:#contiene il numero della cella da controllare se è libera la aggiungo
                        diz[mappa[i][j]].append(mappa[i - 1][j])
                if i+1 < len(mappa):
                    if mappa[i + 1][j] > -1:
                        diz[mappa[i][j]].append(mappa[i + 1][j])
                if j > 0:
                    if mappa[i][j - 1] > -1:
                        diz[mappa[i][j]].append(mappa[i][j - 1])
                if j + 1 < len(riga):
                    if mappa[i][j + 1] > -1:
                        diz[mappa[i][j]].append(mappa[i][j + 1])
    return diz

def sceltaNodo(non_visitati, label):
    minLabel = sys.maxsize
    minNodo = None
    for nodo in non_visitati:
        labelNodo = label[nodo]
        if labelNodo <= minLabel:
            minLabel = labelNodo
            minNodo = nodo
    
    return minNodo

def algoritmoDijstrak2(nodo_sorgente, matrice):
    
    n_nodi = len(matrice)

    nodo_precedente = {}

    non_visitati = set([i for i in range(0, n_nodi)])
    label = {i: sys.maxsize for i in range(0, n_nodi)}
    label[nodo_sorgente] = 0
    
    while len(non_visitati) > 0:
        nodoCorrente = sceltaNodo(non_visitati, label)
        #print(nodoCorrente)
        non_visitati.remove(nodoCorrente)

        for nodo_vicino, peso in enumerate(matrice[nodoCorrente]):
            if peso > 0:
                nuova_label = label[nodoCorrente] + peso
                if nuova_label < label[nodo_vicino]:
                    nodo_precedente[nodo_vicino] = nodoCorrente
                    label[nodo_vicino] = nuova_label
        
    return label, nodo_precedente

def main():
    pygame.init()
    clock = pygame.time.Clock()
    m = matrice_da_file("maze.csv")

    screen = pygame.display.set_mode((LATOX * len(m), LATOY * len(m[0])))
    celle = [[Cella(n) for n in riga] for riga in m]
    disegna_matrice(screen, celle)

    m_numerata = matrice_numerata(m)

    diz_adiac = celleLibereAdiacenti(m_numerata)
    print(diz_adiac)

    nodo_sorgente = 0

    matrice = [[0, 1, 0, 0, 0, 1, 2], [1, 0, 2, 3, 3, 1, 0], [0, 2, 0, 2, 1, 0, 0], [0, 3, 2, 0, 0, 1], 
                [0, 3, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 0, 0], [2, 0, 0, 1, 0, 0, 0]]
    diz_dijstrak, diz_nodo_precedente = algoritmoDijstrak2(nodo_sorgente, m)
    print(diz_dijstrak)
    print(diz_nodo_precedente)

    destinazione = int(input("inserisci il nodo destinazione: "))
    lista = []
    prec = diz_nodo_precedente[destinazione]
    lista.append(diz_nodo_precedente)

    while prec != nodo_sorgente:
        prec = diz_nodo_precedente[prec]
        lista.append(prec)
    lista = lista[::-1]
    print(lista)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        clock.tick(60)

if __name__ == "__main__":
    main()