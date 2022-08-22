s = input()
count_s = 0
count_h = 0
count_o = 0
for i in range(len(s)):
    if(s[i]=="*"):
        count_s +=1
    else:
        if(s[i]=="#"):
            count_h +=1 
        else:
            count_o +=1

if(count_s==count_h):
    print("0")
else:
    if(count_h>count_s):
        print("-1")
    else:
        print("+1")