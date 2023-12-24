sales_data = [
    "Иванов лыжи 1",
    "Иванов сумка 1",
    "Иванов палки 2",
    "Петров коньки 3",
    "Петров куртка 1"
]

customers = {}  # Словарь для хранения информации о покупателях

for sale in sales_data:
    data_split = sale.split()  # Разбиваем запись на отдельные части
    customer = data_split[0]  # ФИО покупателя
    product = data_split[1]  # Наименование товара
    quantity = int(data_split[2])  # Количество товара
    
    if customer in customers:
        if product in customers[customer]:
            customers[customer][product] += quantity
        else:
            customers[customer][product] = quantity
    else:
        customers[customer] = {product: quantity}

# Выводим результаты
for customer, products in customers.items():
    print(customer + ":")
    for product, quantity in products.items():
        print(product, quantity)
    print()
