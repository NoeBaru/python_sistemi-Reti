"""
Author: Noemi Baruffolo
date: 26/09/2023
es. 006 pag.73 es.1
text: chiedere un numero in input e comunicare all'utente se questo numero è divisibile per 3 oppure no. Per verificare la divisibilità
può esserti utile l'operatore resto '%'. L'espressione 'a % b' calcola il resto della divisione tra 'a' e 'b'
"""

def main():
    num = int(input("Inserisci un numero: "))
    div = 3

    if num % div == 0:
        print(f"il numero {num} e' divisibile per {div}")
    else:
        print(f"il numero {num} NON e' divisibile per {div}")
if __name__=="__main__": 
    main()