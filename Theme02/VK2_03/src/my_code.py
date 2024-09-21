# -*- coding: utf-8 -*-
"""
#KT 3

Tee ohjelma, joka pyytää käyttäjää syöttämään lampotila -nimiseen muuttujaan jonkin mielivaltainen 
lämpötilan arvon (mieti tyyppi tarkasti kun ensin katsot alla olevaa...). Ohjelman tulee siis hyväksyä esim lämpötila 22.5.

Ohjelma tulostaa sitten seuraavasti, kun lämpötila on:

>39 tulostuu : Liian kuuma
<=39 ja >10 tulostuu : Lämmintä
<=10 ja >=0 tulostuu : Haaleaa
<0 ja >-30 tulostuu : Pakkasta
<=-30 tulostuu : Liian kylmää

Toteuta ohjelma if-elif-else -rakenteella.

Ole tarkka, että tulostat juuri sen tekstin, jota pyydettiin!


#TASK 3
Create a program that asks the user to input a temperature value into a variable called lampotila 
(consider the appropriate type based on the example below). The program should accept a value like 22.5 for temperature.

The program should print the following depending on the temperature:

    If the temperature is greater than 39, print: "Too hot"
    If the temperature is less than or equal to 39 and greater than 10, print: "Warm"
    If the temperature is less than or equal to 10 and greater than or equal to 0, print: "Mild"
    If the temperature is less than 0 and greater than -30, print: "Freezing"
    If the temperature is less than or equal to -30, print: "Too cold"

Implement the program using an if-elif-else structure.

Be precise and ensure you print exactly the text requested!
"""

# Ask the user to input a temperature value (which can be a decimal number)
lampotila = float(input("Anna lämpötila: "))

# Use if-elif-else structure to categorize the temperature and print the corresponding message
if lampotila > 39:
    print("Liian kuuma")
elif lampotila <= 39 and lampotila > 10:
    print("Lämmintä")
elif lampotila <= 10 and lampotila >= 0:
    print("Haaleaa")
elif lampotila < 0 and lampotila > -30:
    print("Pakkasta")
elif lampotila <= -30:
    print("Liian kylmää")
