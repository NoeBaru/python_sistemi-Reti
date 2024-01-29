def main():
    """
    Author: Noemi Baruffolo
    date: 29/01/2024
    es. 57 tuple
    text: tuple, a differenza delle liste, non sono modificabili(immutabili)
    """
    t = (3, 4, 10, 2)
    # t[1] = 9 #ERRORE
    print(t[0])
    
    punto = (3, 4)
    x, y = punto #assegnazione multipla, spacchettamento della tupla
    print(y)
    
if __name__ == '__main__':
    main()