import os
import shutil
from os import write
import tkinter as tk


def main():
    while True:
        print("Anzeigen".ljust(15) + "(1)")
        print("Hinzufügen".ljust(15) + "(2)")
        print("Abhaken".ljust(15) + "(3)")
        print("Exit".ljust(15) + "(4)")

        wahl = input("Was möchtest du machen?: ")
        match wahl:
            case ("1"):
                Anzeigen()
            case ("2"):
                Hinzufügen()
            case ("3"):
                Abhaken()
            case ("4"):
                break
            case _:
                print("Gib NUR eine Zahl von 1 bis 4 an: ")


def Anzeigen():
    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            print(f"{index}. {line.strip()}")

def Hinzufügen():
    To_Do = input("Was möchtest du hinzufügen?: ")
    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "a", encoding="utf-8") as file:
        file.writelines(To_Do + "\n")

def Abhaken():
    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for index, zeilen in enumerate(lines, start=1):
        print(f"{index}.  {zeilen.strip()} ")

    try:
        print(lines)
        task = int(input("Welche Aufagbe möchtest du Abhaken? gib bitte die Nummer an!: "))
        if 1 <= task <= len(lines):
            zeile = lines[task - 1].strip()
            print(zeile)
            if not lines[task - 1].strip().endswith("✓"):
                lines[task -1] = zeile + " ✓\n"
            else:
                lines[task - 1].removesuffix(" ✓")

        else:
            print("Ungültige Nummer!")
            return
    except ValueError:
        print("Gib eine Richtige Zahl an")
        return

    with open(r"C:\Users\lepuc\Desktop\ToDoList.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)

    print("Aufgabe Abgehakt")



if __name__ == "__main__":
    main()