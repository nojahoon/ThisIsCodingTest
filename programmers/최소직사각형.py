def solution(sizes):
    mx , my = 0 , 0
    for each in sizes:
        each.sort()
        mx = max(mx,each[0])
        my = max(my,each[1])
    return mx*my