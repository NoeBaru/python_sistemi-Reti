"""
Author: Noemi Baruffolo
date: 21/10/2023
es. 028 pag.73 es.20
text: Utilizza le list comprehension per creare la tavola pitagorica per i numeri da 1 a 10. Stampa la tavola ottenuta e salvala su file.
"""

def print_tabellina(tabellina):
    file = open("tabelline.txt", "w")
    for cont, element in enumerate(tabellina): #enumerate numera le liste, ritorna indice(cont) ed elemento(element)
        print(f"Tabellina del {cont + 1}: {element}") #element è una lista, tabellina è una lista di liste
        file.write(f"Tabellina: {element}\n")
    file.close()
def main():
    n = 10
    tabellina = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
    print_tabellina(tabellina)       
if __name__=="__main__": 
    main()