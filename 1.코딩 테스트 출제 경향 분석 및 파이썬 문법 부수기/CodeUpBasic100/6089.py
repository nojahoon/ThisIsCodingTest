a , r , n = map(int,input().split())

answer=0
mul=a
for i in range(1,n):
    if(n==1):
        answer=a
    else:
        mul*=r
print(mul)

