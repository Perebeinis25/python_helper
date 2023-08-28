# Task 3
def count_symbols(str_arg):
    result = {}

    for char in str_arg:
        key = str_arg.count(char)
        result[char] = key

    return result


print("# Task_3: ", count_symbols("Hello="))


# Task_4
def count_words(input_str):
    result = {}
    split_word = input_str.split()

    for word in split_word:
        key = split_word.count(word)
        result[word] = key

    return result


input_str = "Hello hello hellO world y x"
result = count_words(input_str)
print("# Task_4: ", result)


# Task_5
def dict_union(dict_1, dict_2):
    union = dict_1 | dict_2
    set_keys_dict_1 = set(dict_1)
    set_keys_dict_2 = set(dict_2)

    total_len = len(dict_1) + len(dict_2)

    list_value = []

    list_value.extend(dict_1.values())
    list_value.extend(dict_2.values())
    check = set_keys_dict_1.isdisjoint(set_keys_dict_2)

    if not check:
        var = dict(zip((range(0, total_len)), list_value))
        return var

    else:
        return union


dict_1 = {17: "Hello", 2: "world", 3: "Python", 45: "Python"}
dict_2 = {3: "hello", 2: "world", 5: "python"}
result = dict_union(dict_1, dict_2)
print("# Task_5: ", result)


# Task_6
def dict_union(dict_1, dict_2):
    set_keys_dict_1 = set(dict_1)
    set_keys_dict_2 = set(dict_2)
    key = 0
    intersect = set_keys_dict_1.intersection(set_keys_dict_2)

    for j in dict_2:
        if j in intersect:

            while key in dict_1 or key in dict_2:
                key += 1
            dict_1[key] = dict_2[j]
            key += 1

        else:
            dict_1[j] = dict_2[j]

    else:
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

