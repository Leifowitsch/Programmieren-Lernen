import random
import math
import time
seconds = 0
options = ["Schere", "Stein", "Papier"]
options2 = ["schere", "stein", "papier"]

while True:
    option = random.choice(options)
    user_option = input("Schere, Stein oder Papier? (q to quit): ").lower()
    if user_option not in options2:
        if user_option == "q":
            break
        print("Nicht Valide!")
    elif user_option in options2:
        for second in options2:
            time.sleep(1)
            seconds += 1
            print(seconds)
        seconds = 0
        print(f"Du: {user_option.upper()} VS. {option.upper()}")
        if user_option == option.lower():
            print("----UNENTSCHIEDEN----")
        elif user_option == "schere" and option == "Papier":
            print("----GEWONNEN----")
        elif user_option == "stein" and option == "Schere":
            print("----GEWONNEN----")
        elif user_option == "papier" and option == "Stein":
            print("----GEWONNEN----")
        else:
            print("----VERLOREN----")



