# Task 3
def count_entering(str_1, str_2):
    counter = 0
    indx_input = -1
    indx_str_1 = 0
    indx_str_2 = 0

    while indx_str_1 < len(str_1):

        if str_1[indx_str_1] == str_2[indx_str_2]:

            if indx_input == -1:
                indx_input = indx_str_1

            elif indx_str_2 + 1 == len(str_2):
                counter += 1
                indx_input = -1
                indx_str_1 += 1
                indx_str_2 = 0

            else:
                indx_str_1 += 1
                indx_str_2 += 1

        else:

            if indx_input == -1:
                indx_str_1 += 1
                indx_str_2 = 0

            else:

                if len(str_2) != 1:
                    indx_str_1 = indx_input + 1
                    indx_str_2 = 0
                    indx_input = -1

                else:
                    indx_str_1 += 1

    if counter > 0:
        return counter

    else:
        return -1


print(count_entering("Hellllololo Python", "ll"))
