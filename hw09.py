import re

with open("text.txt", encoding = "utf-8") as f:
    text = f.read()

words = re.findall("вып['ей''ит''ил''ив''ье''ью'][^ .,»):!?[]+", text)

if words == []:
    print("Empty")
else:
    print(words)


#выпить
#выпил
#выпила
#выпило
#выпили
#выпью
#выпьешь
#выпьет
#выпьем
#выпьете
#выпьют
#выпей
#выпейте
#выпив
#выпит__
