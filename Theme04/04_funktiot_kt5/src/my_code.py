"""
KT5

Dictionarya käytetään autojen rekisteröintietietojen tallentamiseen. Kirjoita seuraavat funktiot:

LueAutot - Lukee näppäimistöltä ensin auton rekisterinumeron ja sitten rekisteröintipäivämäärän ja tallentaa tiedot dictionaryyn. 
Tätä toistetaan niin kauan kunnes rekisterinumeroksi syötetään LOPPU. Päivämäärät tallennetaan datetime-tyyppisinä. 
Funktio palauttaa täytetyn dictionaryn. datetime-tyypin käyttö on opiskeltava omatoimisesti. Päivämäärä syötetään muodossa dd.mm.yyyy, 
siis esimerkiksi 14.1.2022. Rekisteröintipäivämäärä pyydetään syöttämään uudestaan mikäli päivämäärä on väärässä muodossa.

TalletaTiedostoon - Saa parametrina edellisen dictionaryn ja tallenta sen sisällön tekstitiedostoon autot.txt. 
Tiedostossa päivämäärät eivät sisällä kellonaikaa. Tiedoston kukin rivi sisältää auton rekisterinumeron 
ja rekisteröintipäivämäärän '\t'-merkillä erotettuna

LueTiedostosta - Lukee autot.txt:n dictionaryyn ja palauttaa sen.

TulostaTiedot - Saa parametrinaan dictionaryn joka sisältää rekisteröintitiedot. 
Funktio tulostaa autojen rekisterinumerot ja rekisteröintipäivämäärät.

Kirjoita tarvittaessa testiohjelma funktioiden testaamiseksi.

VINKKI: Jos luet tiedostoa f rakenteella

for line in f:
   ...

niin muuttuja line sisältää myös rivinvaihdon. Sen voit poistaa str.strip()-metodilla.

"""
import datetime

# Function to read car data from the user and store it in a dictionary
def LueAutot():
    autot = {}
    
    while True:
        rekisterinumero = input("Anna auton rekisterinumero (LOPPU lopettaa): ")
        if rekisterinumero == "LOPPU":
            break
        
        while True:
            paivamaara = input("Anna rekisteröintipäivämäärä (dd.mm.yyyy): ")
            try:
                # Parse the date to datetime object
                rekisteroitymis_paiva = datetime.datetime.strptime(paivamaara, "%d.%m.%Y").date()
                autot[rekisterinumero] = rekisteroitymis_paiva
                break
            except ValueError:
                print("Väärä päivämäärämuoto! Anna päivämäärä muodossa dd.mm.yyyy")
    
    return autot

# Function to save car data into a file
def TalletaTiedostoon(autot):
    with open("autot.txt", "w", encoding="utf-8") as f:
        for rekisterinumero, rekisteroitymis_paiva in autot.items():
            # Write each entry with registration date formatted without time
            f.write(f"{rekisterinumero}\t{rekisteroitymis_paiva.strftime('%d.%m.%Y')}\n")

# Function to read car data from a file and return it as a dictionary
def LueTiedostosta():
    autot = {}
    
    try:
        with open("autot.txt", "r", encoding="utf-8") as f:
            for line in f:
                # Strip the newline and split the line by tab character
                rekisterinumero, paivamaara = line.strip().split('\t')
                # Convert the date string back to datetime object
                rekisteroitymis_paiva = datetime.datetime.strptime(paivamaara, "%d.%m.%Y").date()
                autot[rekisterinumero] = rekisteroitymis_paiva
    except FileNotFoundError:
        print("Tiedostoa autot.txt ei löytynyt.")
    
    return autot

# Function to print car registration data
def TulostaTiedot(autot):
    if not autot:
        print("Ei rekisteröityjä autoja.")
        return
    
    for rekisterinumero, rekisteroitymis_paiva in autot.items():
        print(f"Rekisterinumero: {rekisterinumero}, Rekisteröintipäivämäärä: {rekisteroitymis_paiva.strftime('%d.%m.%Y')}")

# Main program for testing
if __name__ == "__main__":
    # Step 1: Read car data from the user
    autot = LueAutot()
    
    # Step 2: Save the car data to a file
    TalletaTiedostoon(autot)
    
    # Step 3: Load the car data from the file
    luetut_autot = LueTiedostosta()
    
    # Step 4: Print the loaded car data
    TulostaTiedot(luetut_autot)
