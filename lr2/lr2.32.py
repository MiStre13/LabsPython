y = float(input("Введите угол для часовой стрелки (0 < y <= 2): "))

minutes_angle = y * 60
hours = int(y)
remainder_angle = y - hours
minutes = int(remainder_angle * 60)

print(f"Значение угла для минутной стрелки: {minutes_angle} градусов")
print(f"Количество полных часов: {hours}")
print(f"Количество полных минут: {minutes}")

