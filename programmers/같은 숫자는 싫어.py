def solution(arr):
    answer=[]
    length=len(arr)
    if length<=0:
        return
    answer.append(arr[0])
    for i in range(1,length):
        if arr[i]!=arr[i-1]:
            answer.append(arr[i])
    return answer