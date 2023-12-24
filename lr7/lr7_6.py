def find_longest_string(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    max_length = 0
    max_length_number = 0

    for i, line in enumerate(lines):
        length = len(line.strip())
        if length > max_length:
            max_length = length
            max_length_number = i + 1

    print("Длина самой длинной строки:", max_length)
    print("Номер самой длинной строки:", max_length_number)
    print("Самая длинная строка:", lines[max_length_number - 1].strip())

file_name = "/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr4.txt"
find_longest_string(file_name)
