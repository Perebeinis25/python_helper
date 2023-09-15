def entering(str_1, str_2):

    counter = -1
    indx_str_1 = 0
    indx_str_2 = 0
    while indx_str_1 < len(str_1):
        if str_1[indx_str_1] == str_2[indx_str_2]:

            if counter == -1:
                counter = indx_str_1
                if len(str_2) == 1:
                    return counter
                indx_str_1 += 1
                indx_str_2 += 1
            elif indx_str_2 + 1 == len(str_2):
                return counter

            else:
                indx_str_1 += 1
                if indx_str_2 + 1 != len(str_2):
                    indx_str_2 += 1
                else:
                    indx_str_2 = 0

        else:

            if counter == -1:
                indx_str_1 += 1
                indx_str_2 = 0
            else:
                indx_str_1 = counter + 1
                indx_str_2 = 0
                counter = -1

    else:
        return -1


def count_entering(str_1, str_2):
    count = 0
    idx = 0

    while idx >= 0:
        idx = entering(str_1, str_2)

        if idx != -1:
            str_1 = str_1[idx + len(str_2):]
            count += 1

    return count


str_1 = "Hellooollololo Python"
str_2 = "lo"
print(count_entering(str_1, str_2))

