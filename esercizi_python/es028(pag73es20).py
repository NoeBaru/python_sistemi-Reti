"""
Author: Noemi Baruffolo
date: 21/10/2023
es. 028 pag.73 es.20
text: Utilizza le list comprehension per creare la tavola pitagorica per i numeri da 1 a 10. Stampa la tavola ottenuta e salvala su file.
"""

def print_tabellina(tabellina):
    for row in tabellina:
        for element in row:
            print(element, end=" ")
        print()

def main():
    n = 10
    tabellina = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
    print_tabellina(tabellina)
    
if __name__=="__main__": 
    main()