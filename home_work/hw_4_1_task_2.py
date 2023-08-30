# Task 2
def entering(str_1, str_2):

    counter = -1
    indx_str_1 = 0
    indx_str_2 = 0
    while indx_str_1 < len(str_1):
        if str_1[indx_str_1] == str_2[indx_str_2] and indx_str_2 + 1 <= len(str_2):

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


print(entering("Hellllololo Python", "lo"))

