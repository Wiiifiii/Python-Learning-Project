# -*- coding: utf-8 -*-
"""
KT4
Laita vakioon ARVATTAVA_LUKU jonka arvo on 124
Määritä vakio funktion avulla.

Tee ohjelma, joka pyytää arvaamaan lukua.
Jos käyttäjä syötti isomman luvun kuin muuttujassa, niin tulosta : ”Annoit liian suuren luvun”.
Jos taas käyttäjän syöttämä luku oli pienempi kuin vakion luku niin tulosta : ”Annoit liian pienen luvun”.



Kun käyttäjä arvaa luvun oikein niin tulosta : ”Oikein, arvasit luvun 27 kerralla!”.
Missä siis arvo 27 kertoo montako kierrosta meni ennen kuin käyttäjä arvasi oikein

"""

# Define a constant using a function
def ARVATTAVA_LUKU():
    return 124

# Counter for the number of attempts
yritykset = 0

# Start the guessing loop
while True:
    # Ask the user to guess the number
    arvaus = int(input("Arvaa luku: "))
    yritykset += 1  # Increment the attempt counter

    # Check the user's guess and provide feedback
    if arvaus > ARVATTAVA_LUKU():
        print("Annoit liian suuren luvun")
    elif arvaus < ARVATTAVA_LUKU():
        print("Annoit liian pienen luvun")
    else:
        # The user guessed the correct number
        print(f"Oikein, arvasit luvun {yritykset} kerralla!")
        break  # Exit the loop when the correct number is guessed

