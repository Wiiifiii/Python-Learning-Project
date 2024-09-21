# -*- coding: utf-8 -*-
"""
#KT 2

Tee luokka Tilaus, jolla on kolme jäsenmuuttujaa: tilausnumero, tuotekoodi ja maara.
Toteuta lisäksi funktiot hae_tilaukset, talleta_tilaukset sekä tulosta_tilaukset. 
Käytä tiedostonnimenä globaalin muuttujan filename arvoa. 
Käytä talletukseen JSON-formaattia.
Pääohjelma on valmiina, älä muokkaa sitä. Alla esimerkki ohjelman ajosta:
Lisataanko tilaustuote (k/e): k
Tilausnumero: a329847
Tuotekoodi: 22323
Maara: 283
Lisataanko tilaustuote (k/e): k
Tilausnumero: 383838b
Tuotekoodi: 234
Maara: 11
Lisataanko tilaustuote (k/e): e
{'tilausnumero': 'a329847', 'tuotekoodi': '22323', 'maara': 283}
{'tilausnumero': '383838b', 'tuotekoodi': '234', 'maara': 11}


#TASK 2
Create a class Tilaus that has three member variables: tilausnumero (order number), tuotekoodi (product code), and maara (quantity).

Additionally, implement the following functions:

    hae_tilaukset: Reads orders from a file.
    talleta_tilaukset: Saves the orders to a file.
    tulosta_tilaukset: Prints the orders.

Use the global variable filename as the file name, and store the data in JSON format.

The main program is already written; do not modify it. Below is an example of how the program runs:
Lisataanko tilaustuote (k/e): k
Tilausnumero: a329847
Tuotekoodi: 22323
Maara: 283
Lisataanko tilaustuote (k/e): k
Tilausnumero: 383838b
Tuotekoodi: 234
Maara: 11
Lisataanko tilaustuote (k/e): e
{'tilausnumero': 'a329847', 'tuotekoodi': '22323', 'maara': 283}
{'tilausnumero': '383838b', 'tuotekoodi': '234', 'maara': 11}

"""

import json

filename = "./tilaukset.json"

# Define the Tilaus class
class Tilaus:
    def __init__(self, tilausnumero, tuotekoodi, maara):
        self.tilausnumero = tilausnumero
        self.tuotekoodi = tuotekoodi
        self.maara = maara

    def to_dict(self):
        return {
            'tilausnumero': self.tilausnumero,
            'tuotekoodi': self.tuotekoodi,
            'maara': self.maara
        }

# Function to read orders from the JSON file
def hae_tilaukset():
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if the file doesn't exist or is invalid

# Function to save orders to the JSON file
def talleta_tilaukset(tilaukset):
    with open(filename, 'w') as f:
        json.dump(tilaukset, f, indent=4)

# Function to print the orders
def tulosta_tilaukset(tilaukset):
    for tilaus in tilaukset:
        print(tilaus)

if __name__ == '__main__':
    # Read the existing orders from the file
    tilaukset = hae_tilaukset()

    # Continuously ask for new orders until the user says "e"
    while(True):
        vast = input("Lisataanko tilaustuote (k/e): ")
        if vast.lower() != "k":
            break
        tilausnumero = input("Tilausnumero: ")
        tuotekoodi = input("Tuotekoodi: ")
        maara = int(input("Maara: "))
        tilaus = Tilaus(tilausnumero, tuotekoodi, maara)
        tilaukset.append(tilaus.to_dict())

    # Save the updated list of orders to the file
    talleta_tilaukset(tilaukset)

    # Clear the memory and reload from the file
    del tilaukset

    # Read JSON structure and print it
    t_list = hae_tilaukset()
    tulosta_tilaukset(t_list)



