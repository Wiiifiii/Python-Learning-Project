# -*- coding: utf-8 -*-
"""
#KT 1
Tee kaksi lambda-funktiota:
* summa saa parametrinaan kaksi lukua ja palauttaa niiden summan
* tulo saa parametrinaan kaksi lukua ja palauttaa niiden tulon
Tee laske-funktio, joka saa parametrinaan funktion ja listan lukuja. Funktio palauttaa listassa olevien 
lukujen tulon tai summan riippuen kumpaa em lambda-funktiota käytettiin funktion kutsussa. Jos luvut-lista on tyhjä, 
niin palautetaan 0 ja jos luvut sisältää vain yhden alkion, niin palautetaan tämä alkio.
VIHJE: Jos lista=[1, 2, 3], niin voit laskea alkioiden summan, s,  summa-funktion avulla näin:
s=summa(summa(1, 2), 3) .
Vastaava pätäee myös tuloon.
Pääohjelma on valmiina, älä muokkaa sitä.
Esimerkkitulostus:
1320
28
4
4
0
0

#TASK 1

Create two lambda functions:

    summa takes two numbers as parameters and returns their sum.
    tulo takes two numbers as parameters and returns their product.

Create a laske function that takes a function and a list of numbers as parameters. The function returns the product or sum of the numbers in the list, depending on which of the two lambda functions (described above) is used in the function call. If the luvut list is empty, return 0, and if the list contains only one element, return that element.

Hint: If the list is [1, 2, 3], you can calculate the sum of its elements using the summa function as follows:
s = summa(summa(1, 2), 3).

The same logic applies to the product.

Note: The main program is already written; do not modify it.

Example Output:
1320
28
4
4
0
0

"""
# Define the lambda functions
summa = lambda a, b: a + b
tulo = lambda a, b: a * b

# Define the laske function
def laske(function, luvut):
    if not luvut:  # If list is empty
        return 0
    elif len(luvut) == 1:  # If list contains only one element
        return luvut[0]
    
    tulos = luvut[0]
    for num in luvut[1:]:
        tulos = function(tulos, num)  # Apply the function cumulatively
    return tulos

# Don't touch lines below
if __name__ == "__main__":
    luvut = [1,5,8,11,3]
    print(laske(tulo, luvut))  # Output: 1320 (product of all elements)
    print(laske(summa, luvut))  # Output: 28 (sum of all elements)

    luvut = [4]
    print(laske(tulo, luvut))  # Output: 4 (only one element, so return it)
    print(laske(summa, luvut))  # Output: 4 (only one element, so return it)

    luvut = []
    print(laske(tulo, luvut))  # Output: 0 (empty list, so return 0)
    print(laske(summa, luvut))  # Output: 0 (empty list, so return 0)
