from itertools import zip_longest
import json

out_dict = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        sum_lines_users = sum(1 for line in users)
        sum_lines_hobby = sum(1 for line in hobby)
        if sum_lines_users < sum_lines_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for line_user, line_hobby in zip_longest(users, hobby):
            out_dict[line_user.strip()] = line_hobby.strip() if line_hobby is not None else line_hobby

with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f, ensure_ascii=False)
'''
    Я почитал, зачем нужен параметр ensure_ascii=, без него json сохранит все в кодировке, но не выведет понятную
    рускоговорящему человеку кириллицу
'''
print(out_dict)
