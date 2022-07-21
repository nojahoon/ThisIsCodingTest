def solution(board, moves):
    stk = []
    deleted_dolls = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] == 0:
                continue
            else:
                if not stk:
                    stk.append(board[i][move - 1])
                else:
                    if stk[-1] == board[i][move - 1]:
                        stk.pop()
                        deleted_dolls += 2
                    else:
                        stk.append(board[i][move - 1])
                board[i][move-1]=0
                board[i].append(0)
                break
    return deleted_dolls