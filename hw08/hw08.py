#вариант 4

import random

def open_file(fname):
    with open(fname, encoding='utf-8') as f:
        text = f.read()
        lines = text.split('\n')        
    return lines

def gloss(a, dict):
    for l in a:
        row = l.split('\t')
        keyword = row[0]
        dict[keyword] = row[1:]
    return dict

def guess(dict):
    message = "Вы проиграли!"
    num = random.randint(1,5)
    if num == 1:
        for key in dict["врач"]:
            print(key, " ", "."*len(key))
            n = input("Введите слово: ")
            if n == "врач":
                message = "Вы победили!"
                break
    if num == 2:
        for key in dict["директор"]:
            print(key, " ", "."*len(key))
            n = input("Введите слово: ")
            if n == "директор":
                message = "Вы победили!"
                break
    if num == 3:
        for key in dict["повар"]:
            print(key, " ", "."*len(key))
            n = input("Введите слово: ")
            if n == "повар":
                message = "Вы победили!"
                break
    if num == 4:
        for key in dict["шпион"]:
            print(key, " ", "."*len(key))
            n = input("Введите слово: ")
            if n == "шпион":
                message = "Вы победили!"
                break
    if num == 5:
        for key in dict["водитель"]:
            print(key, " ", "."*len(key))
            n = input("Введите слово: ")
            if n == "водитель":
                message = "Вы победили!"
                break
    print(message)
    return 
    
def main():
    a = open_file('text1.txt')
    dict = {}
    b = gloss(a, dict)
    guess(b)
    
if __name__ == "__main__":
    main()
