import random

def random_word(filename):
    with open(filename, encoding='utf-8') as f:
        words = []
        lines = f.readlines()
        for line in lines:
            if line.endswith('\n'):
                line = line[:-1]
            words += [line]
        return random.choice(words)

def verb1():
    return random_word('verb1.txt')

def noun1():
    return random_word('noun1.txt')

def adv1():
    return random_word('adv1.txt')

def verb2():
    return random_word('verb2.txt')

def noun2():
    return random_word('noun2.txt')

def conj():
    return random_word('conj.txt')

def verb3():
    return random_word('verb3.txt')

def noun3():
    return random_word('noun3.txt')

def adj():
    return random_word('adj.txt')

def verb4():
    return random_word('verb4.txt')

def adv2():
    return random_word('adv2.txt')

def noun4():
    return random_word('noun4.txt')

def haiku():
    number = random.choice([0,1])
    if number == 0:
        print(verb1() + ' ' + noun1())
        print('perchè ' + adv1() + ' ' + verb2() + ' ' + noun2())
        print(conj() + ' non ' + verb3() + ' mai.')
    else:
        print(noun3() + ' ' + adj())
        print('sono ' + verb4() + ' ' + adv2() + '.')
        print('e che ' + noun4() + '!')

haiku()






        
