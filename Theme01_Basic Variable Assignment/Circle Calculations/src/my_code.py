
"""
#KT 5
Esittele muuttuja pii, jolle annat alkuarvoksi piin likiarvon 6 desimaalin tarkkuudella.
Lue käyttäjältä ympyrän halkaisija ja tulosta ympyrän piiri ja pinta-ala kahden desimaalin tarkkuudella

Malli ohessa:

Anna ympyrän halkaisija: 12
Piiri on 37.70
Pinta-ala on 113.10

#TASK 5
Declare a variable pii, and assign it the approximate value of pi with an accuracy of 6 decimal places. 
Ask the user for the diameter of a circle, then calculate and print the circumference and area of the circle with two decimal places.

Example:
Enter the diameter of the circle: 12
The circumference is 37.70
The area is 113.10

"""


# Define the variable 'pii' with a value of pi to 6 decimal places
pii = 3.141593

# Ask the user for the diameter of the circle
halkaisija = float(input("Anna ympyrän halkaisija: "))

# Calculate the radius of the circle
sade = halkaisija / 2

# Calculate the circumference and area of the circle
piiri = 2 * pii * sade
pinta_ala = pii * (sade ** 2)

# Print the circumference and area with two decimal places
print(f"Piiri on {piiri:.2f}")
print(f"Pinta-ala on {pinta_ala:.2f}")
