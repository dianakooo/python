#Вариант 4

fname = input("Введите расположение файла на вашем компьютере(без кавычек): ")
with open(fname, encoding = "utf-8") as f:
    text = f.read()
    words = text.split()
print(words)

punct_num = 0
words_num = 0

for word in words:
    words_num += 1
    if word[-1] != "." and word[-1] != ",":# or word[-1] != "?" or word[-1] != "!" or word[-1] != ":" or word[-1] != ";" or word[-1] != ")" or word[-1] != "]" or word[-1] != "}" or word[-1] != "\""
        punct_num += 1

print("Слов в тексте: ", words_num)
print("Слов, не оканчивающихся на точку или запятую: ", punct_num)

percent = 100*punct_num/words_num

print(percent,"%")
