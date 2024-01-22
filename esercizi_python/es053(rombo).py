def main():
    """
    Author: Noemi Baruffolo
    date: 11/01/2024
    es. 53
    text: chiedere un numero n, stampare un rombo
    esempio 
                *
               ***
              *****
               ***
                *
    """
    n = int(input("Inserisci un numero dispari: \n"))
    spazi = n //2
    if n % 2 == 0:
        print("Il numero inserito non è dispari, verrà utilizzato il numero successivo dispari.")
        n += 1
    for i in range(1, n + 1, 2):
        print(" " * spazi + "*" * i)
        spazi -= 1
    spazi += 1
    for i in range(n - 2, 0, -2):
        spazi += 1
        print(" " * spazi + "*" * i)

if __name__ == '__main__':
    main()