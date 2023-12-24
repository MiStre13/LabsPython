n = int(input("vvdeite n "))
counter_fact = 1
sum_fact = 1
for i in range(2, n+1):
    counter_fact *= i
    sum_fact += counter_fact
print(sum_fact)
