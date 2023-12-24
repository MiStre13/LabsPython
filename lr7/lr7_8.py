def number_raz(file_name1, file_name2):
    count = 0
    flag = True
    with open(file_name1, 'r') as file1, open(file_name2, 'r') as file2:
       for a1, a2 in zip(file1, file2):
        count += 1
        if a1 != a2:
            flag = False
            break

    print(f"Нет отличий") if flag else print(f"Отличается строка {count}")



file_name1 = "/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr7(inp).txt" 
file_name2 = "/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr7(out).txt" 
number_raz(file_name1, file_name2)