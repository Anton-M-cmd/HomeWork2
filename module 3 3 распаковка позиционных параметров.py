def print_params (a = 1, b = 'строка', c = True):
    print(a)
    print(a, b, c)
    print()


values_list = [2, 3.45,'str']
values_dict = {'a': 6, 'b': 7.89, 'c': 'бу'}
print_params(b = 25,c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)


