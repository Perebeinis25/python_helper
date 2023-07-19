
def for_statement():

    tuple_v1 = (547, "Python", True)
    list_v1 = [546, "I love python", tuple_v1]
    str_v1 = "Python is BS"
    range_v1 = range(19, -19, -6)

    for elem in tuple_v1:  # key word 'in' has not the same effect as word 'in' in this case '547 in tuple_v1'
        print(elem)

    for elem in list_v1:
        print(elem)

    for elem in str_v1:
        print(elem)

    for elem in range_v1:
        print(elem)





for_statement()
