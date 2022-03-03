n = int(input())
index=0
count=0
while(index<=n):
    if index%2==0:
        count+=index
    index+=1
print(count)
