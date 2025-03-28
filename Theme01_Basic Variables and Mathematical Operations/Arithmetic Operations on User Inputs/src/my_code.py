# -*- coding: utf-8 -*-
"""
#KT 3
Lue käyttäjältä arvot kahteen lukumuuttujaan. Nimeä muuttujat nimillä eka ja toka sekä alusta ne arvolla nolla.
Tulosta näiden muuttujien summa, erotus ja tulo alla olevalla tavalla 
(HUOM! Laskutoimituksen tulostus alkaa kaikissa samasta kohdasta!)
Anna eka luku: 10
Anna toka luku: 5
Summa :        10 + 5 = 15
Erotus :       10 - 5 = 5
Tulo :         10 * 5 = 50

#TASK 3

Read values from the user into two number variables. Name the variables 'first' and 'second' and initialize them to zero.
Print the sum, difference, and product of these variables in the format shown below 
(NOTE! The arithmetic operation output starts at the same position for all operations!)
Example:
Enter the first number: 10
Enter the second number: 5
Sum :         10 + 5 = 15
Difference :  10 - 5 = 5
Product :     10 * 5 = 50

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
