# 1)321 = 31
# 2) 31*10 = 310
# 3) 31%10 = 1
# 4) 2)+3)

n = int(input("Введите число n"))

if 99<n<999:
    # newDigit=n%100//10
    lastDigitN = n%10
    newDigitN = n//100*10+lastDigitN
    lastDigitX = newDigitN%10
    newDigitN = newDigitN*10
    newDigitN = newDigitN+lastDigitX
    print("Result = ", newDigitN)
  


else:
    print("Введите число n трех-значное")
