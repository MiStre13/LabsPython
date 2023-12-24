
def find_substr(subst, st):
    file1 = open(subst, "r")
    lines = file1.readlines()
    for line in lines:
        if line.startswith(st):
            return True
            break
    file1.close()
    return False

# считываем все строки

print(find_substr("/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr8/lr8.txt",'ddd'))