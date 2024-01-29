def somma(a, b):
    return a + b

def main():
    """
    Author: Noemi Baruffolo
    date: 29/01/2024
    es. 58 lambda
    text: lambda function, utile per definire funzioni brevi
    """
    x, y = 10, 4
    lista = [10, 4]
    print(somma(x, y))
    #al posto si pu0' scrivere:
    somma = lambda x, y: x + y #parametri separati da ',' e quando finito ':', poi cosa deve ritornare
    print(somma(*lista))#spacchettamento della lista sui parametri
if __name__ == '__main__':
    main()