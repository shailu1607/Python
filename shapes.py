def rectangle():
    a = int(input("Enter the length(a) : "))
    b = int(input("Enter the breath(b) : "))
    c = a + b
    d = a * b
    print("\nPerimeter of the rectangle: ", 2 * c)
    print ("\nArea of the rectangle: ", d)


def square():
    a = int(input("Enter the side length(a) : "))
    print( "\nPerimeter of the square: ", 4 * a)
    print("\nArea of the square: ", a * a)


def triangle():
    a = int(input("Enter the side(a) : "))
    b = int(input("Enter the side(b) : "))
    c = int(input("Enter the side(c) : "))
    h = int(input("Enter the height(h) : "))
    x = a + b + c
    y = b * h
    print ("\nPerimeter of the triangle: ", x)
    print ("\nArea of the triangle: ", y / 2)


def circle():
    r = int(input("Enter the radius(r) : "))
    p = 22 / 7
    x = 2 * p * r
    y = p * r * r
    print("\nPerimeter of the circle: ", x)
    print("\nArea of the circle: ", y)


def rhombus():
    a = int(input("Enter the side(a) : "))
    b = int(input("Enter the diagonal-1(d1) : "))
    c = int(input("Enter the diagonal-2(d2) : "))
    y = b * c
    print("\nPerimeter of the rhombus: ", 4 * a)
    print("\nArea of the rhombus: ", y / 2)


def switch(num):
    if num == 1 :
        square()
        printfn()
    elif num==2:
        rectangle()
        printfn()
    elif num==3:
        triangle()
        printfn()
    elif num==4:
        circle()
        printfn()
    elif num==5:
        rhombus()
        printfn()
    else:
        print("Invalid command")
        printfn()

def printfn():
    print("\n1.Square\n2.Rectangle\n3.Triangle\n4.circle\n5.Rhombus")
    num = int(input("Enter the Choice : "))
    switch(num)

printfn()