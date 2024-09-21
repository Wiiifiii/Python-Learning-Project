# -*- coding: utf-8 -*-
"""
#KT 3
Tee ohjelma, joka laskee mäkihyppääjän yhden kierroksen suorituspisteet. Ensin ohjelma kysyy hypyn pituuden
(liukuluku 0.5 metrin välein) jonka jälkeen se kysyy viiden arvostelutuomarin tyylipisteet 
(0-20 välillä 0.5 välein eli esim. 16.5 tai 17.0 tai 18.5). Hyppääjän pisteet muodostuvat kaavasta.

pisteet = (hypyn pituus - kriittinen piste) * 1.8 + kolmen keskimmäisen tuomarin tyylipisteet + 60. 
Tyylipisteissä siis parhain ja huonoin pistemäärä tipahtaa pois.
Ohjelman hyppyrimäen kriittinen piste on 90 metrin kohdalla. Laita kriittinen piste globaaliin vakioon KR_PISTE. 
Tulosta lopuksi hypyn pituus ja hypyn pisteet. Käytä ohjelmassa funktioita:

KysyHypynPituus - Kysyy hypyn pituuden ja palauttaa sen reaalilukuna
KysyTuomareidenPisteet - Kysyy tuomareiden pisteet yksi kerrallaan. Palauttaa listan jossa on kunkin tuomarin antamat pisteet reaalilukuina. 
LaskeHypynPisteet - Saa ensimmäisenä parametrina hypyn pituuden sekä toisena parametrina listan 
joka sisältää kaikkien tuomareiden antamat tyylipisteet. Palauttaa hypyn pisteet lukuna.

#TASK 3
Create a program that calculates the performance score of a ski jumper for one round. First, the program asks for the jump distance 
(a floating-point number in 0.5 meter intervals), then asks for the style points from five judges 
(0-20 points in 0.5 intervals, e.g., 16.5, 17.0, 18.5). The jumper’s score is calculated using the following formula:
points = (jump distance - critical point) * 1.8 + the three middle judges' style points + 60

In the style points, the highest and lowest points are dropped.

The critical point of the ski jump is at 90 meters. Assign this value to a global constant KR_PISTE. At the end, print the jump distance and the calculated points. Use functions in the program as described below:

    KysyHypynPituus - Asks for the jump distance and returns it as a floating-point number.
    KysyTuomareidenPisteet - Asks for the style points from the judges one by one. Returns a list containing the style points as floating-point numbers.
    LaskeHypynPisteet - Takes the jump distance as the first parameter and a list of the judges' style points as the second parameter. 
    Returns the calculated jump score as a number.
"""
# Define the global critical point constant
KR_PISTE = 90

# Function to ask the user for the jump length
def KysyHypynPituus():
    while True:
        try:
            pituus = float(input("Anna hypyn pituus (metreinä, 0.5 välein): "))
            if pituus % 0.5 == 0:  # Ensure the length is in 0.5 intervals
                return pituus
            else:
                print("Hypyn pituuden pitää olla 0.5 metrin välein.")
        except ValueError:
            print("Virheellinen syöte! Syötä liukuluku.")

# Function to ask for the judges' scores
def KysyTuomareidenPisteet():
    tuomareiden_pisteet = []
    
    for i in range(5):
        while True:
            try:
                pisteet = float(input(f"Anna tuomarin {i+1} antamat pisteet (0-20, 0.5 välein): "))
                if 0 <= pisteet <= 20 and pisteet % 0.5 == 0:
                    tuomareiden_pisteet.append(pisteet)
                    break
                else:
                    print("Pisteiden pitää olla välillä 0-20 ja 0.5 välein.")
            except ValueError:
                print("Virheellinen syöte! Syötä liukuluku.")
    
    return tuomareiden_pisteet

# Function to calculate the jump score
def LaskeHypynPisteet(hypyn_pituus, tuomareiden_pisteet):
    # Sort the scores and remove the highest and lowest
    tuomareiden_pisteet.sort()
    kolmen_keskimmaisen_pisteet = sum(tuomareiden_pisteet[1:4])  # Sum of the 3 middle scores

    # Calculate the jump score using the formula
    pisteet = (hypyn_pituus - KR_PISTE) * 1.8 + kolmen_keskimmaisen_pisteet + 60
    return pisteet

# Main program
if __name__ == "__main__":
    # Ask for the jump length
    hypyn_pituus = KysyHypynPituus()

    # Ask for the judges' scores
    tuomareiden_pisteet = KysyTuomareidenPisteet()

    # Calculate the final score
    hypyn_pisteet = LaskeHypynPisteet(hypyn_pituus, tuomareiden_pisteet)

    # Print the results
    print(f"Hypyn pituus: {hypyn_pituus} m")
    print(f"Hypyn pisteet: {hypyn_pisteet:.1f}")
