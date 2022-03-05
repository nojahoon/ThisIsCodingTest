h ,w = map(int,input().split())
n = int(input())

#격자판 생성
pan = [[0]*w for _ in range(h)]

for i in range(n):
    l,d,x,y = map(int,input().split())
    for j in range(l):
        if d==0:    #가로방향
            if y+j<=w:
                pan[x-1][y-1+j]=1
        elif d==1:  #세로방향
            if x+j<=h:
                pan[x-1+j][y-1]=1

for i in range(h):
    for j in range(w):
        print(pan[i][j] , end=' ')
    print('')