# Task 3
def count_symbols(str_arg):

    result = 0

    for i in str_arg:
        result += 1

    return result

print("# Task_3: ", count_symbols("Hello="))

# Task_4
def count_words(input_str):

    result = len(input_str.split())

    return result


input_str = "Hello hello hellO world y x"
result = count_words(input_str)
print("# Task_4: ", result)


# Task_5
def dict_union(dict_1, dict_2):

    union = dict_1 | dict_2

    for i in dict_1:

        if i in dict_2:
            var = dict(zip(range(0, len(union)), (union.values())))
            return var

    else:
        return union


dict_1 = {1: "Hello", 2: "world", 3: "Python"}
dict_2 = {3: "hello", 4: "world", 5: "python"}
result = dict_union(dict_1, dict_2)
print("# Task_5: ", result)

# Task_6
def dict_union(dict_1, dict_2):

    key_list = list(range(len(dict_1) + len(dict_2)))
    print(key_list)
    for i in dict_1:
        if i in dict_2 or i not in dict_2:
            key_list.remove(i)
    print(key_list)
    dict_3 = dict_1 | dict(zip(key_list, (dict_2.values())))

    return dict_3


dict_1 = {1: "Hello", 2: "world", 3: "Python", 4: "Python"}
dict_2 = {1: "hello", 2: "world", 3: "python"}
result = dict_union(dict_1, dict_2)
print("# Task_6: ", result)


# Task_7
def statistic(str_arg):
    split_words = str_arg.split()
    new_dict = {}

    for word in split_words:
        key = len(word)

        if key in new_dict:
            new_dict[key].append(word)

        else:
            new_dict[key] = [word]

    new_list = list(new_dict.keys())

    for item in new_list:
        if len(new_dict[item]) < 2:
            new_dict.pop(item)

    return new_dict


str_arg = "Hello how are you ? I'm ok thank you. How old are you ? I'm 27 kj;j;jkjghhg"
result = statistic(str_arg)
print("# Task_7: ", result)

