#es007 pag.40 es.2

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