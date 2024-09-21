# -*- coding: utf-8 -*-
"""
#KT 4
Pääset suunnittelemaan Tuote-sovellusta suuren kauppaketjun tuotekehitysosastolla. Tehtävänäsi on suunnitella luokkarakenne, 
jolla voidaan hallinnoida yrityksen tuotteita. Kaikilla tuotteilla on samat yhteiset ominaisuudet: nimi, hinta, hyllypaikka sekä koodi. 
Nämä esitellään tuote-luokassa, jonka aliluokat perivät. Aliluokkia on kolme, joilla on omia ominaisuuksia:

a.                         vaate: koko, materiaali
b.                         ruoka: maa, paivays
c.                         kodinkone: takuu, paino 

Tee yksinkertainen ohjelma, jolla voit syöttää tuotteita yhdelle tuotelistalle sekä tulostaa koko listan sisällön. 
Luokkien jäsenmuuttujien tyyppejä ei ole määritelty eli saat päättää ne itse. Ohjelmassa ensin valitaan minkä 
tyyppistä tuotetta ollaan syöttämässä, jonka jälkeen tiedot täytetään. Miten lopetat syötön on sinun päätettävissä. 
Tietysti lopuksi lista tulostetaan.

Ohessa esimerkkiajo:

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: 1
Anna tuotteen nimi: Sokeri
Anna hinta: 2.45
Anna hyllypaikka: Ruoka 11
Anna koodi: 111-222-333-22
Ruuan alkuperämaa: Tanska
Päiväys: 1.3.2024

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: 2
Anna tuotteen nimi: Paita
Anna hinta: 22.10
Anna hyllypaikka: Vaate 3
Anna koodi: 222-122-232-11
Vaatteen koko: M
Vaatteen materiaali: Puuvilla

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: 3
Anna tuotteen nimi: Pakastin
Anna hinta: 320.00
Anna hyllypaikka: Varasto 12
Anna koodi: 543-234-232-22
Kodinkoneen takuu: 1 vuosi
Kodinkoneen paino: 100kg

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: l

Nimi:       Sokeri
Hinta:      2.45
Hylly:      Ruoka 11
Koodi:      111-222-333-22
Alkuperä:   Tanska
Päiväys:    1.3.2024

Nimi:       Paita
Hinta:      22.10
Hylly:      Vaate 3
Koodi:      222-122-232-11
Koko:       M
Materiaali: Puuvilla

Nimi:       Pakastin
Hinta:      320.00
Hylly:      Varasto 12
Koodi:      543-234-232-22
Takuu:      1 vuosi
Paino:      100kg

#TASK 4
You are tasked with designing a product application for the product development department of 
a large retail chain. Your task is to design a class structure to manage the company’s products. 
All products have the same common attributes: name, price, shelf location, and code. These are presented 
in a base product class that the subclasses will inherit from. There are three subclasses, each with its own specific attributes:

a. Clothing: size, material
b. Food: country of origin, expiration date
c. Appliance: warranty, weight

Write a simple program that allows users to enter products into a single product list and print 
the entire content of the list. The types of the class attributes are not specified, so you can 
decide them yourself. In the program, users first select which type of product is being entered, 
and then fill in the relevant details. How to stop entering products is up to you. Naturally, at the end, the entire list is printed.

Here’s an example of the program:

What type of product is being added to the list (1 = Food, 2 = Clothing, 3 = Appliance, other = Exit): 1  
Enter product name: Sugar  
Enter price: 2.45  
Enter shelf location: Food 11  
Enter code: 111-222-333-22  
Country of origin: Denmark  
Expiration date: 1.3.2024  

What type of product is being added to the list (1 = Food, 2 = Clothing, 3 = Appliance, other = Exit): 2  
Enter product name: Shirt  
Enter price: 22.10  
Enter shelf location: Clothing 3  
Enter code: 222-122-232-11  
Clothing size: M  
Material: Cotton  

What type of product is being added to the list (1 = Food, 2 = Clothing, 3 = Appliance, other = Exit): 3  
Enter product name: Freezer  
Enter price: 320.00  
Enter shelf location: Warehouse 12  
Enter code: 543-234-232-22  
Appliance warranty: 1 year  
Weight: 100kg  

What type of product is being added to the list (1 = Food, 2 = Clothing, 3 = Appliance, other = Exit): other  

Name: Sugar  
Price: 2.45  
Shelf: Food 11  
Code: 111-222-333-22  
Country of origin: Denmark  
Expiration date: 1.3.2024  

Name: Shirt  
Price: 22.10  
Shelf: Clothing 3  
Code: 222-122-232-11  
Size: M  
Material: Cotton  

Name: Freezer  
Price: 320.00  
Shelf: Warehouse 12  
Code: 543-234-232-22  
Warranty: 1 year  
Weight: 100kg

"""
# Base class tuote and its derived classes
class tuote:
    def __init__(self, nimi, hinta, hyllypaikka, koodi):
        self.nimi = nimi
        self.hinta = hinta
        self.hyllypaikka = hyllypaikka
        self.koodi = koodi

    def __str__(self):
        return f'Nimi: {self.nimi}\nHinta: {self.hinta:.2f}\nHylly: {self.hyllypaikka}\nKoodi: {self.koodi}'


class vaate(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, koko, materiaali):
        super().__init__(nimi, hinta, hyllypaikka, koodi)
        self.koko = koko
        self.materiaali = materiaali

    def __str__(self):
        return f'{super().__str__()}\nKoko: {self.koko}\nMateriaali: {self.materiaali}'


class ruoka(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, maa, paivays):
        super().__init__(nimi, hinta, hyllypaikka, koodi)
        self.maa = maa
        self.paivays = paivays

    def __str__(self):
        return f'{super().__str__()}\nAlkuperä: {self.maa}\nPäiväys: {self.paivays}'


class kodinkone(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, takuu, paino):
        super().__init__(nimi, hinta, hyllypaikka, koodi)
        self.takuu = takuu
        self.paino = paino

    def __str__(self):
        return f'{super().__str__()}\nTakuu: {self.takuu}\nPaino: {self.paino}'


# Main program
def main():
    tuotteet = []

    while True:
        valinta = input('Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus): ')
        if valinta not in ['1', '2', '3']:
            break

        nimi = input('Anna tuotteen nimi: ')
        hinta = float(input('Anna hinta: '))
        hyllypaikka = input('Anna hyllypaikka: ')
        koodi = input('Anna koodi: ')

        if valinta == '1':
            maa = input('Ruuan alkuperämaa: ')
            paivays = input('Päiväys: ')
            tuote_obj = ruoka(nimi, hinta, hyllypaikka, koodi, maa, paivays)
        elif valinta == '2':
            koko = input('Vaatteen koko: ')
            materiaali = input('Vaatteen materiaali: ')
            tuote_obj = vaate(nimi, hinta, hyllypaikka, koodi, koko, materiaali)
        elif valinta == '3':
            takuu = input('Kodinkoneen takuu: ')
            paino = input('Kodinkoneen paino: ')
            tuote_obj = kodinkone(nimi, hinta, hyllypaikka, koodi, takuu, paino)

        tuotteet.append(tuote_obj)

    for tuote_obj in tuotteet:
        print(f'\n{tuote_obj}')


if __name__ == '__main__':
    main()








