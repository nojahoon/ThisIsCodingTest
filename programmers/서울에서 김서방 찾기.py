def solution(seoul):
    length = len(seoul)
    for i in range(length):
        if seoul[i]=="Kim":
            return "김서방은 "+str(i)+"에 있다"