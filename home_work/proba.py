
def entering(str_1, str_2):

    result = 0
    indx_str_1 = 0
    indx_str_2 = 0

    while indx_str_1 < len(str_1):
        temp_idx = indx_str_1

        while str_1[temp_idx] == str_2[indx_str_2]:
            indx_str_1 = temp_idx
            temp_idx += 1
            indx_str_2 += 1

            if indx_str_2 == len(str_2):
                indx_str_2 = 0
                result += 1



        indx_str_1 += 1
    return result

# print(entering("Hello world and hello python", "lo"))
print(entering("Helolo", "lo"))
