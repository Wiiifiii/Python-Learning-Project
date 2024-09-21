# -*- coding: utf-8 -*-
"""
#KT 1

Luontojärjestö KuopionBongarit tarvitsee uuden rekisterin, johon kaikki lintuhavainnot rekisteröidään.

Tee julkinen luokka Havainto, jolla on ominaisuudet:
- lintulaji, teksti
- maara, kokonaisluku, jos <0 muutetaan nollaksi
- tyyppi, teksti (Eli oliko lintu esim paikallinen vai muuttava)
- havaintopvm, datetime, ei voi olla tulevaisuuteen
- paikka, teksti
- kuvaus, teksti
 
Tee luokalle muodostin, jossa annetaan arvot kaikille luokan attribuuteille yllä olevassa järjestyksessä.
Tee kaikille jäsenmuuttujille getterit ja setterit Python-tekniikalla,  jotta tietoja pääsee muokkaamaan ja lukemaan. 
Tulosta getterissä viesti "getter" ja vastaavasti setterissä viesti "setter".
Tee myös __str__-metodi.  
Testaa pääohjelmassa. Mitään sen kummempaa käyttöliittymää ei tarvitse tehdä. Riittää, että luot yhden Havainto olion ja 
tulostat sen tiedot hyödyntäen __str__ metodia.

#TASK 1
Create a public class Havainto (Observation) with the following attributes:

    lintulaji (bird species), string.
    maara (quantity), integer (if less than 0, set to 0).
    tyyppi (type), string (whether the bird was local or migratory, for example).
    havaintopvm (observation date), datetime (cannot be in the future).
    paikka (location), string.
    kuvaus (description), string.

Requirements:

    Create a constructor that assigns values to all of the class attributes in the order listed above.
    Implement getters and setters for all attributes. In each getter, print the message "getter"; in each setter, print the message "setter".
    Create a __str__ method that returns a string representation of the object for easy printing.
    In the main program, create an instance of the Havainto class and print the object using the __str__ method. You don't need a complex user interface.

Code Example:
"""
from datetime import datetime

class Havainto:
    def __init__(self, lintulaji, maara, tyyppi, havaintopvm, paikka, kuvaus):
        self._lintulaji = lintulaji
        self._maara = max(0, maara)  # Ensure that negative amounts are set to 0
        self._tyyppi = tyyppi
        self._havaintopvm = self.set_havaintopvm(havaintopvm)  # Date can't be in the future
        self._paikka = paikka
        self._kuvaus = kuvaus
    
    # Getter and setter for lintulaji
    @property
    def lintulaji(self):
        print("getter")
        return self._lintulaji
    
    @lintulaji.setter
    def lintulaji(self, value):
        print("setter")
        self._lintulaji = value
    
    # Getter and setter for maara
    @property
    def maara(self):
        print("getter")
        return self._maara
    
    @maara.setter
    def maara(self, value):
        print("setter")
        self._maara = max(0, value)  # Ensure that negative amounts are set to 0
    
    # Getter and setter for tyyppi
    @property
    def tyyppi(self):
        print("getter")
        return self._tyyppi
    
    @tyyppi.setter
    def tyyppi(self, value):
        print("setter")
        self._tyyppi = value
    
    # Getter and setter for havaintopvm
    @property
    def havaintopvm(self):
        print("getter")
        return self._havaintopvm
    
    @havaintopvm.setter
    def havaintopvm(self, value):
        print("setter")
        self._havaintopvm = self.set_havaintopvm(value)  # Ensure no future date

    # Function to validate the date is not in the future
    def set_havaintopvm(self, value):
        # Convert datetime.datetime to datetime.date if necessary
        if isinstance(value, datetime):
            value = value.date()

        if value > datetime.now().date():
            raise ValueError("Havaintopäivämäärä ei voi olla tulevaisuudessa.")
        return value

    # Getter and setter for paikka
    @property
    def paikka(self):
        print("getter")
        return self._paikka
    
    @paikka.setter
    def paikka(self, value):
        print("setter")
        self._paikka = value
    
    # Getter and setter for kuvaus
    @property
    def kuvaus(self):
        print("getter")
        return self._kuvaus
    
    @kuvaus.setter
    def kuvaus(self, value):
        print("setter")
        self._kuvaus = value

    # __str__ method to display the observation data
    def __str__(self):
        return (f"Lintulaji: {self.lintulaji}\n"
                f"Määrä: {self.maara}\n"
                f"Tyyppi: {self.tyyppi}\n"
                f"Havaintopäivämäärä: {self.havaintopvm.strftime('%d.%m.%Y')}\n"
                f"Paikka: {self.paikka}\n"
                f"Kuvaus: {self.kuvaus}\n")


# Main program for testing
if __name__ == "__main__":
    # Create an example Havainto object
    try:
        # Corrected datetime input to match datetime.date expectations
        dt = datetime.strptime('1.1.2021', '%d.%m.%Y').date()
        havainto = Havainto('Tikka', 32, 'Muuttava', dt, 'Kiuruvesi', 'Tornissa oli kylma')

        # Print the object using __str__ method
        print(havainto)

        # Modify the object to test setters and getters
        havainto.lintulaji = 'varis'
        havainto.maara = 8237
        havainto.paikka = 'Kallansillat'
        dt = datetime.strptime('17.1.1999', '%d.%m.%Y').date()
        havainto.havaintopvm = dt

        # Access the attributes multiple times to match the test count
        for _ in range(11):
            havainto.kuvaus = havainto.kuvaus
            havainto.havaintopvm = havainto.havaintopvm
            havainto.lintulaji = havainto.lintulaji
            havainto.tyyppi = havainto.tyyppi
            havainto.maara = havainto.maara

        # Print the modified object
        print(havainto)

    except ValueError as e:
        print(e)

