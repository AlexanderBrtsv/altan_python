# ***Коллекции***

#  Список (list)

# Создание пустого списка
my_list = []
my_list = list()

# добавление объекта (элемент) в список
my_list.append(100)
my_list.append(3.14)
my_list.append("Hello")
my_list.append('Hi')
my_list.append([10, 20, 30])

# чтение значения элемента списка
# Прямая индексация (слева направо)
el = my_list[4]

el = my_list[0]

# чтение значений вложеннной коллекции
el = my_list[4][1]

# обратная индексация
el = my_list[-1]
el = my_list[-1][-1]

# print(my_list)
# print(el)

#  Замена значений элементов

my_list[0] = 777.0

# Удаление элемента по значениям
my_list.remove(3.14)

# Удаление элемента по индексу
del my_list[-1]

# Срез списка

# Создание исходного списка из строки
s = "Hello World"
my_list = list(s)

# срез от начала до конца
my_slice = my_list[:]

# срез со 2-го индекса до конца исходного списка
my_slice = my_list[2:]

# срез с начала списка до 5-го индекса не включительно
my_slice = my_list[:5]

# срез со 1-го индекса до 7го не вкл
my_slice = my_list[1:7]

# срез со 2-го индекса до 10го индекса не вкл с шагом 2
my_slice = my_list[2:10:2]

# срез с применением обратной индексации
my_slice = my_list[-2:-7:-1]

# переворот списка
my_slice = my_list[::-1]

# print(my_list)
# print(my_slice)

# длину можно узнать с помощью функции len()
# print(len(my_list))

# ***Кортеж (tuple)***

# Неизменяемая (immutable) коллекция
# легковеснее чем список

# созжание кортежа
my_tuple = (10, 20, 30, 5, 1, 0)

# чтение значений элементов
el = my_tuple[0]

# срез
my_slice = my_tuple[2:]

# print(my_tuple)
# print(my_slice)

# ***Словарь (dict)***

# пара "ключ-значение"
# {ключ_1:значение_1, ключ_2:значение_2}

# создание словаря
my_dict = {10:3.14, "abc":[1, 2, 3]}

# чтение значений
val = my_dict["abc"]
val2 = my_dict[10]

# print(my_dict)
# print(val)
# print(val2)

# замена значения
my_dict[10] = 777
# print(my_dict)

# добавление новой пары
my_dict["A"] = "hello"
# print(my_dict)

# удаление пары
del my_dict[10]
print(my_dict)