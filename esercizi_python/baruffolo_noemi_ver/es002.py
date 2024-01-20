def main():
    """
    Author: Noemi Baruffolo
    date: 19/01/2024
    es. 02
    text: numeri narcisisti
    """
    lista = [] #supporto dove mettere le cifre divise
    numNarcis = [] #lista che contiene solo i numeri narcisisti da 1 a 999
    
    for num in range(1,1000):
        s = str(num) #numero versione stringa
        lista.append(s.split) #metto nella lista di supporto la stringa divisa
        #print(lista) #testo del codice
        
        for i in len(lista): #itero nella lista di supporto
            somma += lista[i] ** 3
            print(somma)
            if (somma == s):
                numNarcis.append(s)
    print(numNarcis)

if __name__ == '__main__':
    main()