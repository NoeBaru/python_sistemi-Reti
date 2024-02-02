import networkx as nx
import matplotlib.pyplot as plt

def drawGraph(matrice):
    G = nx.Graph(matrice)

    pos = nx.spring_layout(G)  #Specifica il layout del disegno del grafo

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', font_family='Arial')
    plt.show()

def main():
    """
    Author: Noemi Baruffolo
    date: 01/02/2024
    es. 061 disegno grafi
    text: fare una funzione python che a partire dalla matrice di adiacenza, crei il disegno del grafo networkX
    """
    matrice = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]} # Matrice di adiacenza fornita
    
    drawGraph(matrice) #Chiamata alla funzione per disegnare il grafo
if __name__ == '__main__':
    main()