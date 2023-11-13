"""
Author: Noemi Baruffolo
date: 13/11/2023
es. 040 class
text: 
"""

class Quadrato(): #sempre con la maiuscola
    def __init__(self, lato): #costruttore della classe (il nome è sempre quello)
            self.lato = lato #come il this di Java
    def calcolaArea(self): #metodo nella classe
        return self.lato**2
    def stampaLato(self):
        print(f"Il lato è {self.lato}")
        
def main():
    q = Quadrato(4)
    print(f"L'area del quadrato q e': {q.calcolaArea()}") #non si mette self nelle chiamate
    
    #nulla e' privato, infatti posso fare:
    print(q.lato)
    q.lato = 5
    print(f"L'area del quadrato q e': {q.calcolaArea()}")
if __name__ == '__main__':
    main()