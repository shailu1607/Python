# substraction of two numbers without - operation
a = int(input())
b = int(input())


def subtraction(a, b):
    if b == 0:
        return a
    else:
        return subtraction(a ^ b, (~a & b) << 1)


print(subtraction(a, b))
