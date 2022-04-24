# sum of two numbers without + operation
a = int(input())
b = int(input())


def addition(a, b):
    if b == 0:
        return a
    else:
        return addition(a ^ b, (a & b) << 1)


print(addition(a, b))
