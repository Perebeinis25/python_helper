def fun_1():
    result = "No arguments, no return"
    print("fun_1:", result)


fun_1()


def fun_2(x, y):
    return 1


res = fun_2(2, 5)
print("fun_2:", res)


def fun_3():
    return


res = fun_3()
print("fun_3:", res)


def fun_4(x, y):
    return x - y


result = fun_4(25, 20)
print("fun_4:", result)



def fun_5(x, y):
    return x - y


result = fun_5(fun_5(5, 9), fun_5(8, 2))
print("fun_5:", result)




