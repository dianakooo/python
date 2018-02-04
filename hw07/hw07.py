#вариант 4

def name():
    fname = input("Введите расположение файла на вашем компьютере(без кавычек): ")
    return fname

def open_file(fname):
    with open(fname, encoding='utf-8') as f:
        text = f.read()
    words = text.split(' ')
    for word in words:
        word = word.strip('.,?!<>{}[]()"')
    return words

def counting(words):
    count = [0,0]
    for word in words:
        if word[-2:] == "ed":
            count[0] += 1
            if word[-3] == "i":
                count[1] += 1
    return count

def main():
    fname = name()
    mat = open_file(fname)
    numbers = counting(mat)
    print("Число форм на -ed в тексте: ", numbers[0])
    print("Число слов, образованных от глаголов на -e, -y: ", numbers[1])

main()
