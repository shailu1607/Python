d = {'mon':6,'tue':5,'wed':4,'thu':3,'fri':2,'sat':1}
day = input()
limit = int(input())
sunday = 1
week = 0
week = week+d[day]
while(week<limit):
    week+=7
    sunday+=1
print(sunday)