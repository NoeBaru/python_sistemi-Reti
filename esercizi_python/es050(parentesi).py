def push(pila, elemento, posizione):
    pila.append((elemento, posizione))

def pop(pila):
    if len(pila) == 0:
        return None
    else:
        return pila.pop()

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
    posizione = 0
    for carattere in str:
        posizione += 1

        if carattere in parentesiAperte:
            push(pila, carattere, posizione)

        if carattere in parentesiChiuse:
            parentesi = pop(pila)
            if parentesi is None or dizionario[parentesi[0]] != carattere:
                errore = True
                print(f"Errore! Parentesi non corrispondenti alla posizione {posizione}")
                break

    if not errore and len(pila) > 0:
        carattere, posizione = pila[-1]
        print(f"Errore! Parentesi non chiuse alla posizione {posizione}")
    elif not errore:
        if len(pila) == 0:
            print("Corretto!")
        else:
            carattere, posizione = pila[-1]
            print(f"Errore! Parentesi mancante alla posizione {posizione}")
if __name__ == '__main__':
    main()