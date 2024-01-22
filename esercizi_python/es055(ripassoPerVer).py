def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. ripasso per verifica
    text: 
    """
    lettere = "abcdefghilmnopqrstuvz ?"
    N = len(lettere)
    lettere2numeri = {} #lettere to numeri
    numeri2lettere = {}
    for pos, lettera in enumerate(lettere):
        lettere2numeri[lettera] = pos
        numeri2lettere[pos] = lettera
        
    testoChiaro = "ciao come stai?"
    chiave = "itisdelpozzo"
    
    testoCriptato = ""
    for letteraTesto, letteraChiave in zip(testoChiaro, chiave):
        numero = (lettere2numeri[letteraTesto] + lettere2numeri[letteraChiave]) % N
        testoCriptato += numeri2lettere[numero]
    print(f"il testo '{testoChiaro}' criptato diventa '{testoCriptato}'.")
    
    testoChiaro = ""
    for letteraTesto, letteraChiave in zip(testoCriptato, chiave): #letteraTesto cicla su testo Criptato e letteraChiave su chiave
        numero = (numeri2lettere[letteraTesto] + numeri2lettere[letteraChiave]) % N
        testoChiaro += lettere2numeri[numero]
    print(f"il testo '{testoCriptato}' decriptato diventa '{testoChiaro}'.")
        
    pass #non fa niente, così non da errori nel codice
if __name__ == '__main__':
    main()