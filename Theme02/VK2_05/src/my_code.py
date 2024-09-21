# -*- coding: utf-8 -*-

"""

KT5

Kysy käyttäjältä kaksi lukua. Ensimmäisessä luvussa annetaan alkuarvo  lukuparille ja toisessa montako kertaa lukuparia kasvatetaan/vähennetään.


Tulosta lukuparit allekkain for-silmukkaa käyttäen. Vasen luku siis kasvaa ja oikea vähenee yhden verran kullakin rivillä.

Jos käyttäjä antaa luvut 10 ja 5, tulostus näyttää seuraavalta:
10,10
11,9
12,8
13,7
14,6
15,5



Eli tulostuvan lukuparin ensimmäinen arvo kasvaa ja toinen vähenee lähtien liikkeelle luvusta 10 toistuen 5 kertaa

"""

# Ask the user for the starting number and how many times the pair should be incremented/decremented
lukuparin_alku = int(input("Anna lukuparin alkuarvo: "))
toistot = int(input("Kuinka monta kertaa lukuparia kasvatetaan/vähennetään: "))

# Use a for loop to print the pairs
for i in range(toistot + 1):  # Use 'toistot + 1' to include the last iteration properly
    vasen_luku = lukuparin_alku + i
    oikea_luku = lukuparin_alku - i
    print(f"{vasen_luku},{oikea_luku}")

