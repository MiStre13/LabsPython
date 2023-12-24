# Открываем файл для чтения
with open('/Users/mikhailstreltsov/Desktop/учеба/pythonProject/lr7/lr9.txt', 'r') as file:
    # Считываем количество станций N
    N = int(file.readline().strip())

    # Создаем словарь для хранения информации о пассажирах
    passengers = {}

    # Считываем информацию о пассажирах
    for _ in range(N-1):
        line = file.readline().split()
        station_start = int(line[2])
        station_end = int(line[3])
        passengers[(station_start, station_end)] = passengers.get((station_start, station_end), 0) + 1

    # Находим максимальное значение в словаре
    max_passengers = max(passengers.values())

    # Выводим перегоны, на которых было наибольшее число пассажиров
    for key, value in passengers.items():
        if value == max_passengers:
            print(f"{key[0]}-{key[1]}")
