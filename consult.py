lines2016 = []
a = 0
with open("happiness-cantril-ladder.csv", encoding='utf-8') as f:
    #for line in f:
    lines = f.readlines()
    for line in lines:
        #print(line)
        cells = line.split(',')
        #print(cells)
        if cells[2] == '2016':
            lines2016.append(cells)
user_country = input("Your country: ")

for line in lines2016:
    if line[0] == user_country:
        print(line[-1])
        a += 1
        break
    
if a != 1:
    print("Country not found.")


#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                    #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                        #AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                            #AAAAAAAAAAAAAAAAAAAAA
                                #AAAAAAAAAAAAA
                                    #AAAAA

        #kak sortirovat' strochki??

sorted(..., reverse=True)
