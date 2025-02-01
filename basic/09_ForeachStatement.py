# 반복문
# ----  학습목표 ----
# ■ while명형을 사용한 반복문과 for명령을 사용한 반복문의 차이를 설명할수있다.
# ■ for문에서 range()함수를 이용하여 반복문ㅇ르 구현할수 있다.
# ■ 반복문과 종종 함께 사용되는 break문과 continue문의 역활을 설명할수있다.


print();print()
print("=== while문 " , "="* 60)
# - while문은 특정 코드를 반복하고싶을때 사용한다.
# - while문은 조건식이 참일때만 조건식 아래 놓인 while문 블록을 실행한다.
# - while문은 조건식을 조절하여 while문 블록의 반복 실행 횟수를 조절할수있다.
#   ex)  while 조건문 :
#            명령문1
#            명령문2

import turtle

t = turtle.Pen()
t.shape("turtle")

count = 0

while count < 4 :
    t.forward(100)
    t.left(90)
    count = count + 1

print();print()
print("=== for문 " , "="* 60)
# - for문은 시퀀스형 객체의 항목수만큼 for문 블록을 반복실행시킬수있다.
# - 매 반복 실행마다 for문 변수는 시퀀스형 객체의 항목을 순서대로 대입받는다.
# - for문은 반복실행 횟수가 명확하게 정해져 있을때 주로사용하고,
#   while문은 반복회수가 명확하게 정해져 있지 않을떄 주로 사용한다.
#   ex)  for  변수 in 시퀀스형_객체 :
#               명령문1
#               명령문2

t.reset()
star = turtle.Pen()
star.shape("turtle")

for i in [1, 2, 3, 4, 5] :
    star.forward(100)
    star.left(72)

print();print()
print("=== for문과 range()함수  " , "="* 60)
# - range()함수는 range객체를 만들어준다.
# - range(시작값, 종료값, 증가값)에서 종료값은 반드시 입력해야 하며,
#   시작값은 생략시 0이 기본으로 지정되고, 증가값은 생략시 1이 기본값으로 지정된다.
# - range()함수의 '시작값'부터 '종료값-증가값'까지 증가값 단위로 증가해가면서 for문을 반복 실행한다.
#   ex)  변수 in range(반복횟수) :
#               명령문1
#               명령문2

star.reset()

for k in range(40) :
    star.forward(k * 10)
    star.right(144)

star.reset()

print();print()
print("=== 중첩 for문  " , "="* 60)
# - 중첩for문은 for문 안에 또다른 for문을 사용하는것을 말한다.
# - for문 블록에는 변수할당이나 if문, for문, while문 등 다양한 코드들이 삽입 될수있다.
# - out_for문이 한번실행될떄마다 in_for문 블록이 모두 실행완료 되어야 out_for문으로 넘어갈수있다.
#    ex)  for :  #  out_for문
#           out_명령문1
#           out_명령문2
#           for : # in_for문
#               in_명령문1`
#               in_명령문2
#           out_명령문3
#           out_명령문4

t.reset()
t.up()

colors = ["red","green","blue","yellow","purple"]
for c in colors :
    t.color(c)
    for i in range(12) :
        t.forward(100)
        t.dot()
        t.backward(100)
        t.right(30)
    t.right(6)

print();print()
print("=== 반복문정지 (break)  " , "="* 60)
# - break는 반복문을 수행중 반복을 중지하고 반복문을 나가는 역할을 한다.
# - break를 만나면 반복문을 즉시 탈출하기 때문에 보통if문 등을 이용해 특정조건 하에서만 실행되도록 한다.
# - 중첩 반목문에서 사용하면 가장 가까운 반복문을 탈출한다.

t.reset()
for item in range(30) :
    if item % 2 :
        t.pendown()
    else :
        t.penup()

    if item == 10 :
        break

    t.forward(10)

print();print()
print("=== 반복문 건너뛰기 (continue)  " , "="* 60)
# - continue는 프로그램의 흐름을  반복문 수행의 다음 시작점으로 이동시킨다.
# - continue는 보통 if문 등을 이용해 특정 조건하에서만 실행되도록 한다.
# - 중첩 반복문에서 사용하면 가장 가까운 반복문의 시작점으로 이동한다.

t.reset()
for item in range(30) :
    if item % 2 :
        t.penup()
        t.forward(10)
        t.pendown()
        continue

    t.forward(10)
