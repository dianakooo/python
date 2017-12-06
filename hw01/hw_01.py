# Вариант 4

print("Привет!")

input_a = input("Введите число a: ")
a = int(input_a)

input_b = input("Введите число b: ")
b = int(input_b)

input_c = input("Введите число c: ")
c = int(input_c)

if a + b == c:
    print("Сумма a и b равна c")
else:
    print("Сумма a и b не равна c")

if a * b == c:
  print("Произведение a и b равно c")
else:
  print("Произведение a и b не равно c")
  
if a % b == c:
  print("a даёт остаток c при делении на b")
else:
  print("a не даёт остаток c при делении на b")

if a * c + b == 0:
  print("c является решением линейного уравнения ax + b = 0")
else:
  print("c не является решением линейного уравнения ax + b = 0")  
  
if a / b == c:
    print("Частное a и b равно c")
else:
    print("Частное a и b не равно c")
  
if pow(a, b) == c:
  print("a в степени b равно c")
else:
  print("a в степени b не равно c")  

print("Конец")
