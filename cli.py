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
        if len(chapters) > 1 and "-" in chapters[1]:
            splitter = chapters[1].strip().split("-")
            chapters[1] = splitter[0]
            chapters.append(splitter[1])

        for i in chapters:
            if int(i) < 1:
                raise IndexError

        F = None
        for verse in bible:
            if "name_ger" in verse and verse["name_ger"].lower() == sys.argv[1].lower() or verse["name"].lower() == sys.argv[1].lower() or verse["abbrev"].lower() == sys.argv[1].lower():
                F = verse["chapters"]

        if chapters == [] and sys.argv[1].lower() != "inhalt":
            for line in F:
                for sub in line:
                    print(sub)

        elif sys.argv[1].lower() == "inhalt":
            for verse in bible:
                if "name_ger" in verse:
                    print(verse["name_ger"], "/", verse["name"], f'({verse["abbrev"]})')
                else:
                    print(verse["name"], f'({verse["abbrev"]})')

        elif len(chapters) == 2:
            print(F[int(chapters[0]) - 1][int(chapters[1]) - 1])

        elif len(chapters) == 1:
            for line in F[int(chapters[0]) - 1]:
                print(line)
        elif len(chapters) == 3:
            for i in range(int(chapters[1]), int(chapters[2]) + 1):
                print(F[int(chapters[0]) - 1][int(i) - 1])
        else:
            # raise an error if to many arguments are given
            raise IndexError


except (IndexError, TypeError, ValueError):
    print("Den Befehl habe ich nicht verstanden ...")
    print("Möglich sind folgende Formate:")
    print("John\nJohn 1\nJohn 1:20\nJohn 1:20-25")
    print("")
    print("Längere Namen müssen mit Unterstrich geschrieben werden (z.B.: Book_of_Solomon).")
    print("Bücher mit Nummer sind ohne Abstand zu schreiben (z.B.: 1.Samuel).")
    print("Es funktionieren Abkürzungen und sowohl die englischen als auch die deutschen Namen.")
    print("")
    print("Das Script kann auch ohne Argumente ausgeführt werden für einen zufälligen Vers.")
    print("")
    print("Mit dem Befehl 'Inhalt' werden alle Bücher unter einander aufgelistet.")
