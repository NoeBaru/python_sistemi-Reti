"""
Author: Noemi Baruffolo
date: 25/10/2023
es. 033 dizonario
text: dizionario: collezione di coppie: chiave (un solo tipo) e valore, non ha indici, ma si indicizza per chiave
lista: come dizionario, ma senza la chiave e quindi la posizione, sennò bisogna ricordarsi che il nome è pos[0]
"""
def main():
    dizionario = {"nome": "Mario", "cognome": "Rossi"} #nome e cognome sono chiave , Mario e Rossi sono valore
    print(dizionario) #stampo tutto il dizionario
    print(dizionario["nome"]) #stampo solo il valore della chiave nome
    lista = ["Mario", "Rossi"]

    #si aggiunge al dizionario
    dizionario["data nascita"] = "01/01/1900" 
    dizionario["anni"] = 123
    
    #sovrascrive l'elemento chiave "nome"
    dizionario["nome"] = "Luca" 
    print(dizionario)

    #ciclo for sul dizionario
    for chiave in dizionario:
        print(f"chiave: {chiave} - valore: {dizionario[chiave]}")

    #rubrica
    rubrica = {38189192: "Mario Rossi", 348039013: "Alice Verdi", 32193991: "Luca Gialli"} #numero prima perché omonimi magari
    print(rubrica)

if __name__ == '__main__':
    main()