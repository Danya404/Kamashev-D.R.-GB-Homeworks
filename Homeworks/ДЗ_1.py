def separator(sep):
    print(sep * 100, '\n')


# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


def duration_sec(seconds: int):
    print(seconds, 'сек')


def duration_min(seconds: int):
    minutes = seconds // 60
    print(minutes, 'мин', seconds, 'сек')


def duration_hrs(seconds: int):
    hours = seconds // 3600
    minutes = seconds // 60
    print(hours, 'час', minutes, 'мин', seconds, 'сек')


def duration_days(seconds: int):
    days = seconds // 86400
    hours = seconds // 3600
    minutes = seconds // 60
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')


duration_sec(59)
duration_min(365)
duration_hrs(9999)
duration_days(123456789)
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
    if i % 10 == 1:
        print(i, 'процент')
    elif 10 < i < 20 or i % 10 in (0, 5, 6, 7, 8, 9):
        print(i, 'процентов')
    else:
        print(i, 'процента')
