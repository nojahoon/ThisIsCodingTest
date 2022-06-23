def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0] - 1          # start index
        j = command[1] - 1          # end index
        k = command[2] - 1          # choose index

        arr = array[i: j + 1]       # slicing
        arr.sort()
        answer.append(arr[k])

    return answer