# 조건문
# ---  학습목표 ---
# ■ turtle모듈을 이용하여 그래픽 선긋기를 할수있다.
# ■ if문과 elif문, else문등을 이용하여 조건문을 작성할수있다.
# ■ 비교연산자, 논리연산자, in / not in 연산자등을 이용하여 조건문의 조건 정의를 선언할수있다.
# ■ 비교연산자와 논리연산자를 같이 사용할경우 어느연산자부터 수행하는지 알아본다.
# ■ 파이썬에서 들여쓰기 (indentation)의 의미를 알아본다.


print();print()
print("=== tutle graphics " , "="* 60)
# 터틀 그래픽스 (tutle graphics, https://docs.python.org/ko/3.11/library/turtle.html)
#   - 파이썬에서 그림을 그리는 작업을 지원하는 모듈
#   - 거북이(turtle)가 펜을 들고 다니는것을 상상하여 그림을 그린다는 뜻에서 붙여진 이름
#   - 그림을 그리는 방법은 turtle모션을 사용하는 방법과 Pen컨트롤을 사용하는 방법이 있다.

# -- Turtle 모듈에서 제공하는 메서드들 --
# turtle.showturtle()  : 캔버스 상에서 그림을 그리는 화살표(거북이 아이콘)를 나타낸다.
# turtle.hideturtle()  : 캔버스 상에서 그림을 그리는 화살표(거북이 아이콘)를 숨긴다.
# turtle.penup()       : 거북이가 이동을 할때 선이 그어지지 않도록 펜을 들어올린다.
# turtle.goto(좌표값)   : 거북이를 지정한 좌표위치로 이동시킨다.
# turtle.pendown()     : 거북이가 이동할때 선이 그어지도록 펜을 내린다.
# turtle.done()        : 거북이가 그림 그리는 작업을 중지한다.
# turtle.exitonclick() : 마우스로 클릭하면, 거북이의 작업을 중지시키고 캔버스를 닫는다.

# -- Turtle 모듈에서 Pen 컨트롤로 그래픽을 그리기위해 제공되는 메서드들 --
# t.shape("turtle") : 캔버스 상에서 그림을 그리는 화살표 모양을 변경한다.
# t.reset()         : 캔버스를 지우고 화살표를 원위치로 이동한다.
# t.clear()         : 캔버스를 깨긋이 지우고 화살표를 그대로 둔다.
# t.forward(값)     : 화살표가 "값"만큼 앞으로 전진한다.
# t.backward(값)    : 화살표가 "값"만큼 뒤로 후진한다.
# t.right(값)       : 화살표가 "값"만큼 오른쪽(시계방향)으로 회전한다.
# t.left(값)        : 화살표가 "값"만큼 왼쪽(반시계방향)으로 회전한다.
# t.up()            : 펜을 들어올린다. 화살표가 이동해서 선이 안그려진다.
# t.down()          : 펜을 내린다. 화살표가 이동할떄 선이 그려진다

import turtle
t = turtle.Pen()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# if 조건문
# ■ if문은 아래 나타낸 것과 같이 조건식을 가지며, 조건식의 판단결과가 참일때만
#   if조건식: 아래놓인 명령문 블록을 실행한다.
#   ex)  if 조건식 :
#           명령문1
#           명령문2
#           명령문3

# 자료형별 True , False 기준
# 자료형      ,  참(True)       , 거짓(False)
# 정수형      ,  '0'이아닌값     , '0'
# 문자열      , 빈문자열이 아닌값  , "" 빈문자열
# 리스트      , 빈리스가 아닌값    , [] 빈리스트
# 튜플        , 빈튜플이 아닌값    , () 빈튜플

# ----   if 조건식 : 아래 놓이는 명령문 작성시 주의사항  ----
# 같은 블록으로 묶어주기 위해서는 반드시 같은수의 칸으로 들여쓰기를 해야한다.
# 아래 두경우 모두 명령문1과 명령문2는 같은 블록이고 명령문3은 다른 블록으로 분류되고 IdentationError이 발생한다.
# Case 1)                     Case2)
#     if 조건식 :                 if 조건식 :
#           명령문1                 명령문1
#           명령문2                 명령문2
#        명령문3                        명령문3

# 들여쓰기 탭(Tab)과 공백(Space)은 다른문자로 인식하기때문에 주의할 필요가있다.
# 블록구분은 탭(tab)으로 구분하는것을 추천 한다.

t.shape("turtle")

rabbit = 50
carrot = 0
#carrot = 10

if rabbit :
    t.forward(100)

if carrot :
    t.forward(100)
t.backward(100)

print();print()
print("=== if와 비교연산자 " , "="* 60)
# ■ 비교연산은 두값의 크기를 비교하는 연산이다.
# ■ 비교연산의 겨로가는 반드시 참(True)또는 거짓(False)이다.
# ■ 비교연산자의 우선순위는 산술연산자 보다 낮다.

# --- 조건식을 위한 비교연산자 ---
# 비교연산  ,  의미
# x > y    , x값이 y보다 크면 True , 아니면 False
# x >= y   , x값이 y보다 크거나 같으면 True , 아니면 False
# x < y    , x값이 y보다 작으면 True , 아니면 False
# x <= y   , x값이 y보다 작거나 같으면 True , 아니면 False
# x == y   , x값과 y값이 같으면  True , 아니면 False
# x != y   , x값과 y값이 다르면  True , 아니면 False

# --- 연산자 우선순위  ---
# 우선순위 ,  연산자              ,  참고
# 1       , ()                  , 괄호안을 가장먼저 연산한다.
# 2       , **                  , 지수승
# 3       , *, /, //, %         , 곱샘, 나눗셈, 나머지 연산
# 4       , +, -                , 덧셈 , 뺄셈
# 5       , ==,!=,<,<=,>,>=     , 비교연산자
# 6       , =, 복합대입연산자      , 대입연산자는 가장마지막에 처리.

t.reset()
t.shape("turtle")
side1 = 100
side2 = 50

if side1 > 0:
    t.forward(side1)

if side1 >= side2 :
    t.up()
    t.forward(side2)
    t.down()
    t.forward(side1)

if 60 < side2 <= side1 :
    t.reset()

print();print()
print("=== if와 논리연산자 " , "="* 60)
# ■ 논리연산은 두 논리값(참/거짓)을 위한 연산이다.
# ■ 논리연산의 결과도 비교연산과 마찬가지로 반드시 True/False 이다.
# ■ 논리연산자의 우선순위는 비교 연산자 보다 낮다.

# 논리연산   , 의미
# x and y  , x,y모두가 True인 경우만 True , 아니면 False
# x or  y  , x,y중 하나만 True이면 True , 아니면 False
# not   x  , x가 True이면 False , False이면 True

# --- 연산자 우선순위  ---
# 우선순위 ,  연산자              ,  참고
# 1       , ()                  , 괄호안을 가장먼저 연산한다.
# 2       , **                  , 지수승
# 3       , *, /, //, %         , 곱샘, 나눗셈, 나머지 연산
# 4       , +, -                , 덧셈 , 뺄셈
# 5       , ==,!=,<,<=,>,>=     , 비교연산자
# 6       , not                 , 논리부정연산자
# 7       , and                 , 논리곱연산자
# 8       , or                   , 논리합 연산자
# 9       , =, 복합대입연산자      , 대입연산자는 가장마지막에 처리.

t.reset()
t.shape("turtle")

legs = int(input("거북이의 다리 갯수는?"))
skin = input("거북이의 색은?")

if legs == 4 and skin == 'green' :
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

#t.reset()
if legs == 4 or skin == 'black' :
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)

print();print()
print("=== in과 not in 연산자 " , "="* 60)
# ■ x in s는 s 안에 x가 있으면 True , 없으면 False를 반환한다
# ■ x not in s는 s 안에 x가 없으면 True , 있으면 False를 반환한다
# ■ 두연산의 결과는 모두 True, False를 반환한다.y

t.reset()
t.shape("turtle")

reptilia = ["turtle", "crocodile","iguana","chameleon"]
amphibian = ["frog", "toad", "axolotl"]

if "turtle" in reptilia :
    t.color("red")
    t.forward(100)

if "turtle" not in amphibian :
    t.color("gray")
    t.forward(100)

print();print()
print("=== if와 elif, else문 " , "="* 60)
# ■ if문의 조건식이 거짓일때도 실행할 명령어를 지정하기위해 else를 사용한다.
# ■ elif문을 이용하여 여러개의 조건식을 추가할수있다.
# ■ if , elif , else블록중 단 하나의 블록만 실행된다.
# ■ 조건이 True인것이 여러건 존재할경우 처음 만나는 True조건의 블록을 수행한다.
# ■ else블록에는 조건식이 거짓일떄 실행할 코드를 작성한다.
# ■ if 블록은 참일때만, else블록은 거짓일떄만 실행된다.
#   ex)  if 조건식 :
#           True일때 명령문1
#           True일때 명령문2
#        elif 조건식2 :
 #           elif가 True일때 명령문1
 #           elif가 True일때 명령문2
#        else :
#           False일때 명령문1
#           False일때 명령문2

t.reset()
t.shape("turtle")

draw = True
if draw :
    t.forward(100)
if not draw :
    t.forward(-100)

moyang = 3
if(moyang == 4) :
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
else :
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)

t.reset()
t.shape("turtle")
color = int(input("색을 선택하세요(1:파랑, 2:빨강, 3:노랑)"))
if color == 1 :
    t.pencolor("blue")
elif color == 2 :
    t.pencolor("red")
elif color == 3 :
    t.pencolor("yellow")
else :
    t.pencolor("black")

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)