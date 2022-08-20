def solution(s):
    answer=len(s)
    if len(s)==1:
        return 1
    for i in range(1,len(s)//2+1):
        temp = s[:i]
        cnt=1
        cur=''
        for j in range(i,len(s),i):
            if temp==s[j:j+i]:
                cnt+=1
            else:
                if cnt==1:
                    cur+=temp
                else:
                    cur+=str(cnt)+temp
                temp = s[j:j+i]
                cnt=1
        if cnt==1:
            cur +=temp
        else:
            cur +=str(cnt) + temp
        answer = min(answer,len(cur))
    return answer
print(solution("aabbaccc"))