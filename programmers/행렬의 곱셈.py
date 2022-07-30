def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        inserted_arr=[]
        for j in range(len(arr2[0])):
            inserted_number=0
            for k in range(len(arr1[0])):
                inserted_number+=arr1[i][k]*arr2[k][j]
            inserted_arr.append(inserted_number)
        answer.append(inserted_arr)
    return answer