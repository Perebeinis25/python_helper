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
'''
def shablon(pol):
    sha = ('NNNN-NNNN-NNNN')
    for i in sha:
        if i == 'N':
            print(pol[0])
        if i == '-':
            print(i)

pol = ('12551644644561')
result = shablon(pol)
print(result)'''

'''
def matrix(lst):
    a = []
    b = []
    c = []
    for i in lst:
        if [i] < [4]:
            a.append(i)
        if [7] > [i] > [3]:
            b.append(i), '\n'
        if [i] > [6]:
            c.append(i)

    return a, b, c
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = matrix(lst)
print(result)
'''

# list_res = list(range(2,6))
# print(list_res)
# # list_res[2]
# list_res[2] = 6
# print(list_res)



# Task_4
def foo(range_arg, list_arg):
    for i in range_arg:
        for z in list_arg:
            if i % z == 0:
                print(z)


range_arg = range(1, 7)
list_arg = [2, 3, 4, 5, 7]
result = foo(range_arg, list_arg)
print(result)


print(input("Введіть число"))
