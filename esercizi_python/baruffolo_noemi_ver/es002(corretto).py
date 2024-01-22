def main():
    """
    Author: Noemi Baruffolo
    date: 22/01/2024
    es. 02
    text: numeri narcisisti
    """
    for num in range(1,1000):
        numStr = str(num) #numero versione stringa        
        if sum([int(cifra)**3 for cifra in numStr]) == num: #itero nella lista di supporto
            print(f"il numero {num}  è narcisista")

if __name__ == '__main__':
    main()