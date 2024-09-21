# -*- coding: utf-8 -*-

"""
KT2
Lue käyttäjältä koenumero 4-10 väliltä. Jos käyttäjä syötti arvosanan väärin (ei väliltä 4-10) , niin tulosta "Et antanut arvosanaa annetulta väliltä". Muussa tapauksessa tulosta:

 Hyvä (jos arvosana oli 9 tai 10)

 Kelpo (jos 7 - 8)

 Tyydyttävä (jos 5 - 6)

 Heikko (jos 4)

 Toteuta ohjelma if-elif-else -rakenteella.

 Ole tarkka, että tulostat juuri sen tekstin, jota pyydettiin.

 
"""
# Read the exam score from the user
koenumero = int(input("Anna koenumero (4-10 väliltä): "))

# Check if the score is within the valid range
if koenumero < 4 or koenumero > 10:
    print("Et antanut arvosanaa annetulta väliltä")
else:
    # Use if-elif-else to categorize the score and print the appropriate message
    if koenumero == 9 or koenumero == 10:
        print("Hyvä")
    elif koenumero == 7 or koenumero == 8:
        print("Kelpo")
    elif koenumero == 5 or koenumero == 6:
        print("Tyydyttävä")
    elif koenumero == 4:
        print("Heikko")
