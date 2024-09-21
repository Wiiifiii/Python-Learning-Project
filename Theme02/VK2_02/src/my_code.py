# -*- coding: utf-8 -*-
"""
#KT 2
Lue käyttäjältä koenumero 4-10 väliltä. Jos käyttäjä syötti arvosanan väärin (ei väliltä 4-10) , 
niin tulosta "Et antanut arvosanaa annetulta väliltä". Muussa tapauksessa tulosta:
Hyvä (jos arvosana oli 9 tai 10)
Kelpo (jos 7 - 8)
Tyydyttävä (jos 5 - 6)
Heikko (jos 4)
Toteuta ohjelma if-elif-else -rakenteella.
Ole tarkka, että tulostat juuri sen tekstin, jota pyydettiin.

#TASK 2
Read a grade from the user between 4 and 10.
If the user enters an invalid grade (not between 4-10), print:
"You did not give a grade from the given range".
Otherwise, print:
"Excellent" (if the grade is 9 or 10)
"Good" (if the grade is between 7 and 8)
"Satisfactory" (if the grade is between 5 and 6)
"Weak" (if the grade is 4)
Implement the program using if-elif-else structure.
Ensure that the text output matches exactly as required.

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
