# multiplication of two numbers without * operation
def multiply(a, b):
    if (b == 0):
        return 0
    elif (b > 0):
        return a + multiply(a, b - 1)
    else:
        return -multiply(a, -b)


a = int(input())
b = int(input())
print(multiply(a, b))
