# Task_2
def arrow(num):
    if num % 2 != 0:
        num_idx = 0
        while num_idx < (num / 2):
            num_idx += 1
            print(num_idx * "*")
        # while num_idx > 1:                                    # Sergii suport
        while num_idx > (num / 2) or 2 <= num_idx < (num / 2):  # its my decision
            num_idx -= 1
            print(num_idx * "*")
    else:
        i = 0
        while i < num:
            i += 1
        # for i in range(num):
            print(num * "* ")

arrow(10)



# Task_3
def fibonachi(num):
    first_dod = 3
    second_dod = 2
    print(first_dod)

    while first_dod + second_dod <= num:

        result = first_dod + second_dod
        print(result, '\n', end="")

        empty_var = first_dod
        first_dod = result
        second_dod = empty_var


fibonachi(26)


# Task_4
def foo(range_arg, list_arg):
    for i in range_arg:
        for z in list_arg:
            if i % z == 0:
                print(i)


range_arg = range(1, 7)
list_arg = [2, 3, 4, 5, 7]
result = foo(range_arg, list_arg)
print(result)


#Task_5
def reunion(list_arg):
    counter = 0

    for list_elem in list_arg:

        if isinstance(list_elem, tuple) or isinstance(list_elem, list):
            counter += len(list_elem)
        else:
            counter += 1

    list_res = list(range(counter))

    i = 0

    for list_elem in list_arg:

        if isinstance(list_elem, tuple) or isinstance(list_elem, list):

            for nested_elem in list_elem:
                list_res[i] = nested_elem
                i += 1

        else:
            list_res[i] = list_elem
            i += 1

    return list_res


list_arg = [72, "Python", ("hello", True), 73.5, ("hello", True)]
result = reunion(list_arg)
print(result)



