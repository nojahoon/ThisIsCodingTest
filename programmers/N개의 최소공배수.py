def solution(arr):
    answer=0
    lcm=1
    while True:
        IS_LCM = True
        for j in range(len(arr)):
            if lcm % arr[j] != 0:
                IS_LCM=False
                break
        if IS_LCM==True:
            answer=lcm
            break
        lcm+=1
    return answer