def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    x = pila.pop()
    return x

def main():
    """
    Author: Noemi Baruffolo
    date: 6/12/2023
    es. 049
    text: pile
    """
    pila = [1, 2, 3, 4]
    
    push(pila, 10)
    print(pila)
    x = pop(pila)
    print(x)
    print(pila)
if __name__ == '__main__':
    main()