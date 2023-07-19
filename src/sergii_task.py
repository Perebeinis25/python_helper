'''def card_number(num):
    if type(num) == int(num) or type(num) == float(num):
        num = str(num)
    if type(num) == str(num):
        range(num)


first_part = number[:4]
first_part = str(first_part)

second_part = number[4:10]
second_part = str(second_part)

third_part = number[10:]
third_part = str(third_part)

print(first_part + '-' + second_part + '-' + third_part)

result = card_number('1294954321321316')
print(result)'''

def shablon(pol):
    sha = ('NNNN-NNNN-NNNN')
    for i in sha:
        if i == 'N':
            print(pol[0])
        if i == '-':
            print(i)

pol = ('12551644644561')
result = shablon(pol)
print(result)

def fun_list_concat(li_1):
    separation = ""
    for i in li_1:
        separation = separation + i
    return separation


li_1 = ["I ", "love ", "python ", "very ", "much !"]
result = fun_list_concat(li_1)
print(result)


def fun_list_num(li_2):
    separation = li_2[0]
    for i in li_2[1:]:
        # num = int(i)
        separation = separation + i
        # print(i)    # x = list_str[0] + list_str[1] + list_str[2] + list_str[3] + list_str[4]
    return separation


li_2 = [1, 2, 3]
result = fun_list_num(li_2)
print(result)
