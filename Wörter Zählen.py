from collections import Counter

def main():
    loop = True
    while loop:
        satz = input("Gib ein Satz ein: ")
        ohneleer = satz.replace(" ","")
        wörter = satz.split()
        clean = satz.lower().replace(" ","")
        buchstaben = Counter(clean)
        top3 = buchstaben.most_common(3)
        print(f"Dein Satz hat {len(wörter)} Wörter und {len(ohneleer)} Buchstaben")
        print(f"Die 3 häufigsten Buchstaben sind: ")
        for buchstabe, anzahl in top3:
            print(f"{buchstabe}: {anzahl}")
        nochmal = input("Nochmal? y/n: ").lower()
        match nochmal:
            case ("y"):
                continue
            case _:
                break

if __name__ == "__main__":
    main()