def fibanocci(num1):
    a = 1
    b = 1
    print(a)
    print(b)
    i = 1
    if num1 == 0 | num1 ==1:
        return 1
    else:
        while i < num1 :
            temp = a+b
            print(temp)
            a = b
            b = temp
            i = i+1
        return 0

num1 = int(input("series to be printed :"))
fibanocci(num1)