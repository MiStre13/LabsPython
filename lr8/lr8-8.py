def delete_backspace(st):
    result = ''
    for char in st:
        if char == '@' and len(result) > 0:
            result = result[:-1]
        elif char != '@':
            result += char
    return result

print(delete_backspace('пп@олс@кр@овт@оде@ец'))
print(delete_backspace('сварка@@@@@лоб@ну@'))
