# time모듈과 datetime모듈
# -- 학습목표 --
# ■ time모듈을 활용하여 프로그램 실행시간이나 현재의 시간, 날짜등 구하는 파이썬 코드를 작성할수있다.
# ■ time모듈을 활용하여 반복문 안에서 프로그램을 잠시 쉬게 해주는 파이썬 코드를 작성할수있다.
# ■ datetime모듈을 활요하여 프로그램 실행 시간이나 현재의 시간, 날짜, 요일 등을 구할수있다.

print();print()
print("=== 프로그램 실행시간 측정하기" , "="* 60)
# - time.time()함수는 1970년 이후부터 지금까지 경과한 시간을 초단위로 알려준다.
# - time.time()함수를 이용하면 프로그램의 실행시간을 알아낼수 있다.

import time  # 파이썬 내장모듈
print("현재시간 : ", time.time())

def manyloop(max) :
    beginTm = time.time()
    for a in range(max) :
        pass
    finishTm = time.time()
    print("수행시간 : ", finishTm - beginTm)

number = int(input("숫자를 입력하세요 : ")) # 90000000
manyloop(number)

print();print()
print("=== ctime()함수로 년,월,일,시,분,초 추출하기" , "="* 60)
# - time.ctime() 함수는 현재시간을 문자열로 알려준다.
# - time.ctime() 함수로 얻은 시간정보를 split함수를 이용해 분리할수있다.

current = time.ctime()  # 현재시간을 문자열로 알려준다.
print(current)

list_cur = current.split(' ')
for t in list_cur :
    print('t : ', t)

print();print()
print("=== 시간 딜레이 주기" , "="* 60)
# - time.sleep()함수는 프로그램을 잠시 쉬게 해주는 기능을 가진 함수이다.
# - time.sleep()함수는 주로 반복문 안에서 사용되고, 초를 실수값으로 입력할수도 있다.

for t in range(3) :
    print(time.ctime())
    time.sleep(1)           # java의 Thread.sleep와 유사한 기능을 제공

print();print()
print("=== 다른 방법으로 년,월,일,시,분,초 추출하기" , "="* 60)
# - datetime.datetime.now()를 이용해서 현재 시간을 구할수 있다.
# - 이때 얻은 값에서 year, month, day ...와 같은 방법으로 년,월,일,시,분,초 를 추출할수있다.
# - weekday() 함수로 얻는 값은 0 ~ 6이며, 이값은 월요일부터 일요일까지의 값을 의미한다.

import datetime

d = datetime.datetime.now() # 현재시간객체를 구한다.
print("d : ", d)

print(d.year , d.month, d.day, sep="/")
print(d.hour , d.minute, d.second, d.microsecond, sep=":")
print(d.weekday()) # 요일 ==>> 0:월, 1:화, 2:수, 3:목 , 4:금, 5:토, 6:일


