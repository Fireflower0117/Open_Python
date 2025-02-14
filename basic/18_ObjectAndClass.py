# 객체(Object) 와 클래스(Class)
# --- 학습목표 ---
# ■ 객체 지향 프로그래밍의 개념을 설명할수있다.
# ■ 객체 특성 및 기능, 클래스의 개념을 설명할수 있다.
# ■ 파이썬으로 클래스를 정의내리고 객체를 생성할수있다.

print("=== 객체(Object) 개요" , "="* 60)
# - 객체는 우리가 보고 느끼고 생각할수있는 모든것을 말한다.
# - 현실의 객체를 구현하기 위해서 우선 특징과 기능을 분석해야 한다.
#     1) 객체의 특성 : 현실 객체의 고정적인 요소들이나 상태 (속성적 요소)
#                    예를들면 색,무게, 재질, 모델명,제조사,제조번호등의 요소정보들이다.
#     2) 객체의 기능 : 현실 객체의 움직임(동작)과 관련된 것들 (행위적 요소)
#                    예를들면 똑바로가다, 회전하다, 이동하다, 계산하다, 납품하다 등등의 정보들
# - 현실 객체에 대한 분석이 완료되면, 이것을 디지털 객체로 구현한다.
#     1) 현실 객체를 디지털 객체로 구현할때, 객체의 특성은 변수(속성)로, 기능은 함수(메서드)로 구현한다.
#
#           (현실객체)                           (디지털객체)
#            특성         ----------------->>    변수(속성)
#            기능         ----------------->>    함수(메서드)

name = "OpenRobot"
weight = 45

def fnSayHello():
    print("안녕하세요")

def fnRobotMove():
    print("로봇이 이동한다.")

#  속성(요소), 함수(메서드)만 만들어놨을뿐 호출하는곳이 없으며
#  Class로 만들지 않으면 매번 함수를 호출하는것이 번러로울수있다.


print();print()
print("=== 클래스(Class)" , "="* 60)
# 객체를 만들기 위해서는 클래스를 먼저 정의 해야한다.
# (클래스를 정의한후, 정의 내힌 클래스를 사용해서 객체를 만든다)
#  - 하나의 클래스로 무수히 많은 객체를 만들어 낼수 있다.

# 클래스 정의 형식 (Class define)
#   class 클래스명 :   - 클래스 헤더(class Header)
#      명령어1   -----┐
#      명령어2   ---------- 클래스 블록 (Class Block)
#      명령어3   -----┘

# 객체를 만드는 방법
#         변수 = 클래스명()
# 객체 지향 프로그래밍은 "객체와 객체가 메세지를 주고 받으며 상호 작용을 하면서 작동하도록 코딩하는것"을 말한다.

# 속성및 함수등 다양한 기능의 재사용성이 확보할수있다.    ( OOP : Object Orented Programing : 객체중심적 프로그래밍 : 시스템의 업무적 프로그래밍)
#                                    ┌----------------------┐
#                                    |  OpenNoteRoom        |   OpenNoteRoom Class
#                                    |  ┌----------------┐  |
#                                    |  | roomNum        |  |
#                                    |  | roomName       |  |
#                                    |  └----------------┘  |
#                                    |  ┌----------------┐  |
#                                    |  | sayRoomNum()   |  |
#                                    |  | sayRoomName()  |  |
#                                    |  └----------------┘  |
#                                    └----------------------┘
#            ┌---------------------------------- ┼ -----------------------------------┐    OpenNoteRoom Class의 구현체
#            |                                   |                                    |
#  ┌----------------------┐          ┌----------------------┐             ┌----------------------┐
#  |   open301Room        |          |    open302Room       |             |    open303Room       |
#  |  ┌----------------┐  |          |  ┌----------------┐  |             |  ┌----------------┐  |
#  |  | roomNum        |  |          |  | roomNum        |  |             |  | roomNum        |  |
#  |  | roomName       |  |          |  | roomName       |  |             |  | roomName       |  |
#  |  └----------------┘  |          |  └----------------┘  |             |  └----------------┘  |
#  |  ┌----------------┐  |          |  ┌----------------┐  |             |  ┌----------------┐  |
#  |  | sayRoomNum()   |  |          |  | sayRoomNum()   |  |             |  | sayRoomNum()   |  |
#  |  | sayRoomName()  |  |          |  | sayRoomName()  |  |             |  | sayRoomName()  |  |
#  |  └----------------┘  |          |  └----------------┘  |             |  └----------------┘  |
#  └----------------------┘          └----------------------┘             └----------------------┘

class OpenNoteRoom:
    roomNum  = "300"
    roomName = "RoomNameBase"
    def sayRoomNum(self):
        print("안녕하세요. 사무실 번호는 300 입니다.")

    def sayRoomName(self):
        print("안녕하세요. 사무실 이름은 RoomNameBase 입니다.")

open301Room = OpenNoteRoom()
open302Room = OpenNoteRoom()
open303Room = OpenNoteRoom()

print("type(open301Room) : ", type(open301Room))
open301Room.sayRoomNum()
open302Room.sayRoomName()

print();print()
print("=== 객체를 만드는 과정" , "="* 60)
#  - 객체를 만드는 과정 (ex : 고양이 )
#    1) 객체분석 : 객체의 특성(속성)과 행위(함수)정보를 분석,취합한다.
#                 특성 : 네발, 뽀족한귀, 긴꼬리 등등...
#                 항위 : 걷다, 뛰다, 점프하다, 먹다 등등...
#    2) 클래스정의 : 클래스는 "class" 키워드와 클래스명 으로 클래스블록을 만들고,
#                  현실 객체의 특성은 속성(변수)으로, 기능은 메서드(함수)로 구현한다.
#                  class Cat :
#                      foot     = 4        # 네발
#                      ear      = `sharp`  # 뽀족한귀
#                      tailSize = 15       # 긴꼬리
#                      def fnWark(self):  # 걷다
#                          pass
#                      def fnRun(self):  # 뛰다
#                          pass
#                      def fnJump(self):  # 점프하다
#                          pass
#    3) 객체생성 : 정의된 클래스(Cat)을 사용하여 객체를 만듬
#                 YellowCat = Cat()

print();print()
print("=== 파이썬은 객체로 구성된다." , "="* 60)
# - 파이썬의 모든 요소는 객체이다.
# - <class 'int'>는 "int 객체"라는 의미다.
# - 새로운 클래스를 정의하면 새로운 자료형이 생긴것과 같다.

a = 10
print("type(a) : ", type(a))  # <class 'int'>

b = int(10)
print("type(b) : ", type(b)) # <class 'int'>

c = [1, 2, 3, 4, 5]
print("type(c) : ", type(c)) # <class 'list'>

def fnAdd1(x) :
    return x + 1
print("type(fnAdd1) : ", type(fnAdd1))  # <class 'function'>

import math
print("type(math) : ", type(math))  #  <class 'module'>

#  <clas '$$$$$$'>  - 사실 파이썬의 모든 객체는 Class이다.

print();print()
print("=== 가장 간단한 클래스." , "="* 60)
# - 객체의 속성을 추가할 때는 점(".")으로 연결한다.
# - 클래스로부터 만들어 진 객체들은 독립적인 개체들이다.
# - 객체를 생성한 후에 속성을 추가하면 다른 객체에는 영향을 주지 않는다.

class Robot :
    ''' 가장 심플한 클래스'''

    def fnSayHello(self):
        pass

ver1Robot = Robot()
ver1Robot.name = "Hubo 1"
ver1Robot.weight = "45 Kg"

ver2Robot = Robot()
ver2Robot.name = "Hubo 2 Plus"
ver2Robot.Birth = "2025.02.14"

print(ver1Robot.__doc__)   # Class Description 조회할때
print(ver1Robot.__dict__)  # Class 속성들 값 조회 (함수 는 조회되지 않는다)
print("ver1Robot.name : ", ver1Robot.name, ", ver1Robot.weight : ",ver1Robot.weight)
print("------")
print(ver2Robot.__doc__)  # Class Description 조회할때
print(ver2Robot.__dict__) # Class 속성들 값 조회 (함수 는 조회되지 않는다)
print("ver2Robot.name : ", ver2Robot.name, ", ver2Robot.Birth : ",ver2Robot.Birth)
print("------")
print(dir(ver1Robot))  # Class 요소들 값 조회 (속성 , 함수 조회)
print("type(ver1Robot.name) : ",type(ver1Robot.name))
print("type(ver1Robot.fnSayHello) : ",type(ver1Robot.fnSayHello))
print("------")

# dir(ver1Robot)함수의 결과 list중 DunDer(double Under Score)를 제거하면 나머지값들('fnSayHello', 'name', 'weight')은 개발자가 추가한 속성들이 조회 가능하다.
# 21_ExceptionProcess.py 까지 학습후. class의 Document, 속성, 함수를 조회할수있는 함수를 만들어 보자
# ex)       ClassName : classDescriptor
#            classDescriptor class의 Document(__doc__)정보 추가하기
#            functions : 1) fnSayDoc() :
#                        2) fnSayAttributes() :
#                        3) fnSayFunctions() :

