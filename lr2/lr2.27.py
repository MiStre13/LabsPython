

n = int(input("Введите число n"))

if 99<n<999:
    lastDigit = n%10
    n = n - lastDigit
    n = n//10
    lastDigitX = n%10*100
    n=lastDigitX+n
    print("Result=",n)
    
else:
    print("Введите число n трех-значное")