import math

def main():
    loop = True
    while loop:
        print("-------------------------------")
        print("Addition".ljust(15) + "(1)")
        print("Subtraktion".ljust(15) + "(2)")
        print("Multiplikation".ljust(15) + "(3)")
        print("Division".ljust(15) + "(4)")
        print("Beenden".ljust(15) + "(5)")
        print("-------------------------------")
        print("")

        eingabe = str(input("Was möchtest du rechnen?: "))
        match eingabe:
            case("1"):
                operator = "+"
                Zahl1 = get_zahl("Gib eine erste Zahl ein: ")
                Zahl2 = get_zahl("Gib eine zweite Zahl ein: ")
                print(f"Das Ergebnis von {Zahl1} {operator} {Zahl2} = {Zahl1 + Zahl2}")
            case("2"):
                operator = "-"
                Zahl1 = get_zahl("Gib eine erste Zahl ein: ")
                Zahl2 = get_zahl("Gib eine zweite Zahl ein: ")
                print(f"Das Ergebnis von {Zahl1} {operator} {Zahl2} = {Zahl1 - Zahl2}")
            case("3"):
                operator = "*"
                Zahl1 = get_zahl("Gib eine erste Zahl ein: ")
                Zahl2 = get_zahl("Gib eine zweite Zahl ein: ")
                print(f"Das Ergebnis von {Zahl1} {operator} {Zahl2} = {Zahl1 * Zahl2:.5f}")
            case("4"):
                while True:
                    operator = "/"
                    Zahl1 = get_zahl("Gib eine erste Zahl ein: ")
                    Zahl2 = get_zahl("Gib eine zweite Zahl ein: ")
                    if Zahl2 == 0:
                        print("Du Schlingel durch 0 darf man nicht, auch nicht bei mir :)")
                    else:
                        print(f"Das Ergebnis von {Zahl1} {operator} {Zahl2} = {Zahl1 / Zahl2:.5f}")
                        break
            case("5"):
                loop = False
            case _: print("Bitte eine Zahl von 1-5, Dankö")

def get_zahl(text):
    return float(input(text))

if __name__ == "__main__":
    main()