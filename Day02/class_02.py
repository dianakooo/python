input_year=input("Введите год: ")
year = int(input_year) #перевод в формат числа

#input_num2=input("И еще одно: ")
#num2 = int(input_num2)

#word_length = len(word)
#print(word_length)

#if num > 0:
#    print(num, num*10)
#else:
 #   print(-num*10)
#print("Конец.")


#if num ==0 точное равенство
#if num != 0: #не равно нулю
 #   print(num)
#else:
    #print(num+100) эквивалентно двум строчкам ниже:
  #  num +=100
 #   print(num)
#print("Конец.")


#if num > 0:
 #   print(num)
  #  print("Больше нуля")
#else:
 #   print(num)
#    print ("Не больше нуля")
#    if num > -2:
#        print ("Больше -2")
#    else:
#        print ("Не больше -2")


#if num > 0 and num <=5:
#    print(num, "строго больше 0 И меньше или равно 5")

#if num > 0 or num <=5:
#    print(num, "строго больше 0 ИЛИ меньше или равно 5")


#if not 2 < 3:
#    print("hello")
#else:
#    print("no")


#if num1 % 2 == 0 and num2 % 2 == 0:
#    print("Оба четные")
#else:
    #if num1%2==1 and num2%2==1:
     #   print("Оба нечетные")
    #else:
     #   print("Одно четное")
#elif num1%2==0 and num2%2!=0:
#    print("Первое - четное, второе - нечетное")
#elif num1%2!=0 and num2%2==0:
#    print("Первое - нечетное, второе - четное")
#else:
#    print("Оба нечетные")


#if num1 < 0:
#    print(-1)
#elif num1 == 0:
#    print(0)
#else:
#    print(1)

#if year%4==0 and year%100!=0:
#    print("Год високосный")
#if year%400==0:
#    print("Год високосный")
#else:
#    print("Год не високосный")

if (year%4==0 and not year%100==0) or (year%400==0):
    print("Год високосный")
else:
    print("Год невисокосный")

print("Конец.")
