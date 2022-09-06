def solution(brown, yellow):
    for i in range(1,yellow+1,1):
        if yellow % i==0:
            larger = max(yellow//i,i)
            smaller = min(yellow//i,i)
            if( (larger+2)*2 + (smaller+2)*2-4 )==brown:
                return [larger+2,smaller+2]