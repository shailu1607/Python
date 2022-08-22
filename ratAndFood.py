r = 7
unit = 2
n = 8 
a = [2,8,3,5,7,4,1,2]
food=r*unit
sum1=0
count =0
for i in a:
    sum1 += i 
    count +=1
    if(sum1>food):
        break
    
print(count)