# -*- coding: utf-8 -*-
"""
#KT 6
Kysy käyttäjältä mitä hän haluaa seuraavista vaihtoehdoista (eli käyttäjä syöttää joko numeron 0, 1, 2 tai 3) :

   0 = Lopetus
   1 = Anna säde
   2 = Laske ympyrän piiri
   3 = Laske ympyrän pinta-ala

   Anna valintasi:

Tulosta kysymys edellä kuvatulla tavalla.

Muu kuin 0,1,2,3 vastaa nollaa eli päättää ohjelman toiminnan.

Vaihtoehto 0 päättää ohjelman

Vaihtoehto 1 kysyy ympyrän säteen.  Säteen oletusarvo on nolla (0.0)

Vaihtoehto 2 tulostaa ympyrän piirin (laskukaava on piiri = 2 * pii * säde)

Vaihtoehto 3 tulostaa ympyrän alan (laskukaava on  ala = pii * sade * sade) pinta-ala ja tulosta se.

Jos vaihtoehto on ollut 1,2,3, niin toimenpiteiden (syöttö/tulostus) jälkeen tulostetaan edellä kuvattu  vaihtoehtokysymys uudelleen

Hae piin arvo math moduulista (koodin alkuun import math ja sen jälkeen pii saadaan  math.pi muuttujasta)

Tulosta kaikki desimaaliluvut kahden desimalin tarkkuudella.

Esimerkkiajo ohessa

0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 1
Anna säde: 12


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 2
Piiri on 75.40


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 3
Ala on 452.39


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 0

#TASK 6
Ask the user what they want to do from the following options (the user inputs either 0, 1, 2, or 3):

0 = Exit 1 = Enter radius 2 = Calculate circle circumference 3 = Calculate circle area

"Enter your choice:"

Print the question as described above.

Any input other than 0, 1, 2, or 3 is treated as 0, which will terminate the program.

Option 0 exits the program.

Option 1 asks for the circle's radius. The default radius value is zero (0.0).

Option 2 prints the circumference of the circle (the formula is: circumference = 2 * pi * radius).

Option 3 prints the area of the circle (the formula is: area = pi * radius * radius).

If the user selects 1, 2, or 3, the program performs the corresponding action (input/output) and then asks the user for their choice again.

The value of pi is obtained from the math module (use import math at the top of the code and retrieve pi with math.pi).

Print all floating-point numbers with two decimal places.

Sample run:
0 = Exit
1 = Enter radius
2 = Calculate circle circumference
3 = Calculate circle area
Enter your choice: 1
Enter radius: 12


0 = Exit
1 = Enter radius
2 = Calculate circle circumference
3 = Calculate circle area
Enter your choice: 2
The circumference is 75.40


0 = Exit
1 = Enter radius
2 = Calculate circle circumference
3 = Calculate circle area
Enter your choice: 3
The area is 452.39


0 = Exit
1 = Enter radius
2 = Calculate circle circumference
3 = Calculate circle area
Enter your choice: 0

   
"""

import math

# Initialize the radius variable with a default value of 0.0
sade = 0.0

# Function to display the menu
def tulosta_valinnat():
    print("0 = Lopetus")
    print("1 = Anna säde")
    print("2 = Laske ympyrän piiri")
    print("3 = Laske ympyrän pinta-ala")
    print("Anna valintasi:", end=" ")

# Start an infinite loop to process user input until the user decides to quit
while True:
    # Display the options
    tulosta_valinnat()
    
    # Read the user's choice
    valinta = int(input())
    
    # Check the user's choice and perform the appropriate action
    if valinta == 0:
        # Exit the program
        print("Ohjelma lopetettu.")
        break
    elif valinta == 1:
        # Ask for the radius
        sade = float(input("Anna säde: "))
    elif valinta == 2:
        # Calculate and print the circumference
        piiri = 2 * math.pi * sade
        print(f"Piiri on {piiri:.2f}")
    elif valinta == 3:
        # Calculate and print the area
        ala = math.pi * sade * sade
        print(f"Ala on {ala:.2f}")
    else:
        # Invalid choice, exit the program
        print("Ohjelma lopetettu.")
        break




