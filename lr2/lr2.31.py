y = float(input("Введите угол, на который повернулась часовая стрелка (0 <= y < 360): "))

minutes = (y * 60) % 360
hours = minutes // 60

print(f"Число полных часов: {int(hours)}")
print(f"Число полных минут: {int(minutes)}")
