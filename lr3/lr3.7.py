digit = int(input("Введите числло : "))

current = 1
previos = 1

while(digit > current):
    next_number = current + previos
    previos = current
    current = next_number

print(current)
