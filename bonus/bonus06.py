#Программа запрашивает у пользователя его рост (в см) и вес (в кг),
#считает индекс массы тела и выдаёт интерпретацию.

Num1 = input("Введите ваш вес (в килограммах): ")
if Num1 == "":
    print("Вы забыли ввести число!")
    raise SystemExit    
wt = int(Num1)

Num2 = input("Введите ваш рост (в сантиметрах): ")
if Num2 == "":
    print("Вы забыли ввести число!")
    raise SystemExit
height = int(Num2)
ht = height / 100

bmi = wt / (ht * ht)
print(bmi)

if bmi < 16:
    print("Выраженный дефицит массы тела.")
if bmi > 16 and bmi < 18.49:
    print("Недостаточная масса тела.")
if bmi > 18.5 and bmi < 24.99:
    print("Ваш вес в норме.")
if bmi > 25 and bmi < 29.99:
    print("Избыточная масса тела.")
if bmi > 30 and bmi < 34.99:
    print("Ожирение первой степени.")
if bmi > 35 and bmi < 39.99:
    print("Ожирение второй степени.")
if bmi > 40:
    print("Ожирение третьей степени(морбидное).")