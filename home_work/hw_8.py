# Task_1
def exept_three():

    for i in range(1, 10):
        if i % 3 == 0:
            continue
        print(i)


print("Task_1: ")
exept_three()

# Task_2
def exept_pair_number():

    for i in range (1, 10):
        if i % 2 == 0:
            continue
        print(i)


print("Task_2: ")
exept_pair_number()

# Task_3
def three_five_seeven():

    for i in range (1, 100):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            continue
        print(i)


print("Task_3: ")
three_five_seeven()

# Task_4
def range_exeption(range_arg):

    for i in range(1, 50):

        for el in range_arg:
            if i % el == 0:
                break

        else:
            print(i)


range_arg = range(3, 8)
print("Task_4: ")
range_exeption(range_arg)



# Task_5
def palindrom():

    for i in range(1, 100):
        i = str(i)
        if i == i[::-1] and int(i) > 9:
            break
        else:
            print(i)

print("Task_5: ")
palindrom()