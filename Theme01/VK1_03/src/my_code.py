# -*- coding: utf-8 -*-

"""

Lue käyttäjältä arvot kahteen lukumuuttujaan. Nimeä muuttujat nimillä eka ja toka sekä alusta ne arvolla nolla.
Tulosta näiden muuttujien summa, erotus ja tulo alla olevalla tavalla (HUOM! Laskutoimituksen tulostus alkaa kaikissa samasta kohdasta!)

Anna eka luku: 10

Anna toka luku: 5

Summa :        10 + 5 = 15

Erotus :       10 - 5 = 5

Tulo :         10 * 5 = 50
"""

# Initialize the variables with default values
eka = 0  # First number
toka = 0  # Second number

# Read values from the user for 'eka' and 'toka'
eka = int(input("Anna eka luku: "))  # Read first number from user
toka = int(input("Anna toka luku: "))  # Read second number from user

# Calculate the sum, difference, and product
summa = eka + toka
erotus = eka - toka
tulo = eka * toka

# Print the results in the required format
print(f"Summa :       {eka} + {toka} = {summa}")
print(f"Erotus :      {eka} - {toka} = {erotus}")
print(f"Tulo :        {eka} * {toka} = {tulo}")
