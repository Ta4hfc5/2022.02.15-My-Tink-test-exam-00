# 2022.02.15 - My Tink test exam 00
min_val, max_val = -32000, 32000 # Задаю приемлемый диапазон значений переменных

def func_get_var_a():
    while True:
        try:
            global Var_a
            Var_a = int(input("Введите значение первого целого числа A от -32000 до 32000\n"))
            if min_val <= Var_a <= max_val:
                print("Принято значение А:")
                return Var_a
            else : func_get_var_a()
            return
        except ValueError:
            print("Вы ввели некорректные данные. Повторите ввод.")

def func_get_var_b():
    while True:
        try:
            global Var_b
            Var_b = int(input("Введите значение второго целого числа B от -32000 до 32000\n"))
            if min_val <= Var_b <= max_val:
                print("Значение принято B:")
                return Var_b
            else : func_get_var_b()
            return
        except ValueError:
            print("Вы ввели некорректные данные. Повторите ввод.")

print (func_get_var_a()) # Вызов функции назначения А
print (func_get_var_b()) # Вызов функции назначения B

sum_list = [Var_a,Var_b] # формирую список
sum_vars = sum(sum_list) # Получаю сумму
print("Сумма целых чисел = {}".format(sum_vars)) # Вывод значения пользователю.
