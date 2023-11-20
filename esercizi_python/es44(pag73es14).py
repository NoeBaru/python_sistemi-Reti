"""
Author: Noemi Baruffolo
date: 19/11/2023
es. 43 pag.73 es.14
text: Crea una classe Python che astragga la figura geometrica del quadrato sul piano euclideo. La classe deve essere dotata di metodi
per calcolare l'area, il perimetro e dato un punto verificare se esso è esterno al quadrato.
"""

class Quadrato:
    def __init__(self, lato):
        self.lato = lato
    def calcoloArea(self):
        return self.lato**2
    def calcoloPerimetro(self):
        return self.lato * 4
    def descrizione(self):
        return f"lato: {self.lato}, area: {self.calcoloArea()}, perimetro: {self.calcoloPerimetro()}"
    def puntoInterno(self, x, y):
        if(x > 0 and x < self.lato and y > 0 and y < self.lato):
            return True
        else:
            return False

def main():
    q1 = Quadrato(3)
    q2 = Quadrato(10)
    
    print(q1.descrizione())
    print(q1.puntoInterno(4, 5))
    
    print(q2.descrizione())
    print(q2.puntoInterno(4, 5))
    
if __name__ == '__main__':
    main()