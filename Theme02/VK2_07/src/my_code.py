# -*- coding: utf-8 -*-

"""
KT7

Toimeentulotukea maksetaan turvaamaan perustuslaissa tarkoitettu välttämätön toimeentuloa.
Tee ohjelma, joka laskee yksinäisen henkilön tai perheen saaman toimeentulotuen.
Ohjelma laskee tuen määrän käyttäjän syöttämälle määrälle päiviä ja tulostaa toimeentulotuen kokonaismäärän kahdella desimaalilla.
Ohjelma kysyy tuen laskemisessa tarvittavat tiedot yhdessä asumisesta ja lapsista.
Toimeentulotuen määrä lasketaan alla olevan taulukon mukaisesti kahden desimaalin tarkkuudella.
Toimeentulotuen laskemista voidaan toistaa niin monta kertaa kuin ohjelman käyttäjä haluaa. Alla on suuntaa antava esimerkki ohjelman toiminnasta.

Tuki lasketaan siis yhdelle henkilölle, ei esim avioparille


Tuen saaja

Euroa / päivä

Yksin asuva

16,18

Yksinhuoltaja

17,80

Avio- ja avopuolisot kumpikin

13,76

Jokainen 10-17-vuotias lapsi

11,33

Jokainen alle 10-vuotias lapsi

10,20



Tämä ohjelma laskee toimeentulotuen määrän. Alla esimerkkiajo ohjelmasta.

Koodin rakenteelle ei aseteta vaatimuksia muuten kuin, että syötteet annetaan esimerkin mukaisessa järjestyksessä ja ohjelma laskee (tulostaa) tuen määrän oikein. Esimerkkiajosta käy ilmi. että kysymyksiä luupataan eli ohjelma päättyy vasta kun  käyttäjä ei halua enää laskea toimeentulotukea uusilla tiedoilla.



Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): k

Asutko yksin (1) vai puolison kanssa (2) : 1

Onko sinulla/teillä alaikäisiä lapsia (k/e) : k

Kuinka monta alle 10-vuotiasta lasta : 1

Kuinka monta 10-17-vuotiasta lasta : 2

Kuinka monelle päivälle tuki lasketaan : 10



Saat toimeentulotukea 506.60 euroa

Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): e

"""

# -*- coding: utf-8 -*-

import math

# Constants for daily support amounts
YKSIN_ASUVA = 16.18
YKSINHUOLTAJA = 17.80
AVI_PARISKUNTA = 13.76
LAPSI_10_17 = 11.33
LAPSI_ALLE_10 = 10.20

def laske_toimeentulotuki():
    # Ask if the person lives alone or with a partner
    asuu_yksin = int(input("Asutko yksin (1) vai puolison kanssa (2) : "))

    # Initialize the base support amount
    tuki = 0.0
    
    # Ask if they have children
    lapsia = input("Onko sinulla/teillä alaikäisiä lapsia (k/e) : ").lower()

    if asuu_yksin == 1:
        if lapsia == 'k':
            # Single parent case
            tuki = YKSINHUOLTAJA
        else:
            # Single, no children
            tuki = YKSIN_ASUVA
    elif asuu_yksin == 2:
        # Married or living with a partner
        tuki = AVI_PARISKUNTA * 2  # Since both partners get support
    else:
        print("Virheellinen syöte.")
        return 0.0

    if lapsia == 'k':
        # Ask for the number of children under 10 and between 10 and 17
        alle_10_lapsia = int(input("Kuinka monta alle 10-vuotiasta lasta : "))
        yli_10_lapsia = int(input("Kuinka monta 10-17-vuotiasta lasta : "))

        # Add the support for each child
        tuki += alle_10_lapsia * LAPSI_ALLE_10
        tuki += yli_10_lapsia * LAPSI_10_17

    # Ask for how many days the support should be calculated
    paivat = int(input("Kuinka monelle päivälle tuki lasketaan : "))

    # Calculate the total support amount
    toimeentulotuki = tuki * paivat

    # Return the calculated support amount, rounded to two decimals
    return round(toimeentulotuki, 2)

def main():
    while True:
        # Ask if the user wants to calculate the support
        jatketaanko = input("Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): ").lower()

        if jatketaanko == 'k':
            # Calculate the support
            tuki = laske_toimeentulotuki()
            print(f"Saat toimeentulotukea {tuki:.2f} euroa")
        elif jatketaanko == 'e':
            print("Ohjelma lopetettu.")
            break
        else:
            print("Virheellinen syöte, yritä uudelleen.")

if __name__ == "__main__":
    main()


