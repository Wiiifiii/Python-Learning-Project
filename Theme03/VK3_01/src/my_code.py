# -*- coding: utf-8 -*-
"""
#KT 1

Luo aluksi tyhjä lista (muuttujanimi: luvut) ja lue siihen käyttäjältä 5 kokonaislukuarvoa.
Tulosta lopuksi syötettyjen lukujen summa (kokonaislukuna) ja keskiarvo kolmella desimaalilla

Esimerkkiajo ohessa

Anna luku: 1
Anna luku: 2
Anna luku: 3
Anna luku: 4
Anna luku: 5
Summa on: 15
Keskiarvo on: 3.000

#TASK 1
First, create an empty list (variable name: luvut).
Read 5 integer values from the user and add them to the list.
Finally, print the sum of the entered numbers (as an integer) and the average with three decimal places.

Example run:
Enter a number: 1  
Enter a number: 2  
Enter a number: 3  
Enter a number: 4  
Enter a number: 5  
The sum is: 15  
The average is: 3.000

    
"""


# Initialize an empty list to store the numbers
luvut = []

# Loop to read 5 integers from the user
for i in range(5):
    luku = int(input("Anna luku: "))  # Ask for a number
    luvut.append(luku)  # Add the number to the list

# Calculate the sum of the numbers
summa = sum(luvut)

# Calculate the average of the numbers
keskiarvo = summa / len(luvut)

# Print the results
print(f"Summa on: {summa}")
print(f"Keskiarvo on: {keskiarvo:.3f}")



