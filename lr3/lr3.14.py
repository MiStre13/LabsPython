bull_price = 10
cow_price = 5
calf_price = 0.5
available_money = 100
total_heads = 100

possible_combinations = []

for bulls in range(11):  
    for cows in range(21): 
        calves = total_heads - bulls - cows
        total_cost = bulls * bull_price + cows * cow_price + calves * calf_price
        if total_cost == available_money and calves >= 0:
            possible_combinations.append((bulls, cows, calves))


for combination in possible_combinations:
    print(f"Быков: {combination[0]}, Коров: {combination[1]}, Телят: {combination[2]}")
