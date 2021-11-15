# ***"Условные операторы"***
var = 5

# if имеет условие
# if выполняет код внутри своего тела если условие истинно иначе   
# if var != 0: 
#     print("Hello")

# if var < 7:
#     print("Меньше")
# else:
#     print("Больше")

var = "G"

if var == "A":
    res = "Lit A"
# else if
elif var == "B":
    res = "Lit B"
elif var == "C":
    res = "Lit C"
elif var == "a":
    res = "Lit a"
else:
    res = "Не один из вариантов"
# print(res)


# *** Пример. "Термостат"***

# текущая температура
current_temp = 27

# диапозон температур
min_temp = 21
max_temp = 26

# логика термостата
if current_temp < min_temp:
    print("включен нагрев")
elif current_temp > max_temp:
    print("Выключен нагрев")
else:
    print("Температура оптимальна")

