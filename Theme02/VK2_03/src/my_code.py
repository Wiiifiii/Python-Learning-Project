# -*- coding: utf-8 -*-

"""
KT3

Tee ohjelma, joka pyytää käyttäjää syöttämään lampotila -nimiseen muuttujaan jonkin mielivaltainen lämpötilan arvon (mieti tyyppi tarkasti kun ensin katsot alla olevaa...). Ohjelman tulee siis hyväksyä esim lämpötila 22.5.

Ohjelma tulostaa sitten seuraavasti, kun lämpötila on:

>39 tulostuu : Liian kuuma
<=39 ja >10 tulostuu : Lämmintä
<=10 ja >=0 tulostuu : Haaleaa
<0 ja >-30 tulostuu : Pakkasta
<=-30 tulostuu : Liian kylmää

Toteuta ohjelma if-elif-else -rakenteella.

Ole tarkka, että tulostat juuri sen tekstin, jota pyydettiin!
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
