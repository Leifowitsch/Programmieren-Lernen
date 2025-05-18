import os
import shutil
ordner = r"D:\Bilder und Videos für Davinic"
datein = os.listdir(ordner)


def main():
    for datei in datein:
        if os.path.isfile(os.path.join(ordner, datei)):
            endung = datei.split(".")[-1].lower()
            zielordner = os.path.join(ordner, endung)
            os.makedirs(zielordner, exist_ok=True)
            shutil.move(
                os.path.join(ordner, datei),
                os.path.join(zielordner, datei)

            )







if __name__ == "__main__":
    main()