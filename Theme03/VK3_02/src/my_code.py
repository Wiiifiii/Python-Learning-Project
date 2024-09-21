# -*- coding: utf-8 -*-

#
# KT2
#
# Kysy käyttäjältä, montako lukua arvotaan.Jos käyttäjä syöttää arvon < 1, tulostuu "Virhe!"
# Tee lista ja arvo siihen em määrä lukuja  väliltä 0-20.
# Vain parilliset luvut sallitaan.
# Jos arvottiin pariton luku niin sen tilalle on arvottava uusi luku.
# Tulosta luvuista suurin ja pienein samalle riville
# Ja lopuksi tulosta arvotut luvut yhdelle riville pilkulla erotettuna
# Huomaa, että viimeisen luvun jälkeen ei tule pilkkua
#
# Esimerkkiajo ohessa
#
# Montako lukua arvotaan: 3
# Suurin: 6 ja pienin: 0
# 4,0,6
#

import random

# Ask the user how many numbers to generate
maara = int(input("Montako lukua arvotaan: "))

# Check if the number is valid
if maara < 1:
    print("Virhe!")
else:
    # Initialize an empty list to store the generated numbers
    luvut = []

    # Generate the required number of even numbers between 0 and 20
    while len(luvut) < maara:
        arpa = random.randint(0, 20)  # Random number between 0 and 20
        if arpa % 2 == 0:  # Check if the number is even
            luvut.append(arpa)  # Add the even number to the list

    # Print the largest and smallest number
    suurin = max(luvut)
    pienin = min(luvut)
    print(f"Suurin: {suurin} ja pienin: {pienin}")

    # Print the list of numbers, joined by commas, without a trailing comma
    print(",".join(map(str, luvut)))

