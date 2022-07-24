def solution(arr, divisor):
    answer=[]
    for number in arr:
        if number%divisor==0:
            answer.append(number)
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer