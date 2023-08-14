# Task_2
def copy_list(original_list):

    new_list = original_list.copy()

    return new_list


original_list = [4, 9.3, "Hello", True]
print("# Task_2: ", original_list, type(original_list), id(original_list)) # different id
new_list = copy_list(original_list)
print("# Task_2: ", new_list, type(new_list), id(new_list))                # different id


# Task_3
def foo(original_list):

    new_list = []

    for i in original_list:

        if isinstance(i, list):
            new_list.append(i.copy())

        elif isinstance(i, tuple):
            temp = []

            for el in i:
                temp.append(el)
            new_list.append(tuple(temp))

        else:
            new_list.append(i)

    return new_list

original_list = [4, 9.3, (6, 7), "Hello", ["Python", "Lorem"], True]
print("# Task_3: ", original_list, id(original_list), id(original_list[2]))
result = foo(original_list)
print("# Task_3: ", result, type(result), id(result), id(result[2]))


# Task_4
def same_list(original_list):

    original_list[2] = original_list.copy()

    return original_list


original_list = [4, 9.3, "Hello", ["Python", "Lorem"], "Python", "Lorem", True]
print("# Task_4: ", original_list, id(original_list))   # id the same
new_list = same_list(original_list)
print("# Task_4: ", new_list, id(new_list))             # id the same


# Task_5
def remove_duplicates(original_list):

    index_now = 0

    while index_now < len(original_list):

        if original_list[index_now] in original_list[:index_now]:
            original_list.pop(index_now)
            index_now -= 1
        index_now += 1

    return original_list


original_list = [4, 6.6, False, True, True, False, "Python", "Python", "python"]
print("# Task_5: ", original_list, type(original_list), id(original_list)) # id the same
result = remove_duplicates(original_list)
print("# Task_5: ", result, type(result), id(result))                      # id the same


# Task_6
def special_values(list_1, list_2):   # it's not correct function because True == 1...9, False == 0
    list_result = []                  # I need help with it

    for i in list_1:
        if i not in list_2:
            list_result.append(i)
    for c in list_2:
        if isinstance(c, bool):
            if bool not in list_2:
                list_result.append(c)
        if c not in list_1:
            list_result.append(c)
    return list_result


list_1 = [5, 6, 7, 8, 9, 1, 0]
list_2 = [6, 7, 8, True, False, "Hello", 1]
result = special_values(list_1, list_2)
print("# Task_6: ", result)


# Task_7
def count_symbols(input_str):

    list_result = []
    input_str = input_str.lower()

    for symbol in input_str:
        tuple_in_list = (symbol, input_str.count(symbol))

        if tuple_in_list not in list_result:
            list_result.append(tuple_in_list)

    return list_result


result = count_symbols("Google")
print("# Task_7: ", result)


# Task_8
def count_number(input_str):
    result = 0

    for item in input_str:

        if item.isdecimal():
            result += 1

    return result


input_str = "I have 32 apples and 345 mellons"
result = count_number(input_str)
print("# Task_8: ", result)


# Task_9
def countng(general_str, entering_str):

    if entering_str in general_str:
        var = general_str.count(entering_str)
        return var


general_str = "Hello world and hello python"
entering_str = "Hello world"
result = countng(general_str, entering_str)
print("# Task_9: ", result)


# Task_10
def count_words(input_str):

    list_result = []
    input_str = input_str.lower().split()


    for item in input_str:
        tuple_in_list = (item, input_str.count(item))

        if tuple_in_list not in list_result:
            list_result.append(tuple_in_list)

    return list_result


input_str = "Hello hello hellO world y"
result = count_words(input_str)
print("# Task_10: ", result)

