def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    if len(pila) == 0:
        x = None
    else:
        x = pila.pop()
    return x

def main():
    """
    Author: Noemi Baruffolo
    date: 6/12/2023
    es. 050
    text: data una stringa, controllare se le parentesi sono corrette o no e stampare dove c'è l'errore
    """
    parentesiAperte = ["{", "[", "("]
    parentesiChiuse = ["}", "]", ")"]
    
    dizionario = {"{" : "}", "[": "]", "(": ")"}
    str = "{1+[2+3]*5}"
    pila = []
    errore = False
    for carattere in str:
        if carattere in parentesiAperte:
            push(pila, carattere)
            
        if carattere in parentesiChiuse:
            parentesi = pop(pila)
            if(parentesi != None):
                if dizionario[parentesi] != carattere:
                    errore = True
                    break
            else:
                errore = True
    if errore:
        print("Errore!")
    else:
        print("Corretto!")
if __name__ == '__main__':
    main()