# Task_1
def fun_list_concat(li_1):
    separation = ""
    index_elem = 0

    while index_elem < len(li_1):
        separation += li_1[index_elem]
        index_elem += 1

    return separation


li_1 = ["I ", "love ", "python ", "very ", "much !"]
result = fun_list_concat(li_1)
print(result)


# Task_2
def fun_list_num(li_2):
    separation = 0
    index_elem = 0

    while index_elem < len(li_2):
        separation = separation + li_2[index_elem]
        index_elem += 1

    return separation


li_2 = [1, 10, 100, 2001, 5.52]
result = fun_list_num(li_2)
print(result)


# Task_3
def pair(num):
    var_1 = 0
    var_2 = 0
    index_elem = 0

    while index_elem < len(num):

        if num[index_elem] % 2 == 0:
            var_1 = var_1 + 1
        if num[index_elem] % 2 != 0:
            var_2 = var_2 + 1

        index_elem += 1

    count_pair = var_1, var_2

    return count_pair


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = pair(num)
print(result)


# Task_4
def object_definition(object_type):
    a = []
    index_elem = 0

    while index_elem < len(object_type):

        if type(object_type[index_elem]) == int or type(object_type[index_elem]) == float:
            a.append(object_type[index_elem])

        index_elem += 1

    return a


object_type = [54, 5, 4.6, True, "Python", (84674, 7493)]
result = object_definition(object_type)
print(result)


# Task_5
def exeption_seven(num_input):
    a = []
    num_input = abs(num_input)
    index_elem = 0

    if isinstance(num_input, int):

        while index_elem < num_input:

            if index_elem % 7 != 0:
                a.append(index_elem)

            index_elem += 1

        return a


result = exeption_seven(-33)
print(result)


# Task_6
def multi_ply(input_num):
    index_elem = 1
    while index_elem < 10:

        res = index_elem * input_num
        print("{} * {} = {}".format(index_elem, input_num, res))
        index_elem += 1
    else:
        print("Number is not valid")


multi_ply(10)


def fizz_fuzz(lst):
    index_elem = 0
    print(len(lst))
    while index_elem < len(lst):

        if lst[index_elem] % 7 == 0 and lst[index_elem] % 5 == 0:
            print(lst[index_elem], 'fizz fuzz ')
        elif lst[index_elem] % 7 == 0:
            print(lst[index_elem], 'fuzz')
        elif lst[index_elem] % 5 == 0:
            print(lst[index_elem], 'fizz')
        index_elem += 1
lst = range(1, 36)
fizz_fuzz(lst)
