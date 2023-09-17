
def placeholder_format(format_str, value):
    indx_str = 0
    indx_value = 0
    str_res = ""

    while indx_str + 1 <= len(format_str):

        if format_str[indx_str] != '{':
            str_res += format_str[indx_str]
            indx_str += 1

        else:
            indx_str += 1

            if indx_str == len(format_str):
                str_res += format_str[indx_str - 1]
                return str_res

            elif format_str[indx_str] == '}':
                str_res += str(value[indx_value])
                indx_value += 1
                indx_str += 1

                if indx_value == len(value):
                    str_res += format_str[indx_str:]
                    return str_res

            else:
                str_res += format_str[indx_str - 1]

    return str_res

format_str = "I {} {} {-} have  apples and  mellons , {{{{"
value = [6, 5, 2]
print(placeholder_format(format_str, value))