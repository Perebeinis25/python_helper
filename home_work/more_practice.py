def str_to_int(string):
    cycle_var = 1
    number_result = 0
    char_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

    for i in string[::-1]:

        for el in char_dict:

            if i == el:

                res = char_dict[el] * cycle_var
                number_result += res
                cycle_var *= 10

    return number_result


print(str_to_int("250650"))