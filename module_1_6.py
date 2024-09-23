my_dict = {'Anna': 1987, 'Sveta': 1991, 'Max': 1992}
print(my_dict)
print(my_dict['Anna'])  #существующий ключ
print(my_dict.get('Lexa'))  #отсутствующий ключ
my_dict.update({'Alex':2001,'Max': 1999}) #доп пара
del_name = my_dict.pop('Sveta')    #удалить существующий
print(del_name) #вывести значение удаленного
print(my_dict)

my_set = {1,2,3,4,1,3,5,2}
print(my_set)
my_set.update({6, 7})   #доп 2 элемента
my_set.discard(3)   #удалить элемент
print(my_set)