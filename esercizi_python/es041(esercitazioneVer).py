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

def cercaCovid(seq, covid):
    return seq.find(covid)

def contaOccorrenze(seq, nucleotide):
    return seq.count(nucleotide)

def main():
    seq = ""
    covid = "ATGTTTGTTTTT"
    nucleotidi = {"A": 0, "T": 0, "G": 0, "C": 0}
    
    with open("covid-19_gen1.txt", "r") as file:
        seq = file.read().replace("\n", "")

    for nucleotide in nucleotidi:
        nucleotidi[nucleotide] = contaOccorrenze(seq, nucleotide)
    
    print("Numero di occorrenze di ogni nucleotide nella sequenza:", nucleotidi)
    
    posizione = cercaCovid(seq, covid)
    if posizione != -1:
        print("Sequenza trovata alla posizione:", posizione)
    else:
        print("Sequenza non trovata nel genoma.")

if __name__ == '__main__':
    main()