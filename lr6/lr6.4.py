num_students = int(input("Введите количество школьников: "))
languages_all = set()
languages_any = set()

for _ in range(num_students):
    num_languages = int(input(f"Введите количество языков, которые знает школьник {num_students}: "))
    student_languages = set()
    for _ in range(num_languages):
        language = input("Введите название языка: ").strip()
        student_languages.add(language)
    if not languages_all:
        languages_all = student_languages
    else:
        languages_all &= student_languages
    languages_any |= student_languages

print("Количество языков, которые знают все школьники:", len(languages_all))
print("Список языков, которые знают все школьники:")
for language in sorted(languages_all):
    print(language)

print("Количество языков, которые знает хотя бы один школьник:", len(languages_any))
print("Список языков, которые знает хотя бы один школьник:")
for language in sorted(languages_any):
    print(language)
