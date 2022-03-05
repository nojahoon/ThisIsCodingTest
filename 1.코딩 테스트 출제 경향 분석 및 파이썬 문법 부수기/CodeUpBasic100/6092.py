student=[0]*23
call_list=list()

call_number=int(input())
call_list = list(map(int,input().split()))

for call in call_list:
    student[call-1]+=1


for student_count in student:
    print(student_count,end=' ')


# 풀이코드
# n = int(input())
# a = input().split()
#
# for i in range(n) :
#   a[i] = int(a[i])
#
# d = []
# for i in range(24) :
#   d.append(0)
#
# for i in range(n) :
#   d[a[i]] += 1
#
# for i in range(1, 24) :
#   print(d[i], end=' ')