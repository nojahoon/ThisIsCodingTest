n = int(input())
call = input().split()
for i in range(n):
    call[i]=int(call[i])

min = call[0]
for i in range(n):
    if call[i]<min:
        min=call[i]

print(min)