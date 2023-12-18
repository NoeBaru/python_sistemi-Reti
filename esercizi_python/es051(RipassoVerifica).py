import random

class Nemico():
    def __init__(self, posX, posY, nVite):
        self.posX = posX
        self.posY = posY
        self.nVite = nVite
    def stampa(self):
        print(f"Nemico in posizione {self.posX}, {self.posY} con {self.nVite} vite")

class Personaggio():
    def __init__(self):
        pass

def main():
    """
    Author: Noemi Baruffolo
    date: 18/12/2023
    es. 51 esRipassoVerifica
    text: ripasso per verifica su dizionari e classi
    """
    #dizionari:
    dizionario = {"a": "albero", "b": "brutto", "c": "casa"}
    #lista = ["albero", "brutto", "casa"]
    
    print(dizionario["b"])
    #print(lista[1])
    
    dizionario["d"] = "dado"
    print(dizionario)
    
    #iterazione dizionario su chiave
    for chiave in dizionario:
        print(f"La chiave {chiave} ha valore: {dizionario[chiave]}")
    
    #ricerca di presenza di una chiave
    if "a" in dizionario:
        print("'a' è presente nel dizionario")
    
    
    #classi:
    N_NEMICI = 5
    WIDTH = 800
    HEIGHT = 400
    
    listaNemici = []
    random.seed(1234) #seme del generatore di numeri pseudo casuali, così hai sempre la stessa sequenza di numeri
    
    for _ in range(N_NEMICI): #_ perché non ci serve a niente la variabile
        posX = random.randint(0, WIDTH - 1) #include gli estremi ed è intero perché in pixel
        posY = random.randint(0, HEIGHT - 1)
        nemico = Nemico(posX, posY, 5)
        listaNemici.append(nemico)
    print(listaNemici)
    
    personaggio = {"posX": 100, "posY": 200}
    for nemico in listaNemici:
        nemico.stampa()
        if (nemico.posX == personaggio["posX"]) and (nemico.posY == personaggio["posY"]):
            print("COLLISIONE")
    
if __name__ == '__main__':
    main()