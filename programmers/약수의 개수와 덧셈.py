def solution(left, right):
    #if number of divisor ==> odd: -
    #if number of divisor ==> even: +
    answer = 0
    for i in range(left,right+1,1):
        divisor_count=0
        for j in range(1,i+1,1):
            if i%j == 0:
                divisor_count+=1
        if divisor_count%2==0:
            answer+=i
        else:
            answer-=i
    return answer