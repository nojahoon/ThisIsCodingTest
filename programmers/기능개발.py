def solution(progresses, speeds):
    answer = []

    # 첫번째 기능이 제일 마지막 index로 가도록 조정
    progresses.reverse()
    speeds.reverse()

    index = len(progresses)

    while index > 0:

        # peek 라고 생각
        progress = progresses[index - 1]

        # progress 100이면 계속 pop해주기
        count = 0
        while progress >= 100:
            p = progresses.pop()
            s = speeds.pop()
            index -= 1
            count += 1
            if index > 0:
                progress = progresses[index - 1]
            else:
                break
        # 배포가 발생했다면 발생횟수 answer arr에 지속적으로 추가
        if count != 0:
            answer.append(count)

        # speeds 만큼 작업량 진행
        for i in range(index):
            progresses[i] += speeds[i]

    return answer