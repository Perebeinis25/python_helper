# Task_1
def fun_list_concat(li_1):
    separation = ""

    for i in li_1:
        separation = separation + i

    return separation


li_1 = ["I ", "love ", "python ", "very ", "much !"]
result = fun_list_concat(li_1)
print(result)


# Task_2
def fun_list_num(li_2):
    separation = 0

    for i in li_2:
        # num = int(i)
        separation = separation + i
        # print(i)    # x = list_str[0] + list_str[1] + list_str[2] + list_str[3] + list_str[4]
    return separation


li_2 = [1, 10, 100, 2001, 5.52]
result = fun_list_num(li_2)
print(result)


# Task_3
def pair(num):
    var_1 = 0
    var_2 = 0

    for i in num:
        if i % 2 == 0:
            var_1 = var_1 + 1
        if i % 2 != 0:
            var_2 = var_2 + 1

    count_pair = var_1, var_2
    print(isinstance(count_pair, tuple))
    return count_pair


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 74]
result = pair(num)
print(result)


# Task_4
def object_definition(object_type):
    a = []

    for i in object_type:

        if type(i) == int or type(i) == float:
            a.append(i)

    return a


object_type = [54, 5, 4.6, True, "Python", (84674, 7493)]
result = object_definition(object_type)
print(result)


# Task_5
def exeption_seven(lst):
    a = []

    for i in lst:
        i = abs(i)

        if type(i) == int or type(i) == float:

            if i % 7 != 0:
                a.append(i)
    return a


lst = [0, -1, 3, 4, 5, 6, 7, 8, 9, -10.5, 11, 12, 47.7]
result = exeption_seven(lst)
print(result)


# Task_6
def multi_ply(input_num):

    if 0 < input_num < 10:

        for i in range(1, 10):

            res = i * input_num
            print("{} * {} = {}".format(i, input_num, res))
    else:
        print("Number is not valid")


multi_ply(5)
