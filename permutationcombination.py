import math

n = int(input("Enter the n value (n>r): "))
r = int(input("Enter the r value (n>r): "))
a = int(input("\n1.Permutation\n2.Combination\nChoose the operation : "))
x = n - r
n1 = math.factorial(n)
r1 = math.factorial(r)
x1 = math.factorial(x)
if a == 1:
    print("\n", n, "P", r, "=", n1 / r1)
else:
    if a == 2:
        print("\n", n, "P", r, "=", n1 / (r1 * x1))
    else:
        print("Invalid choice")
