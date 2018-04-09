
word_count = 0
listed = []
razum_listed = []
lines = []
cells = []
words = []

with open("quotes.txt", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        cells = line.split('—')
        words = cells[0].split()
        for word in words:
            word_count += 1
        if (word_count <= 10) and (len(word[0]) < 5):
            print(line)
        word_count = 0
