from collections import deque


def solution(people, limit):
    answer = 0

    #오름차순으로 정렬한다.
    people.sort()
    queue = deque(people)

    while (queue):
        length = len(queue)
        if length == 0:
            break
        if length == 1:
            answer += 1
            break

        #보트에 2명이 탈 수 있으면 태우고, limit을 넘으면 몸무게 큰 사람만 태운다.
        if queue[length - 1] + queue[0] <= limit:
            queue.pop()
            queue.popleft()
        else:
            queue.pop()
        answer+=1

    return answer
