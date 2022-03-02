sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for value in sentence:
    if value.isdigit():
        value = f'"{value.zfill(2)}"'
    elif value[0] in '+-' and value[1].isdigit():
        value = f'"{value[0] + value[1:].zfill(2)}"'


    print(value, end=' ')
