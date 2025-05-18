import math
import random
from words import words

words = words

#dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}



def display_man(wrong_guesses):


    print("****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************")


def display_hint(versuch, word, guess, richtige_buchstaben,alle_richtigen_versuche):
    for index, buchstabe in enumerate(word):
        if buchstabe.lower() == guess:
            richtige_buchstaben.append(index)
            alle_richtigen_versuche.append(guess)
    for index in richtige_buchstaben:
        versuch[index] = guess

def dispplay_answer(word,versuch,wrong_guesses,länge):
    if word.lower() == "".join(versuch):
        print("Geschafft!")
        y = input("Nochmal? y/n: ")
        if y == "y":
            wrong_guesses = 0
        elif y == "n":
            nochmal = "n"

    else:
        pass

def main():
    word = random.choice(words)
    länge = len(word)
    guesses = []
    wrong_guesses = 0
    versuch =[]
    alle_richtigen_versuche = []
    for zahl in range(länge):
        versuch.append("-")
    while True:
        nochmal = "y"
        if nochmal == "n":
            break
        word = random.choice(words)
        länge = len(word)
        guesses = []
        wrong_guesses = 0
        versuch = []
        alle_richtigen_versuche = []
        for zahl in range(länge):
            versuch.append("-")
        while True:
            if nochmal == "n":
                break
            if wrong_guesses == 6:
                print(f'Leider Verloren :( Das wort war: "{word} ')
                nochmal = input("Noch eine Runde? y/n: ").lower()
                if nochmal == "n":
                    break
                elif nochmal == "y":
                    wrong_guesses = 0
                    continue
                else:
                    print(f'Eingabe "{nochmal}" ist nicht Valide')
                    continue

            richtige_buchstaben = []
            guess = input("Bitte gib nen Buchstaben ein: ")
            if guess == "1":
                break
            if guess in alle_richtigen_versuche:
                print("Buchstabe wurde bereits versucht!")
                continue
            if guess not in word.lower():
                wrong_guesses += 1
            guesses.append(guess)
            display_man(wrong_guesses)
            display_hint(versuch, word, guess, richtige_buchstaben,alle_richtigen_versuche)
            dispplay_answer(word, versuch,wrong_guesses,länge)
            versuch = "".join(versuch)
            print(versuch)
            print(f'Fehler Nummer: "{wrong_guesses}"')
            versuch = list(versuch)



if __name__ == "__main__":
    main()