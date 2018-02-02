#Программа запрашивает у пользователя слово или фразу и переводит его
#на «кирпичный язык»: после каждой гласной добавляет “с” и ту же гласную.

word = input("Введите слово: ")
if word == "":
    print("Вы забыли ввести слово!")
    raise SystemExit
new_word = ""

for a in word:
    if a == "а" or a == "е" or a == "ё" or a == "и" or a == "о" or a == "у" or a == "ы" or a == "э" or a == "ю" or a == "я":
        new_word = new_word + a + "с" + a
    else:
        new_word = new_word + a
print(new_word)
