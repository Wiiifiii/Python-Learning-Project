# -*- coding: utf-8 -*-
"""
#KT 4

Kirjoita funktio Tsekkaus, joka tulostaa ensin tiedon siitä, kuinka monta parametria funktioon tuli. 
Eli parametrien määrää ei ole rajattu. Jos ensimmäisen parametri oli "opettaja" niin funktio tulosta 
seuraavalle riville "Koita saada oppilaat oppimaan", jos se taas oli "opiskelija", niin funktio tulostaa 
"Koita opiskella ahkerasti". Jos parametri oli jotain muuta, niin funktio tulostaa "En ymmarra". 
Jos parametreja ei ole yhtään, niin funktio tulostaa "Virhe".

#TASK 4

Write a function called Tsekkaus, which first prints information about how many parameters the function received. The number of parameters is not limited.

    If the first parameter was "opettaja" (teacher), the function prints on the next line "Koita saada oppilaat oppimaan" (Try to get the students to learn).
    If the first parameter was "opiskelija" (student), the function prints "Koita opiskella ahkerasti" (Try to study diligently).
    If the parameter was something else, the function prints "En ymmarra" (I don't understand).
    If no parameters were passed at all, the function prints "Virhe" (Error).
"""
# Define the Tsekkaus function
def Tsekkaus(*args):
    # Print the number of parameters
    print(len(args))

    # Check if no parameters were passed
    if len(args) == 0:
        print("Virhe")
    else:
        # Check the first parameter and respond accordingly
        if args[0] == "opettaja":
            print("Koita saada oppilaat oppimaan")
        elif args[0] == "opiskelija":
            print("Koita opiskella ahkerasti")
        else:
            print("En ymmarra")

# Main program for testing
if __name__ == "__main__":
    # Example calls to demonstrate
    Tsekkaus("opettaja", "testi1", "testi2")
    Tsekkaus("opiskelija")
    Tsekkaus("random")
    Tsekkaus()
