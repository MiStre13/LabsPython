region_cities = {} 

while True:
    region = input("Введите название области, либо нажмите Enter для завершения:")
    if region == "":
        break
    cities = input("Введите города, относящиеся к области (через запятую):").split(",")
    region_cities[region] = [city.strip() for city in cities]


while True:
    city = input("Введите название города для поиска области, либо нажмите Enter для завершения:")
    if city == "":
        break

    found = False 
    for region, cities in region_cities.items():
        if city in cities:
            print(f"{region} область")
            found = True
            break

    if not found:
        print("Город не найден")

