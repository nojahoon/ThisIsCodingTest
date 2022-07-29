def solution(a, b):
    #2016년 윤년 기준 a월 b일
    dict={'1':31,'2':29,'3':31,'4':30,'5':31,'6':30,
          '7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
    week = ['FRI','SAT','SUN','MON','TUE',"WED","THU"]
    day=0
    for i in range(1,a):
        day+=dict[str(i)]
    day+=b-1
    return week[day%7]