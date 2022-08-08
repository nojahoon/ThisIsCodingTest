from collections import deque

def solution(prices):
    answer=[]
    queue = deque(prices)
    while queue:
        stock_price = queue.popleft()
        sec = 0
        for after_price in queue:
            sec+=1
            if after_price<stock_price:
                break
        answer.append(sec)
    return answer