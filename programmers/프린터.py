def solution(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        v = queue.pop(0)
        if any(v[1] < rest[1] for rest in queue):
            queue.append(v)
        else:
            answer+=1
            if v[0] == location:
                return answer