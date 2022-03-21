def odd_nums(n: int):
    for i in range(1, n, 2):
        yield i

print(list(odd_nums(15)))