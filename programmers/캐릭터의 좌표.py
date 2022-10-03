def solution(keyinput, board):
    dic = { 'left':[-1,0] , 'right':[1,0] , 'up':[0,1] , 'down':[0,-1] }
    x=0
    y=0
    for key in keyinput:
        dx = x + dic[key][0]
        dy = y + dic[key][1]
        if abs(dx) > board[0]/2 or abs(dy) > board[1]/2:
            continue
        else:
            x = dx
            y = dy
    return [x,y]