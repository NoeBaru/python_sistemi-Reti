#es006 pag.40 es.1

def main():
    num = int(input("Inserisci un numero: "))
    div = 3

    if num % div == 0:
        print(f"il numero {num} e' divisibile per {div}")
    else:
        print(f"il numero {num} NON e' divisibile per {div}")
if __name__=="__main__": 
    main()