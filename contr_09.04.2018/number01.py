import re

def opening(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()
    return text

def searching(text):
    ns = re.findall("\n", text)
    number = len(ns)
    number = number + 1
    return number

def main():
    isl = opening("kontrosha.html")
    lines = searching(isl)
    lines = str(lines)
    with open("kr.txt", "w", encoding='utf-8') as r:
        r.write(lines)
    
if __name__ == "__main__":
    main()


