def solution(cacheSize, cities):
    answer = 0

    exist = set()
    recent = []

    for city in cities:
        if city.lower() in exist:
            answer += 1
            recent.remove(city.lower())
            recent.append(city.lower())
        else:
            answer += 5
            exist.add(city.lower())
            recent.append(city.lower())
            if len(exist) > cacheSize:  # 캐시크기를 벗어나는경우
                if len(set(recent)) <= cacheSize:
                    continue
                else:
                    while len(set(recent)) > cacheSize:
                        recent.pop(0)
                    for each in exist:
                        if each not in recent:
                            exist.remove(each)
                            break
    return answer
