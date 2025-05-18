import random
from dbm import error
from classes import all_chars
all_chars = all_chars
import pyperclip
import string
import tkinter as tk

def main():
    fenster = tk.Tk()
    fenster.title("Passwort Generator")
    tk.Label(fenster, text="Passwortlänge:").pack()
    entry = tk.Entry(fenster)
    entry.pack()
    tk.Label(fenster, text="Wofür ist das Passwort?:").pack()
    entry2 = tk.Entry(fenster)
    entry2.pack()
    ausgabe = tk.Label(fenster, text="", font=("Courier", 12), fg="green")
    ausgabe.pack()
    ausgabe2 = tk.Label(fenster, text="", font=("Courier", 12), fg="green")
    ausgabe2.pack(pady=5)
    tk.Button(fenster, text="Generieren", command=lambda: generieren(entry,ausgabe,ausgabe2)).pack(pady=5)
    tk.Button(fenster, text="Kopieren", command=lambda: kopieren(passwort,ausgabe)).pack(pady=5)
    tk.Button(fenster, text="Speichern", command=lambda: speichern(passwort,ausgabe, entry2)).pack(pady=5)
    fenster.mainloop()


def anzeigen(ausgabe):
    with open(r"C:\Users\lepuc\Desktop\passwoerter.txt", "r") as file:
        for line in file:
            ausgabe.config(text=line)


def generieren(entry,ausgabe,ausgabe2):
    global passwort
    passwort = []
    passwort = "".join(random.choice(all_chars) for zahl in range(laenge(entry,ausgabe)))
    ausgabe.config(text=f"Dein Passwort ist {stärke(passwort)}")
    ausgabe2.config(text=f"Das ist dein Passwort: {passwort}")
    return passwort




def kopieren(passwort,ausgabe):
        pyperclip.copy(passwort)
        ausgabe.config(text="In Zwischenablage Kopiert!")


def speichern(passwort,ausgabe,entry2):
    Gebrauch = entry2.get()
    with open(r"C:\Users\lepuc\Desktop\passwoerter.txt", "a") as file:
        file.write(f"{Gebrauch}" + f": {passwort}" + f"\nStaerke: {stärke(passwort)}\n\n" )
        ausgabe.config(text="Dein Passwort wurde erfolgreich gespeichert :)")


def laenge(entry,ausgabe):
        try:
            eingabe = entry.get()
            if eingabe.strip() == "":
                raise ValueError

            if all(zeichen.isdigit() for zeichen in eingabe):
                if int(eingabe) > 0:
                    return int(eingabe)
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            ausgabe.config(text="Gib NUR eine ganze positive Zahl ein")


def stärke(passwort):
    punkte = 0
    if any(zeichen.islower() for zeichen in passwort): punkte += 1
    if any(zeichen.isupper() for zeichen in passwort): punkte += 1
    if any(zeichen.isdigit() for zeichen in passwort): punkte += 1
    if any(zeichen in string.punctuation for zeichen in passwort): punkte += 1
    if len(passwort) >= 12: punkte +=1

    stufen = {
        1: "Sehr Schwach",
        2: "Schwach",
        3: "Okay",
        4: "Stark",
        5: "Sehr Stark"
    }
    return stufen.get(punkte, "Unbewertet")

if __name__ == "__main__":
    main()