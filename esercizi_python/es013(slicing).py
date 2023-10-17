"""
Author: Noemi Baruffolo
date: 3/10/2023
es. 013
text: SLICING di stringhe
"""
def main():
    s1 = "ciao" #in Python si può indicizzare con numeri negativi e l'ultimo carattere è -1
    #se voglio i caratteri iniziali uso l'indicizzazione positiva, se gli ultimi, quella negativa
    print(f"il primo carattere e'{s1[0]}")
    print(f"l'ultimo carattere e'{s1[-1]}")
    print(f"il penultimo carattere e'{s1[-2]}")
    print(f"l'ultimo carattere e'{s1[len(s1)-1]}") #C-style, DA NON USARE perché più complesso per nulla, basta usare -1

    s2 = "ciao come stai?"
    print(f"La srtinga dal 3^ carattere al 7^ escluso: {s2[3:7]}") #dal 3 al 7 ESCLUSO
    print(f"Tutta la stringa escluso il primo carattere e l'ultimo: {s2[1:-1]}")
    print(f"Tutta la stringa escluso il primo carattere: {s2[1:]}") #ESCLUDE il primo e l'ultimo
    print(f"Tutta la stringa escluso l'ultimo: {s2[:-1]}") #funziona anche se si mette 0 al posto di nulla
    print(f"Tutta la stringa al contrario: {s2[::-1]}") #specchia la stringa
if __name__=="__main__": 
    main()