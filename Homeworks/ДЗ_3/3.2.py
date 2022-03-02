dictionary = {
    "one": "один", "two": "два", "three": "три", "four": "четыре",
    "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь",
    "nine": "девять", "ten": "десять"
}


def num_translate_adv(val):
    print(
        dictionary.get(val.lower(), "Неизвестное значение").capitalize() if val[0].isupper()
        else dictionary.get(val, "Неизвестное значение")
    )

num_translate_adv('two')
num_translate_adv('Two')
num_translate_adv('eleven')
