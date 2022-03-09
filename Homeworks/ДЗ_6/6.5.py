from itertools import zip_longest
import sys

users, hobby, out = sys.argv[1:]
out_dict = {}
with open(out, 'w', encoding='utf-8') as f:
    with open('users.csv', encoding='utf-8') as users:
        with open('hobby.csv', encoding='utf-8') as hobby:
            sum_lines_users = sum(1 for line in users)
            sum_lines_hobby = sum(1 for line in hobby)
            if sum_lines_users < sum_lines_hobby:
                exit(1)

            users.seek(0)
            hobby.seek(0)
            for line_user, line_hobby in zip_longest(users, hobby):
                splitted_user = line_user.split(',')
                name = splitted_user[0]
                surname = splitted_user[1]
                patronymic = splitted_user[2]
                full_name = (f'{name} {surname} {patronymic}')

                f.write(f'{full_name.strip()}: ' f'{line_hobby.strip() if line_hobby is not None else line_hobby}\n')
