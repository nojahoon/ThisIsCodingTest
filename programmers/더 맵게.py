from heapq import *


def solution(scoville, K):
    heapify(scoville)

    answer = 0

    while (len(scoville) > 1 and scoville[0] < K):
        smallest = heappop(scoville)
        smaller = heappop(scoville)

        heappush(scoville, smallest + smaller * 2)
        answer += 1

    if scoville[0] >= K:
        return answer
    else:
        return -1