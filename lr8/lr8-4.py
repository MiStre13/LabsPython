import os

def add_text_to_file(st):
    if os.path.isfile('sample.txt'):
        print("Строка добавлена к существующиму")
    else:
        print("Файл был создан")
    file1 = open('sample.txt', 'a+')
    file1.write(st+'\n')

add_text_to_file('chibrik')