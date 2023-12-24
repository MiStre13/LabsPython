numbers = [num for num in range(1, 10001) 
           if (num%7==0 and num%3==0) or num % 9 == 0]
print(numbers)