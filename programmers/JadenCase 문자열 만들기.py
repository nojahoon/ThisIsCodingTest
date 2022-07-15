def solution(s):
    arr = list(s.split(' '))
    length = len(arr)
    for i in range(length):
        arr[i] = arr[i].capitalize()
    answer = " ".join(arr)
    return answer