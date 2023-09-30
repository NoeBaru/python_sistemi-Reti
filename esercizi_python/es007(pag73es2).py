"""
Author: Noemi Baruffolo
date: 26/09/2023
es. 007
text: chidere un numero in input e comunicare all'utente se questo numero è divisibile per 2, 3 o per 5, o per nessuno di essi. Per
verificare la divisibilità può esserti utile l'operatore resto '%'. L'espressione 'a % b' calcola il resto della divisione tra 'a' e 'b'
"""

def main():
    num = int(input("Inserisci un numero: "))

    if num % 2 == 0:
        print(f"il numero {num} e' divisibile per 2")

    elif num % 3 == 0:
        print(f"il numero {num} e' divisibile per 3")
    
    elif num % 5 == 0:
        print(f"il numero {num} e' divisibile per 5")

    else:
        print(f"il numero {num} NON e' divisibile per 2 o 3 o 5")

if __name__=="__main__": 
    main()