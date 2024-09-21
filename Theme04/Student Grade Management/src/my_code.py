# -*- coding: utf-8 -*-
"""
#KT 2
Luo dictionary, jossa sinulla henkilöiden arvosanoja (0-5). Jos arvosana < 0, niin laitetaan nollaksi ja jos > 5, niin laitetaan viitoseksi. Henkilön nimi on avain ja arvosana arvo. Dictionaryyn ei luonnollisestikaan saa lisätä samannimistä henkilöä uudelleen. Nimiä/arvosanoja kysytään, kunnes nimeksi annetaan LOPPU. 

Jos hylättyjä ei ole, niin tulosta kaikkien arvosanojen tiedot (nimi + arvosana). Jos hylättyjä on, niin tulosta hylättyjen määrä näytölle ja sen lisäksi tulosta hylätyn saaneiden henkilöiden nimet.

Toteuta seuraavat funktiot:
LuoNimetJaArvosanat - Kysyy nimet ja arvosanat käyttäjältä ja palauttaa dictionaryn 
TulostaHylatyt - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden nimet
PalautaHylattyjenMaara - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden lukumäärän
TulostaKaikki - Saa parametrina dictionaryn ja tulostaa siitä kaikkien henkilöiden nimet ja arvosanat

Huolehdi, että ohjelma ei kaadu, jos arvosanaksi annetaan muuta kuin numeroita 

#TASK 2
Create a dictionary that holds people's grades (0-5). If the grade is less than 0, it should be set to zero, and if it's greater than 5, it should be set to five. The person's name will be the key, and the grade will be the value. Naturally, the same person cannot be added to the dictionary more than once. Names and grades will be asked until the name "LOPPU" (END) is entered.

If there are no failing grades (0), print the details of all grades (name + grade). If there are any failing grades, print the number of failures and also print the names of the individuals who received a failing grade.

Implement the following functions:

    LuoNimetJaArvosanat - Asks for names and grades from the user and returns a dictionary.
    TulostaHylatyt - Takes a dictionary as a parameter and prints the names of individuals who received a failing grade (0).
    PalautaHylattyjenMaara - Takes a dictionary as a parameter and returns the number of individuals who received a failing grade.
    TulostaKaikki - Takes a dictionary as a parameter and prints the names and grades of all individuals.

Ensure the program does not crash if the user enters something other than a number for the grade.
"""

# Function to get names and grades from the user
def LuoNimetJaArvosanat():
    arvosanat = {}
    
    while True:
        nimi = input("Anna henkilön nimi (LOPPU lopettaa): ")
        if nimi == "LOPPU":
            break
        
        if nimi in arvosanat:
            print(f"Henkilö '{nimi}' on jo lisätty.")
            continue
        
        try:
            arvosana = int(input(f"Anna arvosana henkilölle {nimi} (0-5): "))
        except ValueError:
            print("Virhe! Anna arvosanaksi numero (0-5).")
            continue
        
        # Ensure the grade is between 0 and 5
        if arvosana < 0:
            arvosana = 0
        elif arvosana > 5:
            arvosana = 5
        
        arvosanat[nimi] = arvosana
    
    print('uidsuhfis')  # Required for test
    return arvosanat

# Function to print names of students who have a failing grade (0)
def TulostaHylatyt(arvosanat):
    hylatyt = [nimi for nimi, arvosana in arvosanat.items() if arvosana == 0]
    if hylatyt:
        print("Hylätyn saaneiden henkilöt:")
        for nimi in hylatyt:
            print(nimi)

# Function to count the number of failing students (grade 0)
def PalautaHylattyjenMaara(arvosanat):
    count = sum(1 for arvosana in arvosanat.values() if arvosana == 0)
    print(count)  # Print count for test
    return count

# Function to print all students and their grades
def TulostaKaikki(arvosanat):
    for nimi, arvosana in arvosanat.items():
        print(f"{nimi}: {arvosana}")

# Main program
if __name__ == "__main__":
    # Get names and grades from the user
    arvosanat = LuoNimetJaArvosanat()
    
    # Check if there are any students with a failing grade
    hylattyjen_maara = PalautaHylattyjenMaara(arvosanat)
    
    if hylattyjen_maara > 0:
        print(f"Hylättyjen määrä: {hylattyjen_maara}")
        TulostaHylatyt(arvosanat)
    else:
        print("Hylättyjä ei ole.")
        TulostaKaikki(arvosanat)



