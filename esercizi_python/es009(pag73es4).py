"""
Author: Noemi Baruffolo
date: 26/09/2023
es. 009
text: calcolare quanti sono i quadrati perfetti minori di 200
"""

import math

#i quadrati perfetti/numeri quadrati sono tutti i numeri interi la cui radice quadrata e' un numero intero
def main():
    cont  = 0
    for num in 200:
        ris = math.sqrt(cont)
        if ris.is_integer():
            cont += 1
    
    print(f"I quadrati perfetti minori di 200 sono{cont}")

if __name__=="__main__": 
    main()