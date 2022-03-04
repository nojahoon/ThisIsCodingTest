w,h,b = map(int,input().split())

print("{:.2f}".format(w*h*b/8/1024/1024),"MB")

#풀이코드
#res=int(w)*int(h)*int(b)/1024/1024/8
#print('%.2f'%res,"MB")
