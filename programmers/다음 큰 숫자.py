def solution(n):
    answer = 0
    n_count = bin(n).lstrip('0b').count('1')
    next = n+1
    while(True):
        larger_count = bin(next).lstrip('0b').count('1')
        if n_count==larger_count:
            answer=next
            break
        else:
            next+=1
    return answer