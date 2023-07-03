def fun_1(x):
    x = int(x)
    x = abs(x)
    var_1 = x // 100
    var_2 = x % 100 // 10
    var_3 = x % 100 % 10
    return var_1, var_2, var_3


number = input("Введіть число: ")
print(*fun_1(number), sep='\n')


def fun_1_1():
    num = int(input("Введіть число:"))
    num = abs(num)
    var_1 = num // 100
    var_2 = num % 100 // 10
    var_3 = num % 100 % 10
    print(var_1)
    print(var_2)
    print(var_3)


fun_1_1()


def fun_2(x, y):
    return x + y


result = fun_2(int("-11", 10), int(15))
print("fun_2:", result)


def fun_3(var_1, var_2):
    int_v1 = str(var_1)
    int_v2 = str(var_2)
    int_v3 = int_v1 + int_v2
    return int_v3


var_1 = int("-11", 10)
var_2 = int(15)
result = fun_3(var_1, var_2)
print("fun_3:", result)


def fun_4():
    stuff_name_1 = "Yurii"
    stuff_position_1 = "builder"
    stuff_salary_1 = "10000"
    stuff_name_2 = "Igor"
    stuff_position_2 = "Compuctor_man_1"
    stuff_salary_2 = "100000"
    stuff_name_3 = "Sergii"
    stuff_position_3 = "Compuctor_man_2"
    stuff_salary_3 = "50000"

    print("Stuff information 1:", stuff_name_1, "-", stuff_position_1, '\t', stuff_salary_1)
    print("Stuff information 2: {} - {} \t {}".format(stuff_name_2, stuff_position_2, stuff_salary_2))
    print("Stuff information 3: " + "%s - %s %s %s" % (stuff_name_3, stuff_position_3, '\t', stuff_salary_3))
    # can't understand why in Stuff information 2 there are six spaces
    # Stuff information 1 and Stuff information 3 - Just four spaces


fun_4()
