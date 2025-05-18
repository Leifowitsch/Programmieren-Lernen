import math
import time
stunde = int(input("Bitte gib die Stunde ein: "))
minute = int(input("Bitte gib die Minute ein: "))
sekunde = int(input("Bitte gib die Sekunde ein: "))

while sekunde < 61:
    time.sleep(1)
    sekunde += -1
    if sekunde == 00 and minute == 0 and stunde == 0:
        sekunde = 00
    elif sekunde == -1:
        sekunde = 59
        minute += -1
    if minute == 0 and stunde == 0:
        minute = 00
    elif minute == -1 and sekunde == 59:
        minute = 59
        stunde += -1
    if stunde == 0:
        stunde = 0
    if sekunde == 0 and stunde == 0 and minute== 0:
        break
    print(f"{stunde:02}:{minute:02}:{sekunde:02}")












