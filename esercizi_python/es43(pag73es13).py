"""
Author: Noemi Baruffolo
date: 19/11/2023
es. 42 pag.73 es.13
text: Crea una classe Python che astragga i robot. Essa deve avere tra gli attributi il nome del robot, la massa del robot, la sua
tipologia (umanoide oppure no). Inoltre deve avere un metodo che stampi il nome del robot e un metodo che ritorni se il robot può essere
pericoloso. Sono giudicati pericolosi i robot umanoidi con massa superiore ai 100 kg.
"""

class Robot:
    def __init__(self, nome, massa, tipologia='non umanoide'):
        self.nome = nome
        self.massa = massa
        self.tipologia = tipologia 
    def stampaNome(self):
        print(f"Il robot si chiama {self.nome}")
    def isPericoloso(self):
        return self.tipologia == 'umanoide' and self.massa > 100

def main():
    r1 = Robot("Noemi", 100, 'umanoide')
    r2 = Robot("Baruffolo", 101, 'umanoide')
    r1.stampaNome()
    print(f"ha una massa di {r1.massa} kg ed è pericoloso: {r1.isPericoloso()}")
    r2.stampaNome()
    print(f"ha una massa di {r2.massa} kg ed è pericoloso: {r2.isPericoloso()}")

if __name__ == '__main__':
    main()