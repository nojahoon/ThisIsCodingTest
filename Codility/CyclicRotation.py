# Iteration : CyclicRotation
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    ARRAY_LENGTH = len(A)

    # 빈 array가 오는경우 index error 발생방지
    if ARRAY_LENGTH == 0:
        return A

    # 반복문 분기마다 1회씩 right shift한다.
    for i in range(K):
        # 끝 index는 temp에 저장해두고 1번째 인덱스로 이동시킬예정
        temp = A[ARRAY_LENGTH - 1]

        # 끝 index부터 해당 index 이전의 내용으로 덮어쓴다.
        for j in range(ARRAY_LENGTH - 1, 0, -1):
            A[j] = A[j - 1]
        # 처음 index에는 temp의 내용이 오게한다.
        A[0] = temp
    return A