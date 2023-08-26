# Task 3
def count_symbols(str_arg):
    value_index = 0
    key_list = []
    value_list = []
    list_result = []

    for i in str_arg:

        if i not in value_list:
            key_list.append(str_arg.count(i))
            value_list.append(i)
        else:
            continue

    for i in key_list:
        result = f"{i} - {value_list[value_index]}"
        list_result.append(result)
        value_index += 1

    return list_result

print("# Task_3: ", count_symbols("Hello="))

# Task_4
def count_words(input_str):

    split_word = input_str.split()
    value_index = 0
    key_list = []
    value_list = []
    list_result = []

    for i in split_word:

        if i not in value_list:
            key_list.append(split_word.count(i))
            value_list.append(i)
        else:
            continue

    for i in key_list:
        result = f"\'{value_list[value_index]}\' - {i}"
        list_result.append(result)
        value_index += 1

    return list_result


input_str = "Hello hello hellO world y x"
result = count_words(input_str)
print("# Task_4: ", result)


# Task_5
def dict_union(dict_1, dict_2):
    list1 = list()
    list1.extend(dict_1.values())
    list1.extend(dict_2.values())

    union = dict_1 | dict_2
    total_len = len(dict_1) + len(dict_2)

    for i in dict_1:

        if i in dict_2:
            var = dict(zip((range(0, total_len)), list1))
            return var

    else:
        return union


dict_1 = {17: "Hello", 22: "world", 23: "Python", 45: "Python"}
dict_2 = {3: "hello", 4: "world", 5: "python"}
result = dict_union(dict_1, dict_2)
print("# Task_5: ", result)

# Task_6
def dict_union(dict_1, dict_2):
    list1 = list(dict_1.keys())
    key = 0
    for i in list1:

        if i in dict_2:
            for el in dict_2:
                if el not in dict_1:
                    dict_1.update({el: dict_2[el]})
                else:
                    dict_1.update({key: dict_2[el]})
                    while key in dict_1 or key in dict_2 or key == 0:
                        key += 1
            break
    else:
        no_coincidence = dict_1 | dict_2
        return no_coincidence

    return dict_1


dict_1 = {105: "Hello", 2: "Yra", 53: "Python", 5: "is", 10: "the"}
dict_2 = {1: "best", 2: "thing", 3: "except", 5: "Igor`s", 53: "Python", 84: "lessons"}
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

