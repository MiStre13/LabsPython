
h = int(input("Введите часы (от 1 до 23): "))
m = int(input("Введите минуты (от 0 до 59): "))
s = int(input("Введите секунды (от 0 до 59): "))

angle = (360 / 12) * (h % 12) + (360 / 12 / 60) * m + (360 / 12 / 60 / 60) * s

print(f"Угол между положением часовой стрелки в начале суток и указанным моментом времени: {angle} градусов.")

