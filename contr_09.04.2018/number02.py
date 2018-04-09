import re

def opening(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()
    return text

def searching(text):
    ns = re.search('<w lemma="(.*?)" type="(.*?)">(.*?)</w>', text)
    first = re.findall(ns.group(2), text)
    number = len(first)
    return number

def main():
    isl = opening("contr.html")
    lines = searching(isl)
    lines = str(lines)
    with open("dict.txt", "w", encoding='utf-8') as r:
        r.write(lines)
    
if __name__ == "__main__":
    main()

