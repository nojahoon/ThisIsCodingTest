def solution(numbers):
    answer = 0

    for i in range(0, 10, 1):
        if i not in numbers:
            answer += i

    return answer