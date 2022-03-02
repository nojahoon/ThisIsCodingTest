a,b,c = map(int,input().split())
newlist =[a,b,c]
for num in newlist:
    print("even") if num%2==0 else print("odd")