"""
Author: Noemi Baruffolo
date: 13/11/2023
es. 041 "bioinformatica"
text: Il file covid-19_gen1.txt contiene la sequenza del genoma del virus SARS-CoV-2. Esso è una sequenza di lettere (A, C, G, T) che
corrispondono ai quattro nucleotidi costituenti: adenina (A), timina (T), guanina (G) e citosina (C) .
Crea un programma in linguaggio Python 3 nel quale:
- leggi tutte le righe del file e le inserisci all'interno di un sola stringa che contenga l'intera sequenza genomica;
- stampi il numero di occorrenze dei quattro nucleotidi all'interno della sequenza;
- cerchi la sequenza iniziale ("ATGTTTGTTTTT") che codifica la proteina spike nel genoma: se presente allora stampa la posizione iniziale
della sequenza.
"""

def cercaCovid(covid):
    tro = False
        if str == covid:
    return tro

def cercaOccorrenze(carattere):
    pass

def main():
    str = ""
    covid = "ATGTTTGTTTTT"
    nucleotidi = {"A": cercaOccorrenze("A"), "T": cercaOccorrenze("T"), "G": cercaOccorrenze("G"), "C": cercaOccorrenze("C")}
    file = open("covid-19_gen1.txt", "r")
    numR = len(file.readlines())
    str = file.readlines()
    file.close()
    for i in numR:
        if((i != numR - 1) & (str[i] == "\n")):
            str[i] == str[i + 1]
    print(numR)
    tro = cercaCovid(covid)
    
if __name__ == '__main__':
    main()