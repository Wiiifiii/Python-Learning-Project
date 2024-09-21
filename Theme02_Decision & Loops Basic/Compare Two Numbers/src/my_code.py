# -*- coding: utf-8 -*-
"""
#KT 1
Lue käyttäjältä kaksi lukua ja tulosta niistä suurempi. 
Käytä if-else -lausetta vertailussa.

#TASK 1
Compare two numbers entered by the user and print the larger one.
Using an if-else statement for comparison.

"""
    
# Ask the user to input two numbers
luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))

# Compare the two numbers and print the larger one using if-else
if luku1 > luku2:
    print(f"Suurempi luku on {luku1}")
elif luku2 > luku1:
    print(f"Suurempi luku on {luku2}")
else:
    print("Luvut ovat yhtä suuret")


