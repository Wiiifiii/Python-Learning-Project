"""
#KT 2
Esittele muuttujat etunimi (enimi, "??"), sukunimi (snimi, "??") ja kokonimi (knimi, "?? ??") ja
laita niille oletusarvot. Muuttujanimet ja oletusarvot annettu suluissa. Tulosta kokonimi, jolloin pitäisi tulostua aluksi "?? ??".
Lue käyttäjältä etunimi ja sukunimi ja yhdistä nämä kokonimi-muuttujaan.
Tulosta nimi näytölle kokonimi-muuttujasta. Alla esimerkki ohjelmasta:
?? ??
Anna etunimi : Jussi
Anna sukunimi : Juonio
Nimesi on Jussi Juonio

#TASK 2

Introduce variables first_name (enimi, "??"), last_name (snimi, "??"), and full_name (knimi, "?? ??") and
give them default values. The variable names and default values are provided in parentheses. Print full_name, 
so it should initially print "?? ??". Then, ask the user for their first name and last name, and combine these 
into the full_name variable. Finally, print the name from the full_name variable. Below is an example of the program:

?? ??
Enter your first name: Jussi
Enter your last name: Juonio
Your name is Jussi Juonio
"""

# Define the variables with the default values
enimi = "??"  # First name
snimi = "??"  # Last name
knimi = enimi + " " + snimi  # Full name as a combination of first and last name

# Print the default full name
print(knimi)

# Ask the user for their first name and last name
enimi = input("Anna etunimi: ")  # Read first name from user
snimi = input("Anna sukunimi: ")  # Read last name from user

# Update the full name with the user's input
knimi = enimi + " " + snimi

# Print the updated full name
print(f"Nimesi on {knimi}")

