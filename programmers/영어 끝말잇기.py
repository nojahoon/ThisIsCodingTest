def solution(n, words):
    dict = {}
    for i in range(0,len(words)):
        who = i%n+1
        order = i//n+1
        if i!=0 and words[i-1][-1] != words[i][0]:
            return [who,order]
        if words[i] in dict:
            return [who,order]
        else:
            dict[words[i]]=1
    return [0,0]