# -*- coding: utf-8 -*-

"""
KT3

Kysy käyttäjältä ensin kieli (Suomi = 0/ Englanti =1). Oletuskieli on suomi, eli muu kuin 0/1 tarkoittaa suomenkielistä tulostusta.
Määrittele koodissa viikonpäivien(ma, ti ke..) tekstit yhteen listaan, jossa on alkio/päivä eli siis molempien kielien viikonpäivänimet (esim Maanatai/Monday].
Kyse on siis rakenteesta lista listassa.

Ota käyttöön muuttuja (dictonary-tyyppinen), johon voit tallentaa maanantain ja perjantain välisenä aikana neljä mittaustulosta
jokaiselta päivältä (mittaustulos on sademäärä milleinä). Lue käyttäjältä nämä mittaustulokset ja
laske vasta lopuksi ja tulosta jokaisen päivän mittaustulosten keskiarvo yhdellä desimaalilla seuraavan esimerkin mukaisesti :

Maanantai:      12.0 mm
Tiistai:        0.0 mm
Keskiviikko:    1.9 mm
Torstai:        22.8 mm
Perjantai:      0.9 mm

Esimerkkiajo ohessa:
Millä kielellä /Please choose language (0 = suomi, 1 = english): 1
Monday 1. : 3
Monday 2. : 2
Monday 3. : 4
... Säästetty tilaa...
Friday 2. : 6
Friday 3. : 5
Friday 4. : 3

Monday 3.5 mm
Tuesday 3.2 mm
Wednesday 4.0 mm
Thursday 4.2 mm
Friday 4.8 mm

Syötteiden järkevyydestä ei tarvitse välittää!

Ole taas huolellinen tulostusten kanssa!

"""

# Define the list of days of the week in both Finnish and English
viikonpaivat = [
    ["Maanantai", "Monday"],
    ["Tiistai", "Tuesday"],
    ["Keskiviikko", "Wednesday"],
    ["Torstai", "Thursday"],
    ["Perjantai", "Friday"]
]

# Dictionary to store rainfall measurements for each day
mittaustulokset = {}

# Ask the user to choose the language
kieli = int(input("Millä kielellä /Please choose language (0 = suomi, 1 = english): "))

# Default to Finnish if any invalid value is provided
if kieli != 0 and kieli != 1:
    kieli = 0  # Default to Finnish

# Loop through each weekday (Monday to Friday)
for paiva in viikonpaivat:
    # List to store the four rainfall measurements for the day
    mittaukset = []
    
    # Ask for 4 rainfall measurements
    for i in range(1, 5):
        mittaus = float(input(f"{paiva[kieli]} {i}. : "))  # Display the day name in the selected language
        mittaukset.append(mittaus)
    
    # Store the rainfall measurements for the day
    mittaustulokset[paiva[kieli]] = mittaukset

# Calculate and print the average rainfall for each day with one decimal place
for paiva in viikonpaivat:
    paivan_mittaukset = mittaustulokset[paiva[kieli]]
    keskiarvo = sum(paivan_mittaukset) / len(paivan_mittaukset)
    print(f"{paiva[kieli]}: {keskiarvo:.1f} mm")
