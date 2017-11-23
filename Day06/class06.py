#with open("text.txt", 'w') as f:   # 'w' перезаписывает файл, если он не пустой
#    f.write("hello \n world") 


#sent="Доброе утро, страна"
#words = sent.split()
#lines = []
#for w in words:
#    lines.append(w + '\n') #пишет каждое слово с новой строки

#with open("text.txt", "a", encoding = "utf-8") as f: # 'a' добавляет в уже существующий файл
#    f.writelines(lines)


#sent = "Доброе утро страна"
sent = "Доброе УТРО страна НЕ будите МЕНЯ утром"
words = sent.split()
lines = []

with open("text.txt", "w", encoding = "utf-8") as f:
#    for i in range(len(words)):
#        if i % 2 == 0:
#            lines.append(words[i].upper() + '\n')
#        else:
#            lines.append(words[i] + '\n')
#    for line in lines:
#        f.write(line.upper()) #печатает все заглавными
#    f.writelines(lines)
    for i,w in enumerate(words):
        if i % 2 == 1:
            f.write(str(i), " ", w.upper())
        else:
            f.write(str(i), " ", w)

            
if 'hello' in lines
