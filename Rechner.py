import math

print("Welche rechnungsart? (1) Multiplikation, (2) Addition, (3) Division, (4) Exponential: ")
format = int(input())
if (format == 1):
 abc = float(input("Gib mir eine Zahl bitte: "))
 asd = float(input("Noch eine zahl bitte: "))
 we = abc * asd
 print(f"Dein Ergebniss ist: {we} ")
if (format == 2):
    abc = float(input("Gib mir eine Zahl bitte: "))
    asd = float(input("Noch eine zahl bitte: "))
    we = abc + asd
    print(f"Dein Ergebniss ist: {we} ")
if (format == 3):
    abc = float(input("Gib mir eine Zahl bitte: "))
    asd = float(input("Noch eine zahl bitte: "))
    we = abc / asd
    print(f"Dein Ergebniss ist: {we} ")
if (format == 4):
    abc = float(input("Gib mir eine Zahl bitte: "))
    asd = float(input("einen exponenten: "))
    we = abc ** asd
    print(f"Dein Ergebniss ist: {we} ")