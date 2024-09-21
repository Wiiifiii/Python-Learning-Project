# -*- coding: utf-8 -*-
"""

KT4

Lue nimi, pituus ja paino em nimisiin muuttujiin. Käytä juuri noita muuttujanimiä.
Esittele lisäksi bmi muuttuja ja alusta se nollaksi. Kysy käyttäjältä nimi, pituus metreinä ja paino kiloina.
Laske painoindeksi bmi muuttujaan seuraavasti:


bmi = paino / pituus ^ 2



Tulosta lopuksi:


Jussi Juonio pituutesi on 1.81 m ja painosi 104.0 kg
Painoindeksisi on siten 31.75

Huomaa, että bmi tulee kahdella desimaalilla

"""

# Initialize the variables
nimi = ""       # Name
pituus = 0.0    # Height in meters
paino = 0.0     # Weight in kilograms
bmi = 0.0       # Body Mass Index, initialized to 0

# Ask the user for their name, height (in meters), and weight (in kilograms)
nimi = input("Anna nimesi: ")                  # Read name from user
pituus = float(input("Anna pituutesi (m): "))   # Read height from user as float
paino = float(input("Anna painosi (kg): "))     # Read weight from user as float

# Calculate the BMI (Body Mass Index)
bmi = paino / (pituus ** 2)

# Print the result with the BMI rounded to two decimal places
print(f"{nimi} pituutesi on {pituus:.2f} m ja painosi {paino:.1f} kg")
print(f"Painoindeksisi on siten {bmi:.2f}")

