class Testo():
    def __init__(self, testo):
            self.frase = testo
            self.lista = self.frase.split(" ")
            
    def calcoloNumChar(self):
        numChar = len(self.frase)
        return numChar
    
    def listaTesto(self):
        return self.lista
    
    def listaLungParole(self):
        return [len(parola) for parola in self.lista]
    def cercaParola(self, parola):
        return parola in self.lista
            
    def salvaSuFile(self, nomeFile):
        with open(nomeFile, "w") as file:
            file.write(self.frase)
        
    def dizionarioFreq(self):
        freq = {}
        for parola in self.lista:
            if parola in freq:
                freq[parola] += 1
            else:
                freq[parola] = 1
        return freq
    
def main():
    """
    Author: Noemi Baruffolo
    date: 22/01/2024
    es.  01
    text: analisi del testo
    """
    prova = "ciao sono io"
    
    t = Testo(prova)
    print(t.calcoloNumChar())
    print(t.listaLungParole())
    print(t.cercaParola("ciao"))
    t.salvaSuFile("testoVer.txt")
    print(t.dizionarioFreq())
    
if __name__ == '__main__':
    main()