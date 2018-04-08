import re

def opening(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()
    return text

def searching(text):
    result = re.sub("философи", "астрологи", text)
    result1 = re.sub("Философи", "Астрологи", result)
    result2 = re.sub("Филосо́фи", "Астроло́ги", result1)
    result3 = re.sub("ФИЛОСОФИ", "АСТРОЛОГИ", result2)
# вообще правильно бы было сделать, чтобы он не менял слова вроде "философичный", "философический" и "философиня",
# но их нет в статье, поэтому я не знаю, нужно ли это учитывать в программе
    return result3

def main():
    philo = opening("philosophy.html")
    astro = searching(philo)
    with open("astrology.html", 'w', encoding = 'utf-8') as a:
        a.write(astro)
    print("Файл записан.")

if __name__ == "__main__":
    main()



