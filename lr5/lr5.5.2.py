array = [1,2,3,4,5]
arrayTwo = [1,31,3]

def funcSumPerem(*args):
    circle = 0
    for arg in args:
        circle += 1
        total = 0 
        for num in arg:
            total += num**2
        print("Сумма квадратов",circle,"массива",total)

funcSumPerem(array, arrayTwo)


def fucnSrPerem(*args):
    circle = 0
    for arg in args:
        circle += 1
        length = len(arg)
        total = 0
        for num in arg:
            total += num/length
        print("Среднее значение",circle,"массива",total)
        
fucnSrPerem(array, arrayTwo)