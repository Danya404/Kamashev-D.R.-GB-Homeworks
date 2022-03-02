names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for name in names:
    misspelled_name = ' '.join(name.split()[-1:])
    print('Привет,', misspelled_name.capitalize() + "!")
