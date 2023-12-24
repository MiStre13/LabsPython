names = ['Маша', 'Петя', 'Вася']

hashNames = list(map(lambda x: hash(x), names))

print(hashNames)