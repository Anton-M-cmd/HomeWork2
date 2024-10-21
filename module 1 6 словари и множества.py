my_dict = {'Anton': 1989, 'Ilya': 1990, 'Roman': 1986}
print(my_dict)
print(my_dict.get('Anton'))
print(my_dict.get('Alexandr'))
my_dict.update({'Mihail': 1987, 'Sergei':1991 })
print(my_dict)
m = my_dict.pop('Mihail')
print(m)
print(my_dict)

my_set = {1,2,1,4,5,3,2,3,4,5,'q','w','e','w','r','t','t','y','y','string'}
print(my_set)
my_set.update({6,7,'строка'})
my_set.remove('string')
print(my_set)