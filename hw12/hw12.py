import os
import re

def main():
    start_path = 'hw12'
    fnames = os.listdir(start_path)
    files = 0
    file_list = []
    for fname in fnames:
        n = ""
        if os.path.isfile(os.path.join(start_path, fname)):  # проверяет, файл ли это
            name = fname.split('.')[:-1]  
            for i in name:
                n += i
                if len(name) != 1:
                    if i != name[-1]:
                        n += '.'               # смотрит имя файла без его типа
            if re.search("[^a-zA-Z]", n) == None:      #смотрит содержимое имени файла
                files += 1       # подсчитывает количество
                file_list.append(n)
                print(fname)
    if files == 1:
        print('1 file found')
    else:
        print(files, ' files found')
    final_list = []
    for file in file_list:
        if file not in final_list:
            final_list.append(file)
    print('Filenames: ', final_list)   # выводит имена файлов на слйчай, если есть несколько файлов с одним именем, но разными типами

if __name__ == "__main__":
    main()





