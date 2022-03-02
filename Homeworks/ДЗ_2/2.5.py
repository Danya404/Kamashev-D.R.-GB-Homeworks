prices = [57.8, 16.94, 19.84, 99.99, 69.96, 10.01, 32.1, 45, 17.98, 88.04, 12.34]

for (index, price) in enumerate(prices):
    pennies = str(price).split(".")
    try:
        print(pennies[0], 'руб', pennies[1].ljust(2, '0'), 'коп', end='.' if index == len(prices) - 1 else ', ')
    except IndexError:
        print(pennies[0], 'руб 00 коп', end='.' if index == len(prices) - 1 else ', ')

print('\n')
print(id(prices))
prices.sort()
print(prices)
print(id(prices), end='\n' * 2)

print(sorted(prices, reverse=True))  # Список цен по убыванию
print(sorted(prices, reverse=True)[0:5])  # Топ-5 самых дорогих товаров