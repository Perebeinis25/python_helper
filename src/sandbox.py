
tuple_v1 = (547, "Python", True)
list_v1 = [546, "I love python", tuple_v1]
str_v1 = "Python is BS"
range_v1 = range(39, -57, -6)

for tuple_elem in list_v1:
    print(list_v1)

for tuple_elem in range_v1:  # key word 'in' has not the same effect as word 'in' in this case '547 in tuple_v1'
    print(tuple_elem)

concat_collection = list_v1 + list(tuple_v1)
concat_collection_len = len(list_v1) + len(tuple_v1)

for list_indx in range(0, concat_collection_len):
    if list_indx % 2:
        print(concat_collection[list_indx])



list_v1 = ["8849", "Python", 0, 63, 1, True, "8849"]
#           0        1       2  3   4    5      6

print(list_v1[5])

list_len = len(list_v1)

if 7 < list_len:
    print(list_v1[7])


def nested_loops2():

    matrix = [[754, 743, 803, 783],
              [854, 243, 303, 983],
              [954, 943, 503, 873],
              [354, 343, 103, 738]]

    # print()
    for row in matrix:

        row_elems = ""
        elem_index = 0
        for elem in row:

            row_elems = row_elems + str(elem) + ", "
            elem_index = elem_index + 1
            if elem_index == len(row):
                row_elems = row_elems[:-2]

        print(row_elems)


nested_loops2()
