immutable_var = (1,2,3,4,5,'qwerty')
print(immutable_var)
print(type(immutable_var))
# immutable_var[-1]=immutable_var[-1].upper()
# print(immutable_var) - !? - объект не поддерживает назначение элементов, т.к. "tuple"- неизменяемый тип данных с упорядоченной последовательностью элементов
# поэтому переводим "кортеж" в "список"("list" - изменяемую последовательность с упорядоченными элементами)=>
mutable_list = [1,2,3,4,5,'qwerty']
print(mutable_list)
mutable_list[0]=2
print(type(mutable_list))
mutable_list[-1]=mutable_list[-1].upper()
print(mutable_list)
