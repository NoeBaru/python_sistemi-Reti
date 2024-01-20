class Testo():
    def __init__(self, testo):
            self.frase = testo
            
    def calcoloNumChar(self):
        numChar = len(Testo.frase)
        return numChar
    
    def listaTesto(self):
        lista = []
        
        return lista
    
    def listaLungParole(self):
        lung = []
        lista = [Testo.listaTesto]
        
        for i in len(Testo.listaTesto):
            lung[i] = len(lista[i])
            
        return lung
    def cercaParola(self):
        trovato = False
        list = Testo.listaTesto()
        parola = "ciao"
        
        for i in len(list):
            if (parola == list[i]):
                trovato = True
            
            if(trovato):
                return True
            else:
                return False
            
    def salvaSuFile(self):
        file = open("testoVer.txt", "w")
        file.write(Testo.frase)
        file.close()
        
    def dizionarioFreq(self):
        freq = {}
        return freq
    
def main():
    """
    Author: Noemi Baruffolo
    date: 19/01/2024
    es.  01
    text: analisi del testo
    """
    t = Testo("ciao sono io")
    if(t.cercaParola() == True):
        print("Trovata! ")
    else:
        print("Non trovata!")
    print(f"i caratteri sono {t.calcoloNumChar}, le parole sono {t.listaTesto} e ogni parola è lunga: {t.listaLungParole}")
if __name__ == '__main__':
    main()