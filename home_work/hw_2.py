'''def rounding_float(x):
    if not isinstance(x, float) and not isinstance(x, int):
        return "Nan"
    elif type(x) == int:
        return float(x)
    elif isinstance(x, float):
        if x > 1000000:
            return "Inf"
        elif x < -1000000:
            return "-Inf"
        return round(x, 2)


result = rounding_float(555.3665)
print(result)
'''


# Task №7
def ternary_operator(a, b, c):
    val = b if a else c
    return val


result = ternary_operator(6 < 8, 105, 8)
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


'''# Task №10
def transformation(arg):
    if arg.isdigit() = False:
        return 0
    arg = float(arg)

    if arg == float("Infinity"):
        arg = 1000000
        return arg
    if arg == float("-Infinity"):
        arg = -1000000
        return arg
    if arg <= 1000000 or arg >= -1000000:
        return arg
    if arg > 1000000:
        return "infinity"
    if arg < -1000000:
        return "-infinity"


result = transformation('222bhh')
print(result)


str = "555hh5"
print(str.isdigit())

'''
'''
def process_number(value):
    if value.lower() == 'nan':
        return 0.0
    elif value.lower() == 'infinity':
        return 1000000.0
    elif value.lower() == '-infinity':
        return -1000000.0

    float_value = float(value)

    if float_value <= -1000000.0:
        return float('-inf')
    elif float_value < 1000000.0:
        return float_value
    else:
        return float('inf')
'''


# Task №11
def hundreds_decade_units(num, bol):
    if isinstance(num, str):
        print("You enter string")
    elif num == int(num) or float(num):
        if num != 0:
            units = abs(num) % 10
            if units > 0 and bol:
                print("1. " + str(units) + " units")
            elif not bol:
                print(str(units) + " units")
            decade = abs(num) % 100 // 10
            if decade > 0 and bol:
                print("2. " + str(decade) + " decade")
            elif not bol:
                print(str(decade) + " decade")
            hundreds = abs(num) // 100
            if hundreds > 0 and bol:
                print("3. " + str(hundreds) + " hundreds")
            elif not bol:
                print(str(hundreds) + " hundreds")

result = hundreds_decade_units(555, True)
if result:
    print(result)


'''out = str(units) + " units"
if bol:
    out = "1. " + out
print(out)'''
