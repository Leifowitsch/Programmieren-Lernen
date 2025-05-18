import random

spielen = input("Möchtest du eine Runde spielen? Y/N: ")
while spielen == "Y" or spielen == "y":
    wörterliste = ["Apfel", "Banen", "Stuhl", "Tisch", "Blume", "Vogel", "Karte", "Traum", "Wolke", "Spatz", "Sturm",
                   "Wagen", "Fisch", "Glanz", "Hafen", "Maler", "Leben", "Boden", "Traut", "Fluss", "Mauer", "Brett",
                   "Feder", "Sonne", "Licht", "Wasser", "Blatt", "Stein", "Herz"]
    wort = list("_____")
    wortlösung = random.choice(wörterliste)
    wortlösung = wortlösung.lower()
    Versuch = 0
    while "_" in wort and Versuch < 10:
        buchstabe = input("Bitte gib einen buchstaben ein: ")
        if buchstabe not in wort:
            if buchstabe not in wortlösung:
                Versuch += 1
                wort = "".join(wort)
                print(f"Falscher Buchstabe! Versuch nummer: {Versuch}/10")
                print(wort)
                wort = list(wort)
            for position, buchstabe_wort in enumerate(wortlösung):
                if buchstabe_wort == buchstabe:
                    pos = position
                    pos = int(pos)
                    wort[pos] = buchstabe
                    wort = "".join(wort)
                    print(f"Versuch Nummer {Versuch}/10:  {wort}")
                    wort = list(wort)
        else:
            print(f"Du hast |{buchstabe}| bereits versucht {Versuch}/10")
            wort = "".join(wort)
            print(wort)
            wort = list(wort)

    wort = "".join(wort)
    wort = wort.capitalize()
    if Versuch < 10:
        print(f"HURAA!!Die Lösung ist: {wort}!!!")
    else:
        print(f"Leider nicht geschaft :( das Wort war: {wortlösung}")
    spielen = input("Möchtest du eine Runde spielen? Y/N: ")
print("Programm wurde beendet")


