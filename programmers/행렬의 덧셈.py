def solution(arr1, arr2):
    answer = [[]]

    if len(arr1) != len(arr2):
        return
    arr_length = len(arr1)

    for i in range(arr_length):
        element_length = len(arr1[i])
        arr = []
        for j in range(element_length):
            arr.append(arr1[i][j] + arr2[i][j])
        answer.append(arr)
    answer.pop(0)  # 초기 빈요소 제거

    return answer