#지나치게 쉬운 내용들은 훑고 넘긴다.

a = 5.
b = -.7

print(a)    #5.0  python에서 정수부나 소수부가 0인 경우 생략할 수 있다.
print(b)    #-0.7

#지수 표현 방식
a = 75.25e1
b = 3954e-3
print(a)    #752.5
print(b)    #3.954

#리스트 초기화
a = list() # a = []

#크기가 N이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n  #[0,0,0,0,0,0,0,0,0,0]
b = [1,2,3,4,5,6,7,8,9]

print(a)
print(b[1:4])   #2,3,4   슬라이싱에서 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정한다.

#리스트 컴프리헨션
array = [i for i in range(10)]  # 0~9까지 증감하면서 차례로 i의 값들을 원소로 리스트를 만든다.
print(array)    #[0,1,2,3,4,5,6,7,8,9]

#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)    #[1,3,5,7,9,11,13,15,17,19]

#1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1,10)]
print(array)    #[1,4,9,16,25,36,49,64,81]

'''
특히 N X M 크기의 2차원 리스트를 한번에 초기화 해야할 때 매우 유용하다.
좋은 예시 : array = [[0] * m for _ in range(n)]

만약 2차원 리스트를 초기화할 때 다음과 같이 작성하면 예기치 않은 결과가 나올 수 있다.
잘못된 예시 : array = [[0] * m ] * n
이 경우 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식된다.
'''

#N X M 크기의 2차원 리스트 초기화

n = 4
m = 3
array = [[0] * m for _ in range(n) ]
print(array)    #[[0,0,0] , [0,0,0] , [0,0,0] , [0,0,0]]


#N X M 크기의 2차원 리스트 초기화(잘못된 방법)
n = 4
m = 3
array = [[0] * m] * n
print(array)            #[[0,0,0] , [0,0,0] , [0,0,0] , [0,0,0]] 다 0으로 잘 초기화된것처럼 보이지만 아니다.

array[1][1] = 5
print(array)            #[[0,5,0],[0,5,0],[0,5,0],[0,5,0]] 가운데 값이 다 5로 초기화되어버림.

'''
python에서 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 떄 언더바를 자주 사용한다.
for _ in range(5):
    print(something)
'''

#리스트 관련 기타 메서드
a = [1,4,3]

a.append(2)
a.sort()
print("오름차순 정렬: ", a)   #[1,2,3,4]
a.sort(reverse=True)
print("내림차순 정렬 " , a)   #[4,3,2,1]
a.reverse()
print(a)                    #[1,2,3,4]
a.insert(2,3)
print("인덱스 2에 3 추가: ", a)  #[1,2,3,3,4]
print("값이 3인 데이터 개수 : " , a.count(3))   #2
a.remove(1)
print("값이 1인 데이터 삭제: ",a) #[2,3,3,4]

#리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1,2,3,4,5,5,5]
remove_set = {3,5} #집합 자료형

'''remove_list에 포함되지 않은 값만을 저장'''
result = [i for i in a if i not in remove_set]
print(result)   #[1,2,4]

'''
튜플은 리스트와 유사하지만 한 번 선언된 값을 변경할 수 없다.
a = ()
튜플은 리스트에 비해 상대적으로 공간 효율적

서로 다른 성질의 데이터를 묶어서 관리해야 할 때 유용 : 최단 경로 알고리즘에서 (비용,노트번호)의 형태로 tuple 자료형 자주 사용
데이터의 나열을 해싱(Hasing)의 키 값으로 사용해야 할 때 : 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있음
리스트보다 메모리를 효울적으로 사용해야 할 때
'''

'''
사전 자료형 : Key와 Value의 쌍을 데이터로 가지는 자료형
원하는 '변경 불가능한(Immutable)자료형'을 키로 사용가능
파이썬의 자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리 가능
'''

#사전 자료형
data = dict()
data['사과']='Apple'
data['코코넛'] = 'Coconut'
key_list = data.keys();
value_list = data.values();
if '사과' in data:
    print('Apple exists.')

'''
집합은 중복을 허용하지 않고 순서가 없다.
a = set()


'''
#집합 자료형 초기화 방법
data = set([1,1,2,3,4,4,5])
print(data) #{1,2,3,4,5}
data = {1,1,2,3,4,4,5}
print(data) #{1,2,3,4,5}

#집합 자료형 연산
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b)
print(a&b)
print(a-b)

data = set([1,2,3])

data.add(4)
print(data) #{1,2,3,4}
data.update([5,6])  #{1,2,3,4,5,6}
data.remove(3)  #{1,2,4,5,6}

'''
리스트&튜플 : 순서가 있고 인덱싱으로 자료형의 값 획득 가능
사전형&집합 자료형: 순서가 없고 인덱싱으로 값 획득 불가능
사전의 key 혹은 집합의 원소를 이용해 O(1)의 시간복잡도로 조회
'''

#자주 사용되는 표준 입력 방법
'''
input() 함수는 한줄의 문자열을 입력받는 함수
map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
예시) 공백을 기준으로 구분된 데이터를 입력 받을 때
=> list(map(int, input().split()))
예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 다음곽 ㅏㅌ이 사용
a,b,c = map(int, input().split())

'''
#입력을 위한 전형적인 source code
n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

#빠르게 입력받기
'''
사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있다.
파이썬의 경우 sys 라이브러리에 정의되어있는 sys.stdin.readline() 메서드를 이용한다.
단,입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용한다.
'''

import sys
data = sys.stdin.readline().rstrip()
print(data)


#자주 사용되는 표준 출력 방법
'''
python에서 기본 출력은 print() 함수 이용 : 각 변수를 콤마를 이용하여 띄어쓰기로 구분하여 출력가능
print()는 기본적으로 출력 이후에 줄 바꿈을 수행 : 줄바꿈을 원하지 않는 경우 'end' 속성을 이용가능 
'''

a = 1
b = 2
print(a,b)  # 1 2
print(7,end=" ")
print(8, end=" ")

#출력할 변수
answer = 7
print(" 정답은 " + str(answer) + "입니다. ") # 7 8 정답은 7입니다.

#f-string 예제

'''
python 3.6부터 사용 가능 :  문자열 앞에 접두사 'f'를 붙여 사용
중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다. 
'''
answer = 7
print(f"정답은 {answer} 입니다.")

'''
python style guideline에서는 4개의 공백 문자를 사용해 들여쓰기 하는 것을 추천한다.
python에서 조건문 if-elif-else
python에서 조건문 연산자 and or 사용


다수의 데이터를 담는 자료형을 위해 in , not in 연산자가 사용 : list,tuple,문자열,dictionary 모두 사용가능
x in 리스트 : 리스트 안에 x가 들어가 있으면 참
x not in 문자열 : 문자열 안에 x가 들어가 있지 않으면 참

pass 키워드 : 아무것도 처리하고 싶지 않을 때

a = 50
if a >=30:
    pass        #건너뜀
else:
    print("a<30")
    
    
#조건문의 간소화
조건문에서 실행될 소스코드가 한 줄인 경우 , 굳이 줄바꿈을 하지 않고 간략하게 표현 가능
score = 85
if score >= 80: result = "Success"
else: result = "Fail"

조건부 표현식(Conditional Expression)은 if-else문 한줄에 작성하게 해줌
score = 85
result = "Success" if score >=80 else "Fail"

python에서 다른언어처럼 부등식을 if x>0 and x<20: 처럼 안쓰고 바로 if 0<x<20: 같이 사용가능

python에서 파라미터의 변수를 직접 지정할 수 있다 : 이 경우 매개변수의 순서가 달라도 상관이 없다.
def add(a,b):
    print(a+b)
add(b = 3 , a = 7)

함수 밖 변수를 참조하기 위해서 global 키워드를 사용한다.


'''
#여러개의 반환 값
'''파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다.'''

def operator(a,b):
    add_var = a+b
    subtract_var = a-n
    multiply_var = a*b
    divide_var = a / b
    return add_var , subtract_var , multiply_var , divide_var
a,b,c,d = operator(7,3)
print(a,b,c,d)

#람다 표현식
'''
람다 표현식을 이용하면 함수를 간단하게 작성할 수 있다.
특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있게된다
'''
print((lambda a,b: a+b)(3,7))   #10

array = [('홍길동',50),('이순신',32),('아무개',74)]
def my_key(x):
    return x[1]
print(sorted(array,key=my_key))         #정수형 기준으로 정렬 : 굳이 함수를 또 적어주기 불편한 방법
print(sorted(array,key=lambda x:x[1]))  #[('이순신',32),('홍길동',50),('아무개',74)]  1번만 사용되는 경우 람다사용하는게 편함

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
result = map(lambda a,b: a+b ,list1,list2)
print(list(result))

''' 실전에서 유용한 표준 라이브러리

내장함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들 제공
itertools : 반복되는 형태의 데이터를 처리하기 위한 기능 제공 (순열과 조합라이브러리는 코딩 테스트에서 자주 사용)
heapq : 힙 자료구조 제공 : 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
bisect: 이진 탐색 기능을 제공
collections : 덱 , 카운터 등의 유용한 자료구조를 포함
math: 필수적은 수학적 기닝을 제공 : 팩토리얼,제곱근,GCD, 삼각함수 관련 함수부터 pi같은 상수 포함

'''

#자주 사용되는 내장 함수
result = sum([1,2,3,4,5])
print(result)   #15

min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result , max_result)  #2 7

#eval()
result = eval("(3+5)*7")
print(result)   #56

#sorted()
reverse_result = sorted([9,1,8,5,4],reverse=True)
print(reverse_result) # 9 8 5 4 1

array = [('홍길동',35) , ('이순신',75), ('아무개',50)]
result = sorted(array , key=lambda x:x[1] , reverse=True)
print(result)   #[('이순신',75), ('아무개',50) , ('홍길동',35)]


'''
모든 경우의 수를 고려해야 할 때 어떤 라이브러리를 효과적으로 사용해야 하는가?

순열 : 서로 다른 n개에서 서로다른 r개를 선택하여 일렬로 나열하는 것
    {'A','B','C'}에서 세 개를 선택하여 나열하는 경우 : 'ABC','ACB','BAC','BCA','CAB','CBA'
조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
    {'A','B','C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우 : 'AB','AC','BC'
    
순열의 수 nPr = n * (n-1) * (n-2) * ... * (n-r+1)
조합의 수 nCr = n * (n-1) * (n-2) * ... * (n-r+1)/r!

'''

#순열

from itertools import permutations
data = ['A','B','C']

result = list(permutations(data,3))
print(result)   #[('A','B','C') , ('A','C','B') , ('B','A','C') , ('B','C','A') , ('C', 'A','B') , ('C','B','A')]

#조합
from itertools import combinations

data = ['A','B','C']
result = list(combinations(data,2))
print(result)   #[('A','B') , ('A','C') ,('B','C')]

#중복 순열과 중복 조합
from itertools import product

data = ['A','B','C']
result = list(product(data,repeat=2)) #2개를 뽑는 모든 순열 구하기 (중복허용)
print(result)   #[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

from itertools import combinations_with_replacement

data = ['A','B','C']
result = list(combinations_with_replacement(data,2)) #2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)   #[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

#Counter
'''
파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공
리스트와 같은 반복 가능한(iterable)객체가 주어졌을 때 내부의 원소가 몇번씩 등장했는지를 알려준다.
'''
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])  #3   'blue'가 등장한 횟수 출력
print(counter['green']) #1    'green'이 등장한 획수 출력
print(dict(counter))    #{'red': 2, 'blue': 3, 'green': 1} 사전 자료형으로 반환

#최대 공약수와 최소 공배수
''' 최대 공약수를 구해야할 때 math 라이브러리의 gdc() 함수를 이용할 수 있다.'''
import math
def lcm(a,b):
    return a*b // math.gcd(a,b)
a = 21
b = 14

print(math.gcd(21,14))  #7   최대 공약수(GCD) 계산
print(lcm(21,14))       #42   최소 공배수(LCM) 계산
