def solution(N, stages):
    dict = {}
    for i in range(1,N+1,1):
        on_stage_not_cleared_count = 0
        cleared_count = 0
        for each in stages:
            if each == i:
                on_stage_not_cleared_count+=1
            if each >= i:
                cleared_count+=1
        if cleared_count==0:
            failure = 0
        else:
            failure = on_stage_not_cleared_count/cleared_count
        dict[i] = failure
    return sorted(dict,key = lambda x : dict[x] , reverse=True)

print(solution(5,([2, 1, 2, 6, 2, 4, 3, 3])))