import os
import shutil
from os import write
import tkinter as tk


def main():
    fenster = tk.Tk()
    ausgabe = tk.Label(fenster, text=Anzeigen(), font=("Courier", 12), fg="navy", anchor="w", justify="left")
    ausgabe2 = tk.Label(fenster, text="", font=("Courier", 12), fg="red", anchor="w", justify="left")
    fenster.title("To Do Liste :)")
    tk.Label(fenster, text="Füge To Do hinzu!:", font=("Courier", 12), anchor="w", justify="left").pack()
    entry = tk.Entry(fenster)
    entry2 = tk.Entry(fenster)
    entry.pack()
    tk.Button(fenster, text="Hinzufügen", command=lambda: Hinzufügen(entry, ausgabe), anchor="w", justify="left").pack(pady=5)
    tk.Label(fenster, text="To Do´s:",font=("Courier", 15), anchor="w", justify="left").pack()
    ausgabe.pack()
    tk.Label(fenster, text="Welche Nummer möchtest du abhaken?", anchor="w", justify="left").pack()
    entry2.pack()
    tk.Button(fenster, text="Abhaken", command=lambda: Abhaken(entry2, ausgabe2, ausgabe), anchor="w", justify="left").pack(pady=5)
    tk.Button(fenster, text="Aufräumen", command=lambda: Löschen(ausgabe), anchor="w", justify="left").pack(pady=5)
    ausgabe2.pack()
    fenster.mainloop()


def Anzeigen():
    liste = []
    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            liste1 = f"{index}. {line.strip()}\n"
            liste.append(liste1)
    liste = "".join(liste)
    return liste

def Refresh(ausgabe):
    liste = []
    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            liste1 = f"{index}. {line.strip()}\n"
            liste.append(liste1)
    liste = "".join(liste)
    ausgabe.config(text=liste)
    return ausgabe

def Hinzufügen(entry, ausgabe):
    To_Do = entry.get()
    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "a", encoding="utf-8") as file:
        file.writelines(To_Do + "\n")
    Refresh(ausgabe)

def Abhaken(entry2, ausgabe2, ausgabe):
    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    try:
        task = int(entry2.get())
        if 1 <= task <= len(lines):
            zeile = lines[task - 1].strip()
            if not lines[task - 1].strip().endswith("✓"):
                lines[task -1] = zeile + " ✓\n"
            else:
                lines[task - 1].removesuffix(" ✓")

        else:
            ausgabe2.config(text="Eine Gültige Zahl!!")
            return
    except ValueError:
        ausgabe2.config(text="Eine Gültige Zahl!")
        return

    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)

    Refresh(ausgabe)

    ausgabe2.config(text="Aufgabe Abgehakt! :)")

def Löschen(ausgabe):
    liste= []
    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "r", encoding="utf-8") as file:
        for zeile in file:
            if zeile.strip().endswith("✓"):
                zeile = ""
            liste.append(zeile)
    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "w", encoding="utf-8") as file:
        file.writelines(liste)

    Refresh(ausgabe)



if __name__ == "__main__":
    main()