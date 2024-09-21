# -*- coding: utf-8 -*-
"""
KT2
Olet aloittanut osakesijoittamisen ja haluat arvioida sijoituksesi arvoa. Ohjelmalla (pääohjelmassa) on lista, johon käyttäjä voi lisätä Osake-olioita. Ohjelma kysyy käyttäjältä ”Lisätäänkö uusi osake (k/e)”.
Kun osakkeet on lisätty listaan, kysyy ohjelma käyttäjältä kuvitteellisen kasvuprosentin sekä ajanjakson vuosina.

Tee luokka Osake, jolla on jäsenmuuttujat:
- nimi
- ostohinta (>0, osakekohtainen ostohinta)
- maara (> 0, omistettujen osakkeiden lkm)

Osakkeella on metodit:

- tulosta_arvo, jonka parametreina on  kasvuprosentin ja ajanjakson vuosina (tässä järjestyksessä). tulosta_arvo-metodi kutsuu toista Osake-luokan  metodia laske_tuotto_yhdelle_vuodelle, joka laskee vuosikohtaisen tuoton. tulosta_arvo kutsuu laske_tuotto_yhdelle_vuodelle-metodia vuosien lukumäärän verran. Siis, jos lasketaan tuottoa kolmelle vuodelle, niin laske_tuotto_yhdelle_vuodelle kutsutaan kolme kertaa. Huomio "korkoa korolle". Valuutat tulostetaan kahden desimaalin tarkkuudella.

- laske_tuotto_yhdelle_vuodelle -metodi palauttaa tuoton yhdelle vuodelle. Metodi on staattinen ja saa parametrinaan kasvuprosentin ja hinnan vuoden alussa (tässä järjesyksessä).

Laske pääohjelmassa  myös koko osakepotin arvo(sama % ja samat vuodet) käymällä lista läpi eli 
joudut miettimään sitä, miten pääohjelmaan palautetaan tieto yhden osakkeen potin arvosta vuosien jälkeen.

Esimerkkiajo:

Anna osakkeen nimi: Nokia
Anna osakkeen ostohinta/kpl: 10
Anna ostettujen osakkeiden lukumäärä: 1000
Lisää osakkeita (k/e)? k

Anna osakkeen nimi: Fortum
Anna osakkeen ostohinta/kpl: 12
Anna ostettujen osakkeiden lukumäärä: 127
Lisää osakkeita (k/e)? e

Anna kasvuprosentti: 5
Anna vuodet: 3

Nokia 1000 10.0
Osakkeen potin arvo on 11576.25 ja tuotto 1576.25

Fortum 127 12.0
Osakkeen potin arvo on 1764.22 ja tuotto 240.22

Koko potin arvo on 13340.47

#TASK 2
You have started stock investing and want to evaluate the value of your investment. 
The program (in the main program) will have a list where the user can add "Stock" objects. 
The program asks the user, "Would you like to add a new stock (y/n)?". Once the stocks are 
added to the list, the program asks the user for an imaginary growth rate and the duration in years.

Create a class "Stock" with the following member variables:

name: Stock name
purchase_price: (>0, per share purchase price)
quantity: (>0, number of shares owned)

The "Stock" class has the following methods:

print_value: Parameters are the growth rate and duration in years (in this order). 
The print_value method calls another method from the "Stock" class called calculate_annual_growth, 
which calculates the yearly return. The print_value method calls calculate_annual_growth for 
the number of years. For example, if calculating the return for three years, calculate_annual_growth
is called three times. The compound interest is taken into account. The values are printed with two decimal places.

calculate_annual_growth: This method returns the growth for one year. 
The method is static and receives the growth rate and the price at the beginning of the year (in this order).

In the main program, also calculate the total value of the stock portfolio (using the same % and years) 
by going through the list of stocks. You will need to figure out how to return the total value of the portfolio to the main program after several years.
Example Output:

Enter stock name: Nokia
Enter stock purchase price per share: 10
Enter the number of shares: 1000
Add more stocks (y/n)? y

Enter stock name: Fortum
Enter stock purchase price per share: 12
Enter the number of shares: 127
Add more stocks (y/n)? n

Enter growth rate: 5
Enter years: 3

Nokia 1000 10.0
Stock portfolio value is 11576.25, and profit is 1576.25

Fortum 127 12.0
Stock portfolio value is 1764.22, and profit is 240.22

Total portfolio value is 13340.47

"""
# Class for Osake (Stock)
class Osake:
    def __init__(self, nimi, ostohinta, maara):
        self.nimi = nimi
        self.ostohinta = ostohinta if ostohinta > 0 else 0  # Ensure price is greater than 0
        self.maara = maara if maara > 0 else 0  # Ensure the number of shares is greater than 0
    
    # Method to calculate and print stock value after the specified number of years and growth percentage
    def tulosta_arvo(self, kasvuprosentti, vuodet):
        nykyinen_hinta = self.ostohinta
        for _ in range(vuodet):
            nykyinen_hinta = self.laske_tuotto_yhdelle_vuodelle(kasvuprosentti, nykyinen_hinta)
        
        potin_arvo = nykyinen_hinta * self.maara
        alkuarvo = self.ostohinta * self.maara
        tuotto = potin_arvo - alkuarvo
        
        print(f"{self.nimi} {self.maara} {self.ostohinta:.2f}")
        print(f"Osakkeen potin arvo on {potin_arvo:.2f} ja tuotto {tuotto:.2f}")
        
        return potin_arvo  # Return the total value of the stock portfolio after growth

    # Static method to calculate the yearly return on the stock
    @staticmethod
    def laske_tuotto_yhdelle_vuodelle(kasvuprosentti, alkuhinta):
        return alkuhinta * (1 + kasvuprosentti / 100)


# Main program
if __name__ == "__main__":
    osakkeet = []  # List to store Osake objects
    
    # Ask the user for stock details and add to the list
    while True:
        nimi = input("Anna osakkeen nimi: ")
        ostohinta = float(input("Anna osakkeen ostohinta/kpl: "))
        maara = int(input("Anna ostettujen osakkeiden lukumäärä: "))
        
        # Create and add the Osake object to the list
        osakkeet.append(Osake(nimi, ostohinta, maara))
        
        # Ask if more stocks should be added
        jatka = input("Lisää osakkeita (k/e)? ").lower()
        if jatka != 'k':
            break
    
    # Ask for growth percentage and the number of years
    kasvuprosentti = float(input("Anna kasvuprosentti: "))
    vuodet = int(input("Anna vuodet: "))
    
    koko_potin_arvo = 0  # Variable to store the total portfolio value
    
    # Iterate over all the stocks and calculate their values
    for osake in osakkeet:
        koko_potin_arvo += osake.tulosta_arvo(kasvuprosentti, vuodet)
    
    # Print the total value of the portfolio
    print(f"Koko potin arvo on {koko_potin_arvo:.2f}")
