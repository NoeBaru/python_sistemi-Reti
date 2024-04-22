def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 
    text: insiemi: collezioni non indicizzabili
    """
    a = set([1, 2, 3]) #crea un insieme
    b = set([5, 6])
    print(a)
    print(b)
    print(a|b)
    print(a&b)
    b.remove(6)   
    print(b) 
if __name__ == '__main__':
    main()