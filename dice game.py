import math

def show_balance(balance):
    print(f"|Dein Balance ist {balance:.2f}€|")

def deposit(balance):
    while True:
        Betrag = float(input("Wieviel möchtest du aufladen?: "))
        if Betrag <= 0:
            print("Dein Aufladebetrag muss über Null sein")
        else:
            break
    return Betrag

def withdraw(balance):
    while True:
        Betrag = float(input("Wieviel möchtest du Abheben?: "))
        if Betrag < 0:
            print("Dein Abhebebetrag muss über Null sein")
        elif Betrag > balance:
            print(F'Dein Betrag:"{Betrag:.2f}€" darf nicht über deinem Balance:"{balance:.2f}€" liegen')
        else:
            break
    return Betrag


def main():
    balance = 0
    is_running = True
    while is_running:
        print("-----------------------")
        print("     Bank Programm")
        print("-----------------------")
        print("1. Balance Anzeigen")
        print("2. Geld Aufladen")
        print("3. Geld Abheben")
        print("4. Programm Beenden")
        print("-----------------------")
        entscheidung = input("1 / 2 / 3 / 4?: ")
        print("-----------------------")
        if entscheidung == "1":
            show_balance(balance)
        elif entscheidung == '2':
            balance += deposit(balance)
            print(f"|Dein neuer Betrag ist: {balance:.2f}€|")
        elif entscheidung == "3":
            balance -= withdraw(balance)
            print(f"|Dein neuer Betrag ist: {balance:.2f}€|")
        elif entscheidung == "4":
            is_running = False
        else:
            print(f"Dein Input '{entscheidung}' ist nicht valide")
    print("Danke für deinen Besuch, hab noch nen schönen Tag :)")



if __name__ == '__main__':
    main()
