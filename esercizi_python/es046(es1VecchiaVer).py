import random #per una lista uso random.choice e estrae a caso uno degli elementi

def calcolaSpostamenti(sec = 432000, lista = [-1, 1]): #usa questi valori se non passiamo nulla
    movimenti = [random.choice(lista) for _ in range(0, sec)]
    print(movimenti)
    lung = 0
    for val in movimenti:
        lung += val
    print(lung)

def main():
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
    
    sec = 432000
    lista = [-1, 1]
    
    calcolaSpostamenti(1000, [3,-3]) #passaggio parametri con valore di def (posso specificare anche solo un parametro o nessuno (basta sia nel giusto ordine))

if __name__ == '__main__':
    main()