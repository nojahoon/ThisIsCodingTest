def solution(record):
    answer = []
    dict = {}

    # dict에 id-이름 추가작업
    for line in record:
        rec = line.split(' ')
        if rec[0] == 'Leave':
            continue
        # Enter, Change시 dict 내용 기록
        dict[rec[1]] = rec[2]
    # 출력용 순회
    for line in record:
        rec = line.split(' ')
        if rec[0] == 'Leave':
            answer.append(dict[rec[1]] + "님이 나갔습니다.")
        elif rec[0] == 'Enter':
            answer.append(dict[rec[1]] + "님이 들어왔습니다.")
        elif rec[0] == 'Change':
            continue
    return answer