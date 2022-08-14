def solution(new_id):
    answer = ''
    #step 1
    new_id = new_id.lower()
    #step 2
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer+=word
    #step 3
    while '..' in answer:
        answer=answer.replace('..','.')
    #step 4
    if answer!='':
        if answer[0]=='.':
            answer=answer.replace('.','',1)
    if answer!='':
        if answer[-1]=='.':
            answer=answer[0:len(answer)-1]
    #step 5
    if answer=='':
        answer='a'
    #step 6
    if len(answer)>=16:
        answer=answer[0:15]
        if answer[-1]=='.':
            answer=answer[0:14]
    #step 7
    if len(answer)<=2:
        while len(answer)!=3:
            answer=answer+answer[-1]
    return answer