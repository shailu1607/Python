def calc_exp(base1, exp):
    if exp > 0 :
        t1 = base1 ** exp
        return t1
    else :
        stmt = "Invalid"
        return stmt

base1 = int(input("Enter the base value : "))
exp = int(input("Enter the exponential value : "))
print("The exponential of given base is ",calc_exp(base1, exp))
