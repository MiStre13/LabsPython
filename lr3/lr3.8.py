digit = int(input("введите число :"))

maxDigit = 9
count = 0

while digit:
    ost = digit % 10 
    if ost < maxDigit:
        maxDigit = ost
        count = 1
        print("maxDigit:",maxDigit)
    elif ost == maxDigit:
        count+=1
        print("ost:",ost)
    digit = digit//10
    print("digit:",digit)
print("count",count)

