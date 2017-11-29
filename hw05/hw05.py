
#Вариант 4

a = 0

with open("text.txt", "w", encoding = "utf-8") as f:
    for i in range(10000):
        word = input("Введите латинское слово: ")
        if word == "":
            break
        else:
            if word[-3:] == "are" or word[-3:] == "ere" or word[-3:] == "ire" or word[-3:] == "ari" or word[-3:] == "eri" or word[-3:] == "iri":
                f.write(word + '\n')
                a += 1
            
print("Количество возможных инфинитивов: ", a)

