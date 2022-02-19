def separator(sep):
    print(sep * 100, '\n')


# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


def duration(seconds: int):
    if seconds < 60:
        print(seconds, 'сек')
    elif seconds < 3600:
        print(f'{seconds // 60} мин, {seconds % 60} сек')
    elif seconds < 86400:
        print(f'{seconds // 3600} час, {seconds % 3600 // 60} мин, {seconds % 3600 % 60} сек')
    else:
        print(
            f'{seconds // 86400} дн, {seconds % 86400 // 3600} час, {seconds % 86400 % 3600 // 60} мин, {seconds % 86400 % 3600 % 60} сек')


duration(59)
duration(365)
duration(9999)
duration(123456789)

separator('*')

# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000
cubes = [i ** 3 for i in range(1, 1001, 2)]
cubes_plus_17 = [i + 17 for i in cubes]


def number_sum(numbers):  # Функция, считающая сумму цифр в числах списка
    whole_sum = []
    for number in numbers:
        number_copy = number
        current_result = []
        while number_copy > 0:
            current_result.append(number_copy % 10)
            number_copy //= 10
        if (sum(current_result)) % 7 == 0:
            whole_sum.append(number)
    print(sum(whole_sum))


number_sum(cubes)
number_sum(cubes_plus_17)

number_sum([i + 17 for i in cubes])  # Задание со звездочкой
separator('*')
# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

for i in range(1, 101):
    if 10 < i < 20 or i % 10 in (0, 5, 6, 7, 8, 9):
        print(i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    else:
        print(i, 'процента')
