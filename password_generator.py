import random
from classes import all_chars
all_chars = all_chars


def main():
    while True:
        def speichert():
            while True:
                speichern = input("Möchtest du dein Passwort speichern? y/n: ").lower()
                if speichern == "y":

                    with open(r"C:\Users\lepuc\Desktop\passwoerter.txt", "a") as file:
                        file.write(f"{input("Wofür ist das Passwort?: ")}: {passwort}\n")
                    print("Das Passwort wurde erfolgreich gespeichert!")
                    break
                elif speichern == "n":
                    break
                    pass
                else:
                    print(f'"{speichern}" ist keine valide Eingabe')


        def generate(länge):
            for zahl in range(länge):
                passwort.append(random.choice(all_chars))


            pass

        def display(passwort):
            passwort = "".join(passwort)
            print(f'Das ist dein Passwort: {passwort}')
            return passwort

        länge = int(input("Gib an wie Lang das Passwort sein soll: "))
        passwort = []
        generate(länge)
        passwort = display(passwort)
        speichert()
        while True:
            abbrechen = input("Möchtest du noch ein Passwort erstellen? y/n: ").lower()
            if abbrechen == "y":
                break
            elif abbrechen == "n":
                break
            else:
                print(f'"{abbrechen}" ist keine valide Eingabe')
        if abbrechen == "n":
            break



if __name__ == "__main__":
    main()



