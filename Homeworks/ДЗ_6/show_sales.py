import sys

nums = sys.argv[1:]
with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(nums) > 1:
        start_idx = int(nums[0])
        end_idx = int(nums[1])
    elif len(nums) == 0:
        start_idx = 0
        end_idx = sum(1 for line in f)
        f.seek(0)
    else:
        start_idx = int(nums[0])
        end_idx = sum(1 for line in f)
        f.seek(0)
    for idx, line in enumerate(f):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())
'''Задание со звездочкой разобрал самостоятельно, ибо и так получилось, что большую часть дз посмотрел на разборе.
Тема работы файлов для меня оказалась сложнее, чем я думал.'''