immutable_var = (1, 2.0, False, [3,4])
print(immutable_var)
#immutable_var[0] = 5
#print(immutable_var) - нельзя заменить 1 на 5, т.к. кортеж не поддерживает обращение по элементам\редактирование
immutable_var[3][0] = 5
print(immutable_var) # списки, вкходящие в кортеж, можно редактировать
mutable_list = ['six', 7.0, True, (8,9)]
print(mutable_list)
mutable_list[2] = False
mutable_list[1] = 'seven'
#mutable_list[3][0] = 10 - кортеж также нельзя изменить
print(mutable_list)
