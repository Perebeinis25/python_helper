# Task №6
def rounding_float(x):
    if isinstance(x, int):
        x = float(x)
        return x
    if not isinstance(x, float):
        return "Nan"
    elif isinstance(x, float):
        if x > 1000000:
            return float('inf')
        elif x < -1000000:
            return "-Inf"

        rou_1 = (x * 10 // 1) / 10
        rounded_x = x * 10

        if (rounded_x % 1) >= 0.5:
            return  rou_1 + 0.1
        else:
            return rou_1


result = rounding_float(1.27)
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

    if prefix == '0b' or prefix == '0B':
        res = int(con, 2)
    elif prefix == '0x' or prefix == '0X':
        res = int(con, 16)
    elif prefix == '0o' or prefix == '0O':
        res = int(con, 8)
    elif prefix == '' or prefix == '0':
        res = int(con, 10)
    else:
        res = 0
    return res


result = ret_int("0r", "76")
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


result = transformation('555')  # "55hhh" - don't work with string like that.
if result:
    print(result)


# Task №11
def hundreds_decade_units(num, bol):
    if type(num) == str:
        print("You enter string")
    elif isinstance(num, float):
        num = int(num)
    if isinstance(num, int) and not 0:

        units = abs(num) % 10
        val_1 = units > 0 and bol
        ch_1 = str(units) + " units"

        if val_1:
            print("1. " + ch_1)
        elif not bol and units != 0:
            print(ch_1)

        decade = abs(num) % 100 // 10
        val_2 = decade > 0 and bol
        ch_2 = str(decade) + " decade"

        if val_2:
            print("2. " + ch_2) if val_1 else print("1. " + ch_2)
            # if val_1:
            #     print("2. " + str(decade) + " decade")
            # else:
            #     print("1. " + str(decade) + " decade")

        elif not bol and decade != 0:
            print(ch_2)

        hundreds = abs(num) // 100
        val_3 = hundreds > 0 and bol
        ch_3 = str(hundreds) + " hundreds"

        if val_3:

            if decade == 0 and units == 0:
                print("1. " + ch_3)
            elif (decade > 0 and units == 0) or (units > 0 and decade == 0):
                print("2. " + ch_3)
            elif decade != 0 and units != 0:
                print("3. " + ch_3)

        elif not bol and hundreds != 0:
            print(ch_3)


hundreds_decade_units(110, True)

'''out = str(units) + " units"
if bol:
    out = "1. " + out
print(out)'''
