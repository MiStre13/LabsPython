import math

def distance_to_line(P0, P1, P):
    x0, y0 = P0
    x1, y1 = P1
    x, y = P
    
    dx_line = x1 - x0
    dy_line = y1 - y0
    dx_point = x - x0
    dy_point = y - y0
    
    t = (dx_point * dx_line + dy_point * dy_line) / (dx_line * dx_line + dy_line * dy_line)
    
    if t < 0:
        xx = x0
        yy = y0
    elif t > 1:
        xx = x1
        yy = y1
    else:
        xx = x0 + t * dx_line
        yy = y0 + t * dy_line
    
    distance = math.sqrt((x - xx) ** 2 + (y - yy) ** 2)
    
    return distance


x_p = float(input("Введите x-координату точки P: "))
y_p = float(input("Введите y-координату точки P: "))

num_lines = int(input("Введите количество линий: "))

distances = []
for i in range(num_lines):
    print(f"Линия {i+1}:")
    x_p0 = float(input("Введите x-координату точки P0: "))
    y_p0 = float(input("Введите y-координату точки P0: "))
    x_p1 = float(input("Введите x-координату точки P1: "))
    y_p1 = float(input("Введите y-координату точки P1: "))
    
    P0 = (x_p0, y_p0)
    P1 = (x_p1, y_p1)
    P = (x_p, y_p)
    
    distance = distance_to_line(P0, P1, P)
    distances.append(distance)

print("Расстояния от точки P до каждой линии:")
for i, distance in enumerate(distances):
    print(f"Линия {i+1}: {distance}")
