import sys

n = int(sys.stdin.readline())
stk = []
for _ in range(n):
    command = sys.stdin.readline().split()
    if 'push' in command:
        push = command[1]
        stk.append(push)
    if 'pop' in command:
        if stk:
            print(stk.pop())
        else:
            print(-1)
    if 'size' in command:
        print(len(stk))
    if 'empty' in command:
        if stk:
            print(0)
        else:
            print(1)
    if 'top' in command:
        if stk:
            print(stk[-1])
        else:
            print(-1)

