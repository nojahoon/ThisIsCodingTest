def solution(numbers):
    answer = []

    # 직접 푼 풀이는 마지막 테케 2개가 시간초과 난다.
    # for number in numbers:
    #     second = int(number)
    #     isFind=False
    #     while(not isFind):
    #         second+=1
    #         result = number ^ second
    #         if 1<=bin(result).lstrip('0b').count('1')<=2:
    #             isFind=True
    #             answer.append(second)

    #다른 풀이
    for x in numbers:
        x = int(x)
        arr = list('0'+bin(x)[2:])
        index = ''.join(arr).rfind('0')
        arr[index] = '1'
        if x % 2 != 0:
            arr[index+1] = '0'
        answer.append(int(''.join(arr), 2))
    return answer