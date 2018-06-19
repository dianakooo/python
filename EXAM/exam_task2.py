import csv
import os
import re

def main():
    start_path = 'news'
    fnames = os.listdir(start_path)
    #print(fnames)
    for fname in fnames:
        with open(os.path.join(start_path, fname), encoding = "utf-8") as f:
            text = f.read()
            brevs = re.findall('lex=\"([А-Я][А-Я]+)', text)
        #print(brevs)
        brevtypes = {}
        for brev in brevs:
            if brev in brevtypes:
                brevtypes[brev] += 1
            else:
                brevtypes[brev] = 1
        print(brevtypes)
            
if __name__ == "__main__":
    main()

   #ну я же была на правильном пути, да?..
