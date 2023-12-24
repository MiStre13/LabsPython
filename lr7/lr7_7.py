def reverse_lines(file_name_in, file_name_out, order):
    with open(file_name_in, 'r') as file_in:
        lines = file_in.read()

    if order == 'a':
        reversed_lines = lines[::-1]
    elif order == 'b':
        reversed_lines = reversed(lines)
    else:
        print("Введено неверное значение")
        return

    with open(file_name_out, 'w') as file_out:
        file_out.write(reversed_lines)

    print("Строки переписаны успешно.")

file_name_in = "/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr7(inp).txt" 
file_name_out = "/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr7(out).txt" 
order = input("Выберете вариант ответа а или b ")  

reverse_lines(file_name_in, file_name_out, order)
