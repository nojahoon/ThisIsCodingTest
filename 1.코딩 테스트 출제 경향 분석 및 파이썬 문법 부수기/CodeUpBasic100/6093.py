n = int(input())
call = input().split()

for i in range(n):
    call[i] = int(call[i])

for i in range(n-1,-1,-1):
    print(call[i] , end=' ')
