def solution(clothes):
    dict={}
    count=1
    for cloth in clothes:
        if cloth[1] in dict.keys():
            dict[cloth[1]] +=1
        else:
            dict[cloth[1]] = 1
    for key in dict.keys():
        count*=dict[key]+1
    count-=1
    return count