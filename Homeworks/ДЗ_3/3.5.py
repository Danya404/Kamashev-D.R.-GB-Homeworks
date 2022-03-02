from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    """функция, генерирующая 'шутки'"""
    for humoresque in range(n):
        joke = (choice(nouns), choice(adverbs), choice(adjectives))
        joke_str = ' '.join(joke)
        print(joke_str)


get_jokes(3)
