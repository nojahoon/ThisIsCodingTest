def solution(dirs):
    pan = []
    distance = 0
    current_x = 0
    current_y = 0
    for move in  dirs:
        pre_x=current_x
        pre_y=current_y
        if move =='U':
            current_y+=1
        elif move =='L':
            current_x-=1
        elif move =='R':
            current_x+=1
        else:
            current_y-=1
        if current_x<-5 or current_x>5 or current_y<-5 or current_y>5:
            current_x=pre_x
            current_y=pre_y
            continue
        if [pre_x,pre_y,current_x,current_y] in pan:
            continue
        else:
            pan.append([pre_x,pre_y,current_x,current_y])
            pan.append([current_x,current_y,pre_x,pre_y])
            distance+=1
    return distance