
liste = []

#with open("test1.txt", "a") as file:
 #   file.write("Das hier: " + input("Schreibe gerne etwas: ") + "\n")
with open("test1.txt", "r") as file:
    zeilen = file.readlines()
print(zeilen)

for zeile in zeilen:
    print(zeile if zeile == 0 else "Hallo")


with open("test1.txt", "r") as file:
    for zeichen in file:
        info = zeichen.strip()
        if info == 'Das hier:':
            break
        else:
            info = zeichen.strip().split()
            liste.append(info)

print(liste)