# Task 1
def difference(str_1, str_2):

    indx_str_1 = 0
    indx_str_2 = 0

    if len(str_1) == len(str_2):

        while indx_str_1 < len(str_1):

            if str_1[indx_str_1] != str_2[indx_str_2]:

                return False

            if str_1[indx_str_1] == str_2[indx_str_2]:

                indx_str_1 += 1
                indx_str_2 += 1

        return True

    else:
        return False


print(difference("Python", "PyThon"))


# Task 2
def entering(str_1, str_2):

    counter = -1
    indx_str_1 = 0
    indx_str_2 = 0

    while indx_str_1 < len(str_1):

        if str_1[indx_str_1] == str_2[indx_str_2]:

            if counter == -1:
                counter = indx_str_1

            indx_str_1 += 1
            indx_str_2 += 1

            if indx_str_2 == len(str_2):

                return counter

        elif str_1[indx_str_1] != str_2[indx_str_2]:
            indx_str_1 += 1
            indx_str_2 = 0
            counter = -1

    else:
        return -1


print(entering("Hello Python", "Hello Py"))


# Task 3
def count_entering(str_1, str_2):
    result = 0
    indx_str_1 = 0
    indx_str_2 = 0

    while indx_str_1 < len(str_1):

        if str_1[indx_str_1] == str_2[indx_str_2]:

            indx_str_1 += 1
            indx_str_2 += 1

            if indx_str_2 == len(str_2):

                indx_str_2 = 0
                result += 1

        elif str_1[indx_str_1] != str_2[indx_str_2]:

            indx_str_1 += 1
            indx_str_2 = 0

    return result


print(count_entering("Hello world and hello python", "ello"))


# Task 4
def playsholder(str_1, list_1):
    indx_str = 0
    indx_list = 0
    str_res = ""

    while indx_str + 1 < len(str_1):

        if str_1[indx_str] == '{' and str_1[indx_str + 1] == '}':

            if indx_list < len(list_1):
                str_res += str(list_1[indx_list])
                indx_str += 2
                indx_list += 1

            else:
                str_res += str_1[indx_str:]
                break

        if str_1[indx_str] != '{' or str_1[indx_str] != '}':
            str_res += str(str_1[indx_str])
            indx_str += 1

    return str_res


str_1 = "I { have {} apples and {} mellons {}, {}"
list_1 = [6, 0]
print(playsholder(str_1, list_1))


# Task 5
def index_playsholder(str_1, list_1):
    indx_str = 0
    indx_list = 0
    result = ""

    while indx_str + 1 < len(str_1):

        if str_1[indx_str] == '{' and str_1[indx_str + 2] == '}':
            idx = int(str_1[indx_str + 1])

            if idx < len(list_1):
                result += str(list_1[idx])
                indx_str += 3
                indx_list += 1

            else:
                result += str(str_1[indx_str])
                indx_str += 1
        else:
            result += str(str_1[indx_str])
            indx_str += 1

    return result


str_1 = "I have {3} apples and {1} mellons {0} "
list_1 = [6, 5, 3, 10]
print(index_playsholder(str_1, list_1))


