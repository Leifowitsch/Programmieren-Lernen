

def main():
    punkte = 0
    quiz = [[{"frage": "Was ist die Hauptstadt von Deutschland?",
             "antworten": {"a": "Berlin", "b": "Hamburg", "c": "München"},
             "richtig": "a"}],

            [{"frage": "Was ist 5+7?",
             "antworten": {"a": "23", "b": "12", "c": "11"},
             "richtig": "b"}],

            [{"frage": "Wer hat Python erfunden?",
             "antworten": {"a": "Elon Musk", "b": "Guido van Rossum", "c": "Steve Jobs"},
             "richtig": "b"}]]
    frage_nummer = 0
    while frage_nummer < 3:
        for objekt in quiz[frage_nummer]:
            print(objekt["frage"])
            for key, value in objekt["antworten"].items():
                print(f"{key} {value}")
            antwort = input("Bitte gib deine Antwort ein: ").lower()
            if antwort == objekt["richtig"]:
                print("Korrekt")
                punkte += 1
            else:
                print("Leider Falsch")
            print(f"Du hast {punkte} Punkt{"e" if punkte != 1 else ""}")
            frage_nummer += 1

    match punkte:
        case(0):
            print("Versuchs Nochmal")
        case(1):
            print("Ist ein Anfang, aber da geht noch mehr")
        case(2):
            print("Fasst alles gelöst!")
        case(3):
            print("Perfekt Gelöst!")


if __name__ == "__main__":
    main()