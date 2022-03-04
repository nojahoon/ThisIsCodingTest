a , m , d , n =map(int, input().split())

count=a
for i in range(1,n):
    count= count*m+d

print(count)