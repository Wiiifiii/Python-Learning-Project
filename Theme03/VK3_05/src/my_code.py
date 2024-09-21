# -*- coding: utf-8 -*-
"""
#KT 5
Kirjoita Python-kielinen ohjelma, joka kysyy käyttäjän nimeä, kuitenkin enintään 18 merkkiä.
Merkeissä saa olla tyhjeitä. Jos merkkejä > 18, tulostuu teksti "Virhe!".
Ohjelma tulostaa nimen alla kuvatusti laskevana ja pituudesta riippumatta sivusuunnassa alkaen oikeasta reunasta.
Jotta teksti hahmottuisi riviksi, lisää kaksi välilyöntiä perättäisten merkkien väliin. Kirjoita tämä myös nimi.txt-tiedostoon samassa muodossa.

Esimerkkiajo:
Anna nimesi:Jukka
        a
      k
    k
  u
J

#TASK 5
    Write a Python program that asks the user for their name, but limits the input to a maximum of 18 characters.
    The name may contain spaces. If the number of characters is greater than 18, print "Error!".
    The program should print the name in a descending order starting from the last character. Regardless of the length, the text should align to the right.
    For better visualization, add two spaces between consecutive characters. Also, write this same format to a file named nimi.txt.

Example output:
Enter your name: Jukka
        a
      k
    k
  u
J

"""
# Ask the user for their name
nimi = input("Anna nimesi: ")

# Check if the length of the name exceeds 18 characters
if len(nimi) > 18:
    print("Virhe!")
else:
    # Open the file 'nimi.txt' for writing
    with open("nimi.txt", "w") as file:
        # Iterate through the name in reverse (starting from the last letter)
        for i in range(len(nimi)):
            # Print the character from the last to the first with progressively fewer spaces
            result = ' ' * (2 * (len(nimi) - i - 1)) + nimi[len(nimi) - 1 - i]
            print(result)  # Print to the console
            file.write(result + '\n')  # Write to the file









