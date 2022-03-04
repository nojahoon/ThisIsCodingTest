n = int(input())
index=1
while index<=n:
    if(index%3==0):
        index+=1
        continue
    else:
        print(index,end=' ')
        index+=1