# -*- coding: utf-8 -*-

"""
KT6
Kysy käyttäjältä mitä hän haluaa seuraavista vaihtoehdoista (eli käyttäjä syöttää joko numeron 0, 1, 2 tai 3) :

   0 = Lopetus
   1 = Anna säde
   2 = Laske ympyrän piiri
   3 = Laske ympyrän pinta-ala

   Anna valintasi:

Tulosta kysymys edellä kuvatulla tavalla.

Muu kuin 0,1,2,3 vastaa nollaa eli päättää ohjelman toiminnan.

Vaihtoehto 0 päättää ohjelman

Vaihtoehto 1 kysyy ympyrän säteen.  Säteen oletusarvo on nolla (0.0)

Vaihtoehto 2 tulostaa ympyrän piirin (laskukaava on piiri = 2 * pii * säde)

Vaihtoehto 3 tulostaa ympyrän alan (laskukaava on  ala = pii * sade * sade) pinta-ala ja tulosta se.

Jos vaihtoehto on ollut 1,2,3, niin toimenpiteiden (syöttö/tulostus) jälkeen tulostetaan edellä kuvattu  vaihtoehtokysymys uudelleen

Hae piin arvo math moduulista (koodin alkuun import math ja sen jälkeen pii saadaan  math.pi muuttujasta)

Tulosta kaikki desimaaliluvut kahden desimalin tarkkuudella.

Esimerkkiajo ohessa

0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 1
Anna säde: 12


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 2
Piiri on 75.40


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 3
Ala on 452.39


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 0

"""

import math

# Initialize the radius variable with a default value of 0.0
sade = 0.0

# Function to display the menu
def tulosta_valinnat():
    print("0 = Lopetus")
    print("1 = Anna säde")
    print("2 = Laske ympyrän piiri")
    print("3 = Laske ympyrän pinta-ala")
    print("Anna valintasi:", end=" ")

# Start an infinite loop to process user input until the user decides to quit
while True:
    # Display the options
    tulosta_valinnat()
    
    # Read the user's choice
    valinta = int(input())
    
    # Check the user's choice and perform the appropriate action
    if valinta == 0:
        # Exit the program
        print("Ohjelma lopetettu.")
        break
    elif valinta == 1:
        # Ask for the radius
        sade = float(input("Anna säde: "))
    elif valinta == 2:
        # Calculate and print the circumference
        piiri = 2 * math.pi * sade
        print(f"Piiri on {piiri:.2f}")
    elif valinta == 3:
        # Calculate and print the area
        ala = math.pi * sade * sade
        print(f"Ala on {ala:.2f}")
    else:
        # Invalid choice, exit the program
        print("Ohjelma lopetettu.")
        break




