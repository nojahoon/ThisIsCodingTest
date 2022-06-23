# OddOccurrencesInArray
# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    ARRAY_LENGTH = len(A)
    is_paired = [False] * ARRAY_LENGTH

    # 각 원소에 대해서 pair 매칭여부확인
    for i in range(ARRAY_LENGTH):
        # 원소가 같다면 pair 성공으로 간주하고 is_paired 배열에 기록
        for j in range(ARRAY_LENGTH):
            if i != j and A[i] == A[j] and is_paired[j] == False:
                is_paired[i] = True
                is_paired[j] = True

        # pair여부를 검사한 요소가 true로 변경되지 않았으면 non pair 요소
        if is_paired[i] == False:
            return A[i]