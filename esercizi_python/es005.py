#es005
def main():
    lista = [4, 100, 3, 5] #lista

    #ciclo C-style
    for i in range (0, len(lista)): #len da la lunghezza della lista
        print(f"L'elemento {i} della lista e' {lista[i]}")

    #for Python-style
    for elemento in lista:
        print(f"Elemento: {elemento}")

if __name__=="__main__": 
    main()