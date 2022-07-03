def solution(n, arr1, arr2):
    bin_arr = []
    treasure_arr = []
    answer_arr=[]

    for i in range(n):
        bin_arr.append(arr1[i] | arr2[i])
    for treasure in bin_arr:
        treasure = treasure_arr.append((bin(treasure).replace('0b','')).zfill(n))
    for treasure in treasure_arr:
        answer=''
        for each in treasure:
            if each=="1":
                answer+='#'
            else:
                answer+=' '
        answer_arr.append(answer)
    return answer_arr