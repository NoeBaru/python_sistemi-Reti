"""
Author: Noemi Baruffolo
date: 21/10/2023
es. 029 pag.73 es.21
text: Utilizza le list comprehension per creare una funzione che rimuova tutte le vocali presenti in una stringa.
"""

def main():
    stringa = input("Inserisci una stringa: ")
    vocali = "AEIOUaeiou"
    strOutput = [cont for cont in stringa if (cont not in vocali)]
    print(f" ".join(strOutput))
    
if __name__=="__main__": 
    main()