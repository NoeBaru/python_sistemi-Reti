"""
Author: Noemi Baruffolo
date: /09/2023
es. 001
text: intoduzione ai comandi di python
"""

def main(): #main, i blocchi si dividono identando

    nome = input("Come di chiami? \n")#va a capo sempre la print
    anni = int(input("Quanti anni hai? \n"))#va a capo sempre la print
    annoCorrente = int(input("In che anno siamo? "))
    #print(type(anni)) // dice il tipo della variabile
    
    print(f"Il tuo nome e' {nome}, hai {anni} anni")
    print(f"Sei nato nel {annoCorrente - anni}")

if __name__=="__main__": 
    main() 