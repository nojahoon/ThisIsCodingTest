h,b,c , s = map(int,input().split())

print("{:.1f}".format(h*b*c*s/8/1024/1024),"MB",sep=' ')

#풀이코드
#print(round(h*b*c*s/8/1024/1024, 1), "MB")
