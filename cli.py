""" Some nice libraries """
import json
import sys
from random import choice, randint
import os

with open(os.path.join(sys.path[0], "de_schlachter.json"), "r", encoding="utf-8-sig") as raw:
    bible = json.load(raw)

chap = choice(bible)["chapters"]

# Determine the Input
chapters = []
if len(sys.argv) == 3:
    chapters = sys.argv[2].split(":")

# print either Verse, Chapter or Book
# depending on the arguments passed
try:
    if len(sys.argv) == 1:
        verse = chap[randint(0, len(chap)-1)]
        print(verse[randint(0, len(verse)-1)])

    else:
        F = None
        for verse in bible:
            if verse["name"] == sys.argv[1]:
                F = verse["chapters"]

        if chapters == []:
            for line in F:
                for sub in line:
                    print(sub)

        elif len(chapters) == 2:
            print(F[int(chapters[0]) - 1][int(chapters[1]) - 1])

        elif len(chapters) == 1:
            for line in F[int(chapters[0]) - 1]:
                print(line)
        else:
            # raise an error if to many arguments are given
            raise IndexError


except (IndexError, TypeError):
    print("Den Befehl habe ich nicht verstanden ...")
    print("Schreib John 1:20 oder John 1 oder John.")
    print("Du kannst das Script auch ohne Argumente ausführen für einen zufälligen Vers.")
