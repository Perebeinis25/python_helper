# Task 1
def print_args(*vargs, **kwargs):

    for item in vargs:
        print(item)
    for el in kwargs:
        print(kwargs[el])


args_list = [6, 4, 3, 'Hello', (3, 6)]
args_dict = {"key": "Python"}
print("# Task 1: ")
print_args(*args_list, **args_dict)

# Task 2
def print_to_number(num):

    if num <= 0:
        print(0)
        return 0
    print(num)

    return num - print_to_number(num - 1)

print("# Task 2: ")
print_to_number(3)


# Task 3
def count_value(int_value_list, index):

    if index == len(int_value_list) - 1:
        return int_value_list[index]
    # print(int_value_list[index])
    return int_value_list[index] + count_value(int_value_list, index + 1)


int_value_list = [1, 2, 3]
result = count_value(int_value_list, 0)
print("# Task 3: ", result)

# Task 4
def max_value(int_value_list, max_number=0):

    if not int_value_list:
        return max_number
    first_element = int_value_list[0]
    if max_number == 0 or first_element > max_number:
        max_number = first_element

    return max_value(int_value_list[1:], max_number)


int_value_list = [5, 7, 2, 17]
result = max_value(int_value_list)
print("# Task 4: ", result)