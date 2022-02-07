def eval_quad_eqn(a, b, c, x):
    x2 = x * x
    a1 = a * x2
    b1 = b * x
    t = a1 + b1 + c
    return t

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
x = int(input("Enter x : "))
print("The solution of quadratic equation of form ax^2 + bx + c is ", eval_quad_eqn(a, b, c, x))
