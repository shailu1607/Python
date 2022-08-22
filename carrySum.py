def func(a,b):
    temp=a
    temp1=b 
    end = 0
    sum1 = 0
    l1=[0]
    while(temp>0):
        n = (temp%10)
        m = (temp1%10)
        sum1= n+m+l1[0]
        if(sum1>9):
            x = str(sum1)
            l = int(x[0])
            l1.append(l)
            l1.remove(l1[0])
            end+=l
            #print(x)
        temp=temp//10
        temp1=temp1//10
        sum1=0
    print(end)


a = 451
b = 349
if(len(str(a))==len(str(b))):
    func(a,b)
    