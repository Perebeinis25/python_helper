def rounding_float(x):
    if x == int:
        x = float(x)
        return x
    '''if x != float:
        return "Nan"'''
    if x == float(x):
        return x // 10
    if x == float(x) > 1000000000:
        return "Inf"
    if x == float(x) < 1000000000:
        return "-Inf"


some = rounding_float(5.22)
print(some)
