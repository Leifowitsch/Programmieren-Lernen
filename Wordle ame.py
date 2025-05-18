import random
from random import shuffle

import emoji
# print(help(random))
def shufflee(symbole):
    shuffle(symbole)
    return symbole


def display(symbole,roll):
    for index, symbol in enumerate(symbole):
        if index > 2:
            pass
        else:
            roll.append(symbol)
            print(symbol, end="|")


def balance(balance_current,roll,bet):
    enumerate(roll)
    if roll[0] == roll[1] and roll[0] == roll[2]:
        balance_current += (bet * 10)
        print("----------------")
        print(f"HURRA GEWONNEN!")
        print("----------------")
        print(f"DU HAST {bet * 10}€ GEWONNEN")
        print(f"DEIN KONOTOSTAND IST JETZT {balance_current:.2f}€")
        print("----------------")
        return balance_current
    elif roll[0] == roll[1] or roll[0] == roll[2] or roll[1] == roll[2]:
        balance_current += bet
        print("----------------")
        print(f"HURRA GEWONNEN!")
        print("----------------")
        print(f"DU HAST {bet}€ GEWONNEN")
        print(f"DEIN KONOTOSTAND IST JETZT {balance_current:.2f}€")
        print("----------------")
        return balance_current
    else:
        balance_current -= bet
        print("-------------------")
        print("LEIDER VERLOREN! :(")
        print("-------------------")
        print(f"DEIN KONOTOSTAND IST JETZT {balance_current:.2f}€")
        print("----------------")
        return balance_current
def main():
    print("--------------------------")
    print("WILLKOMMEN BEI DEN SPIELEN")
    print("--------------------------")

    symbole = ["🔥","🔥","🔥",
               "🍉","🍉","🍉",
               "⭐","⭐","⭐",
               "🎱","🎱","🎱",
               "🍋","🍋","🍋",]
    roll = []
    balance_current = 50
    while True:

        roll = []
        bet = input(f"Wie viel möchtest du Wetten? Dein Kontostand ist {balance_current:.2f}€: ")
        if not bet.isdigit():
            print(f'"{bet}" ist nicht Valide')
            continue
        bet = float(bet)

        if bet > balance_current:
            print(f"Du hast zu wenig Guthaben! {balance_current:.2f}€")
            continue

        if bet <= 0:
            print("Wette muss größer als Null sein!")
            continue

        symbole = shufflee(symbole)  # Symbole werden Zufällig angeordnet
        display(symbole,roll)  # Symbole werden angezeigt (die ersten 3)
        print()
        balance_current = balance(balance_current,roll,bet)
        if balance_current == 0:
            break
        wiederholen = input("Noch eine Runde? Y/N: ").lower()
        if wiederholen == "n":
            break
        elif wiederholen == "y":
            pass
        else:
            print(f'Dein Eingabe "{wiederholen}" ist nicht Valide ')
    print()
    print("------------------------------------")
    print("DU HAST LEIDER KEIN GUTHABEN MEHR :(")
    print("------------------------------------")

if __name__ == "__main__":
    main()