"""
Author: Noemi Baruffolo
date: 27/11/2023
es. 046 es1 vecchia ver
text: Un braccio robotico industriale libero di muoversi avanti e indietro lungo una rotaia è impazzito. Ogni secondo si muove
scegliendo a caso tra due possibili movimenti: 1 cm in avanti, oppure 1 cm indietro. Non è possibile togliere corrente al robot senza
bloccare tutto lo stabilimento, quindi bisogna attendere lo spegnimento che si effettua tutti i fine settimana e oggi purtroppo è lunedì!
Il tuo responsabile ti chiede di creare un programma in Python per simulare lo spostamento totale che il robot avrà effettuato dopo 5
interi giorni di pazzia.
- Definisci una funzione che restituisca uno spostamento casuale (+1 o -1).
- Utilizza una list comprehension per creare la  lista contenente tutta la sequenza degli spostamenti casuali.
- Infine calcola la somma degli spostamenti casuali per ottenere lo spostamento complessivo accumulato in 5 giorni.
"""

import random #per una lista uso random.choice e estrae a caso uno degli elementi

def spostamentoRandom():
    return random.choice([-1, 1])

def main():
    movimenti = [spostamentoRandom() for _ in range(5 * 24 * 60 * 60)]
    spostamentoTot = sum(movimenti)

    print(f"Spostamento totale dopo 5 giorni: {spostamentoTot} cm")

if __name__ == '__main__':
    main()