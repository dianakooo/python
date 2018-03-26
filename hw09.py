#Вариант 4

import re

with open("alice.txt", encoding = "utf-8") as f:
    text = f.read().lower()

words = re.findall("вып[еиь][йтлвею][^ .,»):!?[]*", text)
#words = re.findall("вып['ей''ит''ил''ив''ье''ью'][^ .,»):!?[]+", text)

if words == []:
    print("Empty")
else:
    print(words)
