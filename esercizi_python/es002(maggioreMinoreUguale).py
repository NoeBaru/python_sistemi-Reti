"""
Author: Noemi Baruffolo
date: /09/2023
es. 002
text: dato un numero in input dire se e' > 5 o compreso tra 0 e 5 o < di 0
"""

def main():
    a = float(input("Inserisci un numero: "))

    print(f"Il tipo di a e' {type(a)}")

    #si puo' usare al posto del switch case
    if a > 5:
        print("a e' maggiore di 5")
    elif (a <= 5) and (a >= 0):
        print("a >= 0 oppure a <= 5")
    else :
        print("a e' minore di 0")

if __name__=="__main__": 
    main() 