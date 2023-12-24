# 321
# 21*10
# 210%100
# 2 
# 212


n = int(input("Введите число n"))

if 99<n<999:
    newDigit=n%100
    newDigit=newDigit*10
    firstDigitX = newDigit//100
    newDigit = newDigit + firstDigitX
    print("Result = ", newDigit)

else:
    print("Введите число n трех-значное")