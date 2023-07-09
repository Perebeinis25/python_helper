# Task №6
def rounding_float(x):
    if isinstance(x, int):
        x = float(x)
        return x
    if not isinstance(x, float):
        return "Nan"
    elif isinstance(x, float):
        if x > 1000000:
            return "Inf"
        elif x < -1000000:
            return "-Inf"
        rounded_x = (x * 10 // 1) / 10  # Vkrav bo sam by ne dodumavcia. Ale rozibravsya yak vono pratciuye
        return rounded_x


result = rounding_float(-1000000000000)
print(result)


# Task №7
def ternary_operator(a, b, c):
    val = b if a else c
    return val


result = ternary_operator(10 < 8, 105, 8)
print(result)


def ternary_operator(a, b, c):
    if a:
        return b
    else:
        return c


result = ternary_operator(6 < 8, 105, 8)
print(result)


# Task №8
def multiply(base1, num1, base2, num2):
    var1 = int(num1, base1)
    var2 = int(num2, base2)
    return var1 * var2


result = multiply(16, "0xAF47", 2, '0b10101')
print("fun_2:", result)


# Task №9
def ret_int(prefix, num):
    con = prefix + num
    res = int(con, 16)
    return res


result = ret_int("0x", "FF32")
print("fun_2:", result)


# Task №10
def transformation(arg):
    if arg == str(arg):
        arg = float(arg)
        if arg != arg:  # Stole this part. Check if arg is nan.
            return 0.0
        if arg == float("inf"):
            arg = 1000000
            return arg
        if arg == float("-Infinity"):
            arg = -1000000
            return arg
        if (1000000 >= arg > -1000000) or (-1000000 <= arg < 1000000):
            return arg
        if arg > 1000000:
            return "infinity"
        if arg < -1000000:
            return "-infinity"
    else:
        print('You enter not string')


result = transformation('5555e55555555')  # "55hhh" - don't work with that.
print(result)


# Task №11
def hundreds_decade_units(num, bol):
    if isinstance(num, str):
        print("You enter string")
    elif isinstance(num, float):
        num = int(num)
    if isinstance(num, int) and not 0:
        units = abs(num) % 10
        if units > 0 and bol:
            print("1. " + str(units) + " units")
        elif not bol and units != 0:
            print(str(units) + " units")
        decade = abs(num) % 100 // 10
        if decade > 0 and bol:
            print("2. " + str(decade) + " decade")
        elif not bol and decade != 0:
            print(str(decade) + " decade")
        hundreds = abs(num) // 100
        if hundreds > 0 and bol:
            print("3. " + str(hundreds) + " hundreds")
        elif not bol and hundreds != 0:
            print(str(hundreds) + " hundreds")


hundreds_decade_units(222.55, True)

'''out = str(units) + " units"
if bol:
    out = "1. " + out
print(out)'''
