def solution(s):
    dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9}
    st = s

    for num in dict:
        # replace() : arguments 2 must be string
        # 따라서 고의적으로 str형 변환함. 아니면 dict에서 처리해도 무방하다.
        st = st.replace(num, str(dict[num]))

    answer = int(st)

    return answer
