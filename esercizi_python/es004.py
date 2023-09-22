#es004
#chiedere due numeri in input e stampare i due numeri in ordine decrescente con un solo print
def main():
    n1 = float(input("Inserisci il primo numero: "))
    n2 = float(input("inserisci il secondo numer0: "))

    if n1 > n2:
        n1, n2 = n2, n1

    print(f"Il maggiore e' {n2} e il minore e'{n1}")

if __name__=="__main__": 
    main()