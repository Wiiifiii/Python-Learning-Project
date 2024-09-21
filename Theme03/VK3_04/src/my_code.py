# -*- coding: utf-8 -*-

"""
KT 4

Kysy käyttäjältä lukujjen määrä ja arvo annettu  kplmäärä  liukulukuja väliltä 1 – 100.
Arvo luku seuraavasti:
    random_decimal = random.randint(100, 10000) / 100
Tulosta arvottu luku käyttäjälle (samalle riville kuin edellinen välilyönnillä erotettuna) ja kirjoita se arvot.txt tiedostoon allekkain.
Jos syötetty luku on < 1, ei ohjelma päättyy ja tulostuu "Virhe!".

Jos tiedosto on jo olemassa, vanhat tiedot menetetään
Älä käytä listaa tms tässä vaiheessa vaan vie luku tiedostoon heti, kun se on arvottu.
Sen jälkeen lue arvot tiedostosta listaan ja lajittele se. Tämän jälkeen tulosta listan  arvot sekä vie
lukujen kplmäärä, summa, keskiarvo, minimiarvo ja maksimiarvo tulokset.txt -tiedostoon
oheisen mallin mukaisesti kahdella desimaalilla (pl kpl):
Kpl: 2
Sum:5.00
Ka: 2.50
Min: 1.00
Max:4.00

Ohessa ajoesimerkki:

Montako lukua arvotaan? 3
Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt:
75.41 12.84 17.27
Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:
12.84 17.27 75.41
Ja lopuksi  tiedostosta tulokset.txt löytyy seuraavat tiedot:
Lkm: 3
Sum: 105.52
Ka: 35.17
Min: 12.84
Max: 75.41

Ole taas huolellinen tulostusten kanssa!

"""

import random

# Ask the user for the number of numbers to be generated
n = int(input("Montako lukua arvotaan? "))

# Check if the number is valid
if n < 1:
    print("Virhe!")
else:
    # Open the file 'arvot.txt' for writing, this will overwrite the file if it already exists
    with open("arvot.txt", "w") as file:
        print("Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt:")

        # Generate the required number of random numbers and write them to the file
        for i in range(n):
            random_decimal = random.randint(100, 10000) / 100  # Generate a random float between 1.00 and 100.00
            print(f"{random_decimal:.2f}", end=" ")  # Print the number to the console (same line)
            file.write(f"{random_decimal:.2f}\n")  # Write the number to the file (each on a new line)
    
    print()  # Newline after printing all numbers

    # Read the numbers from 'arvot.txt' and load them into a list
    with open("arvot.txt", "r") as file:
        luvut = [float(line.strip()) for line in file]

    # Sort the numbers
    luvut.sort()

    # Print the sorted numbers
    print("Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:")
    print(" ".join(f"{luku:.2f}" for luku in luvut))

    # Calculate statistics
    summa = sum(luvut)
    keskiarvo = summa / len(luvut)
    minimi = min(luvut)
    maksimi = max(luvut)

    # Write the statistics to 'tulokset.txt'
    with open("tulokset.txt", "w") as file:
        file.write(f"Lkm: {len(luvut)}\n")
        file.write(f"Sum: {summa:.2f}\n")
        file.write(f"Ka: {keskiarvo:.2f}\n")
        file.write(f"Min: {minimi:.2f}\n")
        file.write(f"Max: {maksimi:.2f}\n")

    # Print the statistics
    print("Ja lopuksi tiedostosta tulokset.txt löytyy seuraavat tiedot:")
    print(f"Lkm: {len(luvut)}")
    print(f"Sum: {summa:.2f}")
    print(f"Ka: {keskiarvo:.2f}")
    print(f"Min: {minimi:.2f}")
    print(f"Max: {maksimi:.2f}")
