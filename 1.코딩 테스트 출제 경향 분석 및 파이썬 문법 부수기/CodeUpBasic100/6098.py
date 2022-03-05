#10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.
size=10
x=2 #ant의 x좌표
y=2 #ant의 y좌표
maze = []


for i in range(size):
    row = list(map(int,input().split()))
    maze.append(row)


while(True):
    #먹이를 찾았다면 종료
    if(maze[y-1][x-1]==2):
        maze[y-1][x-1]=9
        break
    #오른쪽으로 갈 수 있다면 움직일 수 있다면 이동 (장애물이 없고 미로를 벗어나면 안됨)
    if(maze[y-1][x]!=1 and x-1<size):
        #개미가 있던 현재 위치를 9로 표시하고 실제 개미는 오른쪽으로 이동한다.
        maze[y-1][x-1]=9
        x += 1
    #오른쪽이 막혀있고 아래로 갈 수 있다면
    elif(maze[y][x-1]!=1 and y-1<size):
        # 개미가 있던 현재 위치를 9로 표시하고 실제 개미는 아래로 이동한다.
        maze[y-1][x-1]=9
        y+=1
    #움직일 수 없다면
    else:
        # 현재 위치를 기록하고 끝난다.
        maze[y-1][x-1]=9
        break


for i in range(size):
    for j in range(size):
        print(maze[i][j],end=' ')
    print('')
