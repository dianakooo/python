#Вариант 4

word = input("Введите слово: ")

text = 0
a = 1
num = len(word)

while a <= num:
    print(word)
    letters = list(word)
    last = letters.pop()
    word = last + ''.join(letters)
    a += 1
