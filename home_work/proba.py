# Task_6
def special_values(list_1, list_2):
    list_result = []

    for i in list_1:
        var = 0
        for x in list_2:

            if x == i:
                if (not isinstance(x, bool) and not isinstance(i, bool)) or (isinstance(x, bool) and isinstance(i, bool)):
                    var = 1
                    break

        if var == 0:
            list_result.append(i)

    for i in list_2:
        var = 0
        for x in list_1:

            if x == i:
                if (not isinstance(x, bool) and not isinstance(i, bool)) or (isinstance(x, bool) and isinstance(i, bool)):
                    var = 1
                    break


        if var == 0:
            list_result.append(i)

    return list_result


list_1 = [0, 5, 6, True, 7, 9, 8, 1, False]
list_2 = [6, 7, 8, False, "Hello", 1, 0]
result = special_values(list_1, list_2)
print("# Task_6: ", result)


# Task_6
def special_values(list_1, list_2):
    list_result = []

    for i in list_1:
        var = 0
        for x in list_2:

            if x == i:
                if (not isinstance(x, bool) and not isinstance(i, bool)) or (isinstance(x, bool) and isinstance(i, bool)):
                    var = 1
                    break

        if var == 0:
            list_result.append(i)

    for i in list_2:
        var = 0
        for x in list_1:
            if i not in list_2:
                if (type(x) == int and type(i) == int) or (type(x) == bool and type(i) == bool):

                    list_result.append(i)
            if x == i:
                if (not isinstance(x, bool) and not isinstance(i, bool)) or (isinstance(x, bool) and isinstance(i, bool)):
                    var = 1
                    break


        if var == 0:
            list_result.append(i)

    return list_result


list_1 = [0, 5, 6, True, 7, 9, 8, 1, False]
list_2 = [6, 7, 8, False, "Hello", 1, 0]
result = special_values(list_1, list_2)
print("# Task_6: ", result)