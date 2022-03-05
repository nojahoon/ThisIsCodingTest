pan = []
size=19 #19*19
for i in range(size):
    row=list(map(int,input().split()))
    pan.append(row)

n = int(input())

for i in range(n):
    x , y = map(int, input().split())
    for j in range(size):
        if (pan[x-1][j]==0):
            pan[x - 1][j] =1
        else:
            pan[x - 1][j]=0
    for k in range(size):
        if (pan[k][y-1]==0):
            pan[k][y-1] =1
        else:
            pan[k][y-1]=0


for i in range(size):
    for j in range(size):
        print(pan[i][j],end=' ')
    print('')