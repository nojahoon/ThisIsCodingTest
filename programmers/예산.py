def solution(d, budget):
    d.sort(reverse=True)
    count=0
    while(d and d[-1] <= budget):
        budget-=d.pop()
        count+=1
    return count