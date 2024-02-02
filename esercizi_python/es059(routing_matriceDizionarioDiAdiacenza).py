import networkx as nx
import matplotlib.pyplot as plt

def drawGraph(matriceAdiacenza):
    G = nx.Graph(matriceAdiacenza)

    pos = nx.spring_layout(G)  #Specifica il layout del disegno del grafo

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', font_family='Arial')
    plt.show()

def prettyPrint(matrice, separatore = ' '):
    for riga in matrice:
        rigaStr = [str(x) for x in riga]
        print(separatore.join(rigaStr))

def main():
    """
    Author: Noemi Baruffolo
    date: 30/01/2024
    es. 059
    text: creare la matrice di adiacenza del seguente dizionario
          d = {0: [2, 3], 1: [2,4], 2: [0,1, 3], 3:[0, 2, 4],4: [1, 3] }
    """
    d = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]}
    nNodi = len(d) #numero di nodi nel grafo
    matriceAdiacenza = [[0] * nNodi for _ in range(nNodi)] #crea una matrice quadrata di dimensioni num_nodi x num_nodi in cui tutti gli elementi sono inizializzati a zero e sono di tipo intero

    for nodo, valori in d.items(): #caricamento della matrice con 1 dove serve, gli altri rimangono a 0
        for elemento in valori:
            matriceAdiacenza[nodo][elemento] = 1

    # Stampa la matrice di adiacenza
    prettyPrint(matriceAdiacenza)
    drawGraph(d)

if __name__ == '__main__':
    main()