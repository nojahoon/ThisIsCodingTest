number_369 = int(input())
index=1
ISCLAP=False

while(index<=number_369):
    remainder=index
    while (remainder//10 >=1):
        if remainder%10==3 or remainder%10==6 or remainder%10==9:
            print('X' , end=' ')
            ISCLAP=True
        remainder=remainder//10
    #한자리수인 경우
    if remainder == 3 or remainder == 6 or remainder == 9:
        print('X', end=' ')
        ISCLAP=True
    if(not ISCLAP):
        print(index , end=' ')
    ISCLAP=False
    index+=1
#연속 clap에 대한 설명도있길래 고려했더니만 30밑의수만 input으로 잡는 것 같다;;

