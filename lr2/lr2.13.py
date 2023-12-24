a = int(input("Введите число: "))

if a>99:
    digitOne = a//100
    digitTwo = a//10%10
    digitThree = a%10
   
    if digitOne == digitTwo == digitThree:
        print("Все числа равны")
        
        print("Есть два одинаковых числа ")
        
    else:
        print("Числа не одинаковые")
        
        if digitOne == digitTwo or digitTwo==digitThree or digitOne==digitThree:
            print("Есть два одинаковых числа")
        else:
            print("Одинаковых чисел нет")

else:
    print("Надо ввести 3-х значное число")


