#최소공배수로 안풀어보기를 권장하는문제

a,b,c = map(int,input().split())

day=1

while(day%a!=0 or day%b!=0 or day%c!=0):
    day+=1
print(day)