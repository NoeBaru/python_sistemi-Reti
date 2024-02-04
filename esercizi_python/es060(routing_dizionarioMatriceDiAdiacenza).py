import networkx as nx
import matplotlib.pyplot as plt

def drawGraph(graph):
    G = nx.Graph(graph)

    pos = nx.spring_layout(G)
    
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', font_family='Arial')
    plt.show()

def prettyPrint(matrice, separatore=' '):
    for riga in matrice:
        rigaStr = [str(x) for x in riga]
        print(separatore.join(rigaStr))

def createGraphFromMatrix(matriceAdiacenza):
    graph = {}
    nNodi = len(matriceAdiacenza)

    for i in range(nNodi):
        graph[i] = [j for j, valore in enumerate(matriceAdiacenza[i]) if valore == 1]

    return graph

def main():
    """
    Author: Noemi Baruffolo
    date: 30/01/2024
    es. 060
    text: creare il dizionario di una matrice di adiacenza data
    """
    matriceAdiacenza = [
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ]

    prettyPrint(matriceAdiacenza)

    d = createGraphFromMatrix(matriceAdiacenza)
    print("\nGrafo creato:")
    print(d)

    # Disegna il grafo creato
    drawGraph(d)

if __name__ == '__main__':
    main()