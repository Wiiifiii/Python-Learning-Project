# -*- coding: utf-8 -*-
"""
#KT 1

Tee ohjelma, jossa kysytään KysyJaTestaaLuku() nimisessä funktiossa  käyttäjältä kokonaisluku. 
Funktio palauttaa kokonaislukuarvon seuraavasti:
1, jos syötetty luku on positiivinen.
0, jos syötetty luku on nolla.
-1, jos syötetty luku on negatiivinen. 
Tulosta näiden paluuarvojen perusteella pääohjelmassa ilmoitus ruudulle.

”Luku oli positiivinen”, jos paluuarvo oli 1.
”Luku oli nolla”, jos paluuarvo oli 0
”Luku oli negatiivinen”, jos paluuarvo oli -1.

#TASk 1
Create a program where the function KysyJaTestaaLuku() asks the user for an integer.

The function returns an integer value as follows:

    1, if the entered number is positive.
    0, if the entered number is zero.
    -1, if the entered number is negative.

Based on the return values, print the following messages in the main program:

    "The number was positive" if the return value is 1.
    "The number was zero" if the return value is 0.
    "The number was negative" if the return value is -1.
"""

# Define the KysyJaTestaaLuku function
def KysyJaTestaaLuku():
    # Ask the user for an integer
    luku = int(input("Anna kokonaisluku: "))
    
    # Return 1 if positive, 0 if zero, -1 if negative
    if luku > 0:
        return 1
    elif luku == 0:
        return 0
    else:
        return -1

# Main program
if __name__ == "__main__":
    # Call the function and store its return value
    tulos = KysyJaTestaaLuku()

    # Based on the return value, print the corresponding message
    if tulos == 1:
        print("Luku oli positiivinen")
    elif tulos == 0:
        print("Luku oli nolla")
    elif tulos == -1:
        print("Luku oli negatiivinen")
