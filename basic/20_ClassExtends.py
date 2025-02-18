# Class 상속
# ---   학습목표 ---
# ■ 네임 맹글링(name mangling)의 개념을 설명할수있다.
# ■ 상속을 통해 부모 클래스가 가진 속성과 메서드를 물려받는 형태로 자식 클래스를 정의 내일수있다.
# ■ 오버라이딩을 통해 부모클래스로부터 물려받은 메서드를 자식 클래스에서 재 정의할수있다.

print("=== 데이터숨기기" , "="* 60)
# - 변수명/함수명 앞에 두개의밑줄("__"=Double UnderScore=Dunder)을 붙은 변수는 사용하지 말자
# - 변수명/함수명 앞에 '_'이 붙은 변수도 사용하지 말자
# - '_'가 앞에 붙은 변수명은 네임 맹글링(name mangling,이름변경하기)이 적용된다.
# - Python 은 접근제어(public,default,protected,private)가 없지만 네임 맹글링으로 통제하려는 규칙이 있다.

class Robot :
    '''다양한 로봇을 만드는 클래스'''

    def __init__(self, name, build_year): # 생성자(Constructor)
        self.name = name
        self.__build_year = build_year  # "__"로 시작하는 클래스 속성(this.__~~~~~) = 네임 맹글링 (name mangling)
        self.xpos = 0
        self.ypos = 0

    def getYear(self):
        '''Robot의 self.__build_year를 반환'''
        return self.__build_year

hubo = Robot("깡통로봇",2024)
hubo.name = "오픈로봇"

#print("hubo.__build_year : ", hubo.__build_year)  # AttributeError: 'Robot' object has no attribute '__build_year' (접근불가 속성)
print("hubo.name : ", hubo.name)
print("hubo.getYear() : ", hubo.getYear())
print("hubo.__doc__ : ", hubo.__doc__)
print("hubo.getYear.__doc__ : ",hubo.getYear.__doc__)
print()

# dir(class)는 그 클래스가 가지고있는 내부 속성및 함수(메소드)정보를 list로 반환한다.
# 그러나 Python에서 네임맹글링으로 반드시 접근을 막을수 있는것은 아니다.
print("dir(hubo) : ", dir(hubo)) #  dir(hubo) :  ['_Robot__build_year', ....... , 'getYear', 'name', 'xpos', 'ypos']

# 네임맹글링 속성은 "_클래스명__네임맹글링" 속성으로 접근 가능하다. (ex : hubo._Robot__build_year )
# 그러나 사용할수있지만 사용하지는 말자.. 시스템 복잡도 증가 차원에서 사용하지는 말자..
print("hubo._Robot__build_year : ", hubo._Robot__build_year)

print();print()
print("=== 상속" , "="* 60)
# - 상속이란 클래스와 클래스 사이에 부모-자식 관계를 만들어 주는것이다.
# - 상속관계가 생기면 자식 클래스는 부모의 속성과 메서드를 그대로 물려받는다.
# - 상속관계를 사용하면 코드를 재사용할수있고, 유지보수가 편리해진다.

class ParentRobot :
    '''다양한 로봇을 만드는 기본 로본 클래스 입니다.'''
    def speak(self):
        print('로봇이 말한다.')

    def move(self):
        print('로봇이 이동한다.')

    def charge(self):
        print('로봇이 충전한다.')


class CleanRobot(ParentRobot): # class 상속
    def cleanRoom(self):
        print('로봇이 방을 청소한다.')

print("== ParentRobot ==")
prtRobot = ParentRobot()
prtRobot.move()
# prtRobot.cleanRoom()  ParentRobot클래스에는 cleanRoom 함수가 없다.

print()
print("== CleanRobot ==")
clean = CleanRobot()
clean.cleanRoom()
clean.move()

print();print()
print("=== 상속 super()" , "="* 60)
# - super()는 부모 클래스를 의미하는 내장 함수이다.
# - super()는 자식 클래스에서 사용할수있다.
# - super()를 사용하면 코드를 줄일수있다.


class ParentRegoRobot :
    '''레고로봇 부코 글래스 입니다.'''

    def __init__(self, name , release):  # 생성자 (Constructor)
        self.name = name
        self.release = release

    def make(self):
        print("레고블록을 제작한다.")

    def build(self):
        print("레고 블록 조립한다..")

class RegoRobot(ParentRegoRobot): # class 상속
    def __init__(self, name, release, category ):  # 생성자 (Constructor)
        super().__init__(name, release)  # 부모클래스 접근자(super())의 생성자(__init__)를 호출
        self.category = category

    def playing(self):
        print("레고블록을 가지고 논다.")

    def __str__(self): # Java Lnaguage의 class toString() 유사한함수
        word = '{}에 출시된 {}유형의 {}레고이다.'.format(self.release, self.category , self.name)
        # 부모클래스의 속성(self.name , self.release)을 상속 받는다.
        return word

regoRobot = RegoRobot('해양보트', '2025' , '레고시티')
print(regoRobot) # "__str__" 함수가 호출된다.

regoRobot.make()
regoRobot.playing()

print();print()
print("=== 상속 오버라이딩(overriding)" , "="* 60)
# - 오버라이딩(overriding)은 부모 클래스로부터 물려받은 메서드를 자식 클래스에서 재정의 하는것이다.
# - 자식 클래스 입장에서는 부모클래스로부터 물려받은 메서드를 그냥 써도되고 오버라이딩(재정의)해서 써도 된다.
# - 같은 이름의 함수가 다른 형태로 동작하도록 구현하는 기술을 다형성(polymorphism)이라고 하며, 오버라이딩은 객체 지향 프로그래밍에서
#   다형성을 구현하는데 중요한 역활을 한다.

class ParentCar :
    '''자동차의 부모클래스 입니다.'''

    def move(self):
        print('부모클래스의 자동차가 이동한다.')

    def charge(self):
        print('부모클래스의 자동차를 충전한다.')

    def driving(self):
        print('부모클래스의 자동차가 달린다..')

class  AutoCar (ParentCar) :

    def move(self):
        print('자식클래스 자율주행차 자동차가 이동한다.')

    def charge(self):
        print('자식클래스의 자율주행 자동차를 충전한다.')



prtCar = ParentCar()
prtCar.move()
prtCar.charge()
prtCar.driving()

print()
autoCar =  AutoCar()
autoCar.move()   # 함수 Overriding
autoCar.charge() # 함수 Overriding
autoCar.driving()

print();print()
print("=== 포함관계" , "="* 60)
# - 클래스와 클래스의 관계 설정하는 방법에는 상속관계(IS-A관계)와 포함관계(HAS-A관계)가 있다.
#   1) 상속(IS-A)관계
#      자율주행자동차는 자동차다.(자율주행자동차 is as 자동차)
#   2) 상속(HAS-A)관계
#      자율주행자동차는 엔진을 가진다.( 자율주행자동차 has a 엔진)
#      사각형은 점을 가진다. (사각형은 has a 점)
# - 포함관계는 한 클래스가 다른 클래스의 멤버로 포함되는 것을 말한다.
# - 포함관계로 설정했을떄 변수나 메서드를 사용하는 방법을 잘 알아둘 필요가 있다.

import random

class Motor:
    def __init__(self):
        self.distance = 0

    def forward(self):
        print('앞으로 이동한다.')
        self.distance += 1

    def backward(self):
        print('뒤로 이동한다.')
        self.distance -= 1

class AutoMoveCar:
    '''자율주행 자동차 입니다.'''
    def __init__(self):
        self.drive = Motor()  #Has a관계 (자율주행 자동차는 모터를 포함하고있다.)

    def __str__(self):
        return '이동거리 : {}'.format(self.drive.distance)

aMcar = AutoMoveCar()

for i in range(10):
    if random.randint(0,1):  # 0,1중 임의의 값을 선택 (0:false, 1:true)
        aMcar.drive.forward() # 전진 (self.drive = Motor()) Motor 클래스의 forward()를 호출한다.
    else :
        aMcar.drive.backward() # 후진 (self.drive = Motor()) Motor 클래스의 backward()를 호출한다.

print(aMcar) # __str__ 호출 (toString()와 유사하다)
