
word_count = 0
lines = []
cells = []
words = []

with open("quotes.txt", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        cells = line.split('—')
        for cell in cells:
            words = cell.split()
            for word in words:
                if (len(word[0]) < 5) and (len(cell) <=10):
                    print(line)
        

#for word in lines:
#    while word != "-":
#        word_count += 1
#    if word[0] > 5 and word_count >= 10:
#        print(line)
