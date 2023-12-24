import math

def func(x, y):
    z1 = math.cos(y+0.5) - x - 2 
    z2 = math.sin(x) - 2*y -1 
    f = z1+z2
    print(f)


x = float(input("Введите число X"))
y = float(input("Введите число Y"))

func(x,y)