import math
from operator import index
# x = Zeile in welcher Kontostand ist

def main():
    Datei = []
    stand = 0
    with open("finanzen.txt", "r") as file:
        for line in file:
            Stand = line.strip().split("=")
            Datei.append(Stand)



    while True:




        def Einnahmen(stand, Datei):
            for x, Zeilen in enumerate(Datei):
                for Wörter in Zeilen:
                    if "Einnahmen" in Wörter:
                        print()
                        Datei[x][1] = float(Datei[x][1])
                        Datei[x][1] += float(input("Was sind deine zusätlichen Einnahmen?: "))
                        Datei[x][1] = str(Datei[x][1])
                        with open("finanzen.txt", "w") as file:
                            for zeile,zeichen in enumerate(Datei):
                                file.writelines(f"{Datei[zeile][0]}={Datei[zeile][1]}\n")
                        print(f"Deine Einnahmen sind jetzt: {Datei[x][1]}€")
                        return {Datei[x][1]}



            pass


        def Ausgaben():
            for x, liste in enumerate(Datei):
                for Wort in liste:
                    if "Ausgaben" in Wort:
                        print()
                        Datei[x][1] = float(Datei[x][1])
                        Datei[x][1] += float(input("Was sind deine zusätlichen Ausgaben?: "))
                        Datei[x][1] = str(Datei[x][1])
                        print(f"{Datei[x][1]}€")
                        with open("finanzen.txt", "w") as file:
                            for zeile,zeichen in enumerate(Datei):
                                file.writelines(f"{Datei[zeile][0]}={Datei[zeile][1]}\n")
                        print(f"Deine Ausgaben sind jetzt: {Datei[x][1]}€")
                        return {Datei[x][1]}
            pass


        def Kontostand(Datei):
            for x, Zeilen in enumerate(Datei):
                for Zeile in Zeilen:
                    if "Kontostand" in Zeile:
                        print()
                        Datei[x][1] = float(Datei[x][1])
                        Datei[x][1] += float(input("Wieviel möchtest du Aufladen?: "))
                        Datei[x][1] = str(Datei[x][1])
                        print(f"{Datei[x][1]}€")
                        with open("finanzen.txt", "w") as file:
                            for zeile, zeichen in enumerate(Datei):
                                file.writelines(f"{Datei[zeile][0]}={Datei[zeile][1]}\n")
                        print(f"Dein Kontostand ist jetzt: {Datei[x][1]}€")
                        return {Datei[x][1]}





        def Zeiteinheit():
            for x, Zeilen in enumerate(Datei):
                for Wörter in Zeilen:
                    if "Einnahmen" in Wörter:
                        einnahmen = Datei[x][1]
                    else:
                        pass

            for x, Zeilen in enumerate(Datei):
                for Wörter in Zeilen:
                    if "Ausgaben" in Wörter:
                        ausgaben = Datei[x][1]
                    else:
                        pass

            for x, Zeilen in enumerate(Datei):
                for Wörter in Zeilen:
                    if "Kontostand" in Wörter:
                        kontostand = Datei[x][1]
                    else:
                        pass
            eingabe = str(input("Tage(1), Woche(2), Monat(3), Jahr(4)"))
            match eingabe:
                case ("1"):
                    Tage = float(input("Wieviel Tage?: "))
                    ergebnis = kontostand + (einnahmen - ausgaben) * (Tage / 30)
                    print("--------------------------------------")
                    print(f"Dein Kontostand berträgt in {Tage} Tagen {ergebnis}€")
                    print(f"Dein Umsatz berträgt in {Tage} Tagen {ergebnis}€")
                    print("--------------------------------------")

                case ("2"):
                    Wochen = float(input("Wieviel Tage?: "))
                    ergebnis = kontostand + (einnahmen - ausgaben) * (Wochen / 4.5)
                    print("--------------------------------------")
                    print(f"Dein Kontostand berträgt in {Wochen} Tagen {ergebnis}€")
                    print(f"Dein Umsatz berträgt in {Wochen} Tagen {ergebnis}€")
                    print("--------------------------------------")
                case ("3"):
                    Monate = float(input("Wieviel Tage?: "))
                    ergebnis = kontostand + (einnahmen - ausgaben) * Monate
                    print("--------------------------------------")
                    print(f"Dein Kontostand berträgt in {Monate} Tagen {ergebnis}€")
                    print(f"Dein Umsatz berträgt in {Monate} Tagen {ergebnis}€")
                    print("--------------------------------------")

                case ("4"):
                    Jahre = float(input("Wieviel Tage?: "))
                    ergebnis = kontostand + (einnahmen - ausgaben) * (Jahre * 12)
                    print("--------------------------------------")
                    print(f"Dein Kontostand berträgt in {Jahre} Tagen {ergebnis}€")
                    print(f"Dein Umsatz berträgt in {Jahre} Tagen {ergebnis}€")
                    print("--------------------------------------")



        print("-------------------")
        print("\n".join([f"{key} = {value}" for key, value in Datei]))
        print("-------------------")


        eingabe = input("Einnahmen(1), Ausgaben(2), Kontostand(3), Zeiteinheit(4), Exit(5): ")
        match eingabe:
            case("1"):
                einnahmen = Einnahmen(stand, Datei)
            case("2"):
                ausgaben = Ausgaben()
            case("3"):
                kontostand = Kontostand(Datei)
            case("4"):
                Zeiteinheit()
            case("5"):
                break





if __name__ == "__main__":
    main()