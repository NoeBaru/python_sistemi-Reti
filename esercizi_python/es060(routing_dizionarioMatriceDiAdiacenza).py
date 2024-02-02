import networkx as nx
import matplotlib.pyplot as plt

def drawGraph(matriceAdiacenza):
    G = nx.Graph(matriceAdiacenza)

    pos = nx.spring_layout(G)  #Specifica il layout del disegno del grafo

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', font_family='Arial')
    plt.show()

def main():
    """
    Author: Noemi Baruffolo
    date: 30/01/2024
    es. 059
    text: creare il dizionario della matrice di adiacenza del seguente dizionario
          d = {0: [2, 3], 1: [2,4], 2: [0,1, 3], 3:[0, 2, 4],4: [1, 3] }
    """
    matrice = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]}
    drawGraph(matrice)
    pass #non fa niente, così non da errori nel codice
if __name__ == '__main__':
    main()