#division of two numbers without * operation
def divi(a,b):
    if(b==0):
        return "infinity"
    else:
        c=0
        while(a>=b):
            a = a-b
            c += 1
        print ("Quotient",c,"\nReminder",a)
a = int(input())
b = int(input())
print(divi(a,b))