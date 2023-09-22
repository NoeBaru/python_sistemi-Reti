#es001
def main(): #main, i blocchi si dividono identando
    nome = input("Come di chiami? \n")#va a capo sempre la print
    anni = int(input("Quanti anni hai? \n"))#va a capo sempre la print
    #print(type(anni)) // dice il tipo della variabile
    annoCorrente = int(input("In che anno siamo? "))
    print(f"Il tuo nome e' {nome}, hai {anni} anni")
    print(f"Sei nato nel {annoCorrente - anni}")

if __name__=="__main__": 
    main() 