import random

def main():
    zahl = random.randint(0, 100)
    versuch = 0
    loop = True
    while loop:
        try:
            guess = float(input("Gib eine Zahl von 0 bis 100 ein: "))
        except ValueError:
            print("Bitte gib NUR Zahlen ein")
            continue
        if guess > zahl:
            print("Zu Hoch!")
            versuch = versuch + 1
            print(f"Versuch nummer {versuch}")
        elif guess < zahl:
            print("Zu Niedrig!")
            versuch = versuch + 1
            print(f"Versuch nummer {versuch}")
        else:
            print(f"Glückwunsch du hast es geschafft! die Zahl war {zahl}")
            print(f"Du hast {versuch} Versuche gebraucht!")
            weiter = input("Nochmal? y/n: ").lower
            match weiter:
                case("y"):
                    zahl = random.randint(0, 100)
                    versuch = 0
                case _:
                    print("Danke fürs Spielen!")
                    break



if __name__ == "__main__":
    main()