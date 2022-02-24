def thesaurus(*args):
    my_dict = {}
    for i in args:
        my_dict[i[0]] = list(filter(lambda x: x.startswith(i[0]), args))

    print (my_dict)


thesaurus("Иван", "Мария", "Петр", "Илья")
