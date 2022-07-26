def solution(n):
    answer=0
    for i in range(1,n+1):
        count=0
        for j in range(i,n+1):
            count+=j
            if count==n:
                answer+=1
                break
            elif count>n:
                break
    return answer