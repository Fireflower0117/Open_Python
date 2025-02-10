# Random Module
# -- 학습목표 --
# ■ random 모듈을 활용하여 난수를 만드는 파이썬 코드를 작성할수 있다.
# ■ random 모듈을 활용하여 리스트를 섞어 값을 무작위로 뽑은 파이썬 코드를 작성할수있다.
# ■ random 모듈을 활용하여 시퀀스형 객체 또는 집합에서 여러항목을 한꺼번에 뽑는 파이썬 코드를 작성할수있다.

print();print()
print("=== random 모듈" , "="* 60)
# - 난수를 만들려면 random모듈을 임포트 한다.
# - random.randint(시작값 , 종료값)은 시작값과 종료값 사이에 임의의 정수를 추출하는 함수이다.
# - print() 함수의 end속성은 출력후 한줄의 마지막을 어떻게 처리할것인지는 지정해주는 역할을 한다.

import random

for i in range(6) :
    number = random.randint(1, 45)
    #print(number)
    print(number , end=",_,") # print함수의 끝인자로 'end'가 들어가면 개행을 조절할수있다.

print();print()
print("=== 리스트를 섞어 무작위로 뽑기  " , "="* 60)
card = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
print('pre card : ', card)

random.shuffle(card)
print('shuffle card : ', card)

print('choice card : ',random.choice(card))

print();print()
print("=== 여러항목을 한꺼번에 뽑기" , "="* 60)
# - random.sample()의 첫번째 인수는 시퀀스형 객체또는 집합이고 두번째 인수는 추출하고 싶은 개수이다.
# - random.sample()함수는 주어진 개수만큼 무작위로 뽑아주는 기능을 가진다.
# - random.sample()함수는 중복되지 않은 값을 뽑아준다.

myStr = "전남 나주시에 위치한 - 오픈노트" # 문자열도 시퀀스형 객체이다.
print(random.sample(myStr, 3))

lottoNums = random.sample(range(1,46),6)
lottoNums.sort()
print("lottoNums : ", lottoNums)

print();print()
print("=== 실수를 구성한 난수 만들기  " , "="* 60)
# - random.random()함수는 0.0 ~ 1.0사이의 실수를 무작위로 추출한다.
# - random.uniform(시작값, 끝값)함수는 주어진 값의 범위에서 실수를 임의로 추출한다.
# - random 모듈에는 다양한 난수함수가 제공되는데 이중 자주 사용하는 함수를 정리해보자

print("random.random : ", random.random())
print("random.uniform : ", random.uniform(0, 10))