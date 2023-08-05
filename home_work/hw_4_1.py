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

    if len(str_2) == 1:

        while str_1[indx_str_1] != str_2:
            indx_str_1 += 1

            if str_1[indx_str_1] == str_2:
                return indx_str_1

    while indx_str_1 < len(str_1) and len(str_2) > 1:

        while str_1[indx_str_1] == str_2[indx_str_2] and str_1[indx_str_1 + 1] == str_2[indx_str_2 + 1]:
            if counter == -1:
                counter = indx_str_1

            indx_str_1 += 1
            indx_str_2 += 1

            if indx_str_2 + 1 == len(str_2):

                return counter

        else:

            indx_str_1 += 1
            indx_str_2 = 0
            counter = -1

    else:
        return -1


print(entering("Helolo Python", "l"))


# Task 3

def count_entering(str_1, str_2):

    result = 0
    indx_str_1 = 0
    indx_str_2 = 0

    if len(str_2) == 1:

        while str_1[indx_str_1] != str_2:
            indx_str_1 += 1

            if indx_str_1 == len(str_1):
                return result

            while str_1[indx_str_1] == str_2:
                result += 1
                indx_str_1 += 1

    while indx_str_1 < len(str_1):

            while str_1[indx_str_1] == str_2[indx_str_2] and str_1[indx_str_1 + 1] == str_2[indx_str_2 + 1]:

                indx_str_1 += 1
                indx_str_2 += 1

                if indx_str_2 + 1 == len(str_2):

                    indx_str_2 = 0
                    result += 1

            else:

                    indx_str_1 += 1
                    indx_str_2 = 0

    return result


print(count_entering("Hello world and hello python", "o"))


# Task 4
def placeholder_format(format_str, value):
    indx_str = 0
    indx_value = 0
    str_res = ""

    while indx_str + 1 < len(format_str):

        if format_str[indx_str] == '{' and format_str[indx_str + 1] == '}':

            if indx_value < len(value):
                str_res += str(value[indx_value])
                indx_str += 2
                indx_value += 1

            else:
                str_res += format_str[indx_str:]
                break

        if format_str[indx_str] != '{' or format_str[indx_str] != '}':
            str_res += str(format_str[indx_str])
            indx_str += 1
    else:
        str_res += str(format_str[-1])

    return str_res


format_str = "I { have  apples and  mellons , }"
value = [6, 5]
print(placeholder_format(format_str, value))


# Task 5
def index_placeholder(format_str, value):
    indx_str = 0
    indx_value = 0
    result = ""

    while indx_str + 1 < len(format_str):

        if format_str[indx_str] == format_str[-2] == '{':  # Gavno cod....
            result += str(format_str[indx_str:])
            break

        if format_str[indx_str] == '{' and format_str[indx_str + 2] == '}':
            idx = int(format_str[indx_str + 1])

            if idx < len(value):
                result += str(value[idx])
                indx_str += 3
                indx_value += 1

            else:
                result += str(format_str[indx_str])
                indx_str += 1
        else:
            result += str(format_str[indx_str])
            indx_str += 1
    
    else:
        result += str(format_str[-1])

    return result


format_str = "I have  apples and  mellons { "
value = [6, 5, 3, 10]
print(index_placeholder(format_str, value))


