print("Print Console ", "=="*60)
# Print Test
# Print함수는 Console에 Log를 남기는 함수이다.
# 문자열 , 정수 , 계산식의 결과를 console에 남긴다.
# 수행방법은  cmd(teminal) 창에서 프로젝트의 경로로 이동후
# "python 01_PythonBasic.py" 를 수행한다. (python이 System Path에 등록된경우)
# 모르겠으면 구글에서 "python 시스템 환경변수"로 검색할것.

print(2020)
print( 3 + 2 )
print("반갑다 파이썬.!!")




print("주석처리 " , "=="*60)
# "#" 은한줄 주석
# 여러줄 주석은 """  여러줄주석 """ 더블쿼터3개를 이용하여 주석을 남긴다.
"""
여러줄을 한번에 묶는 블록단위 주석입니다.
"""

print("구분자 (seprator) " , "=="*60)
# 구분자 (seprator)
# 여러개값을 콘솔에 출력할때 구분자를 지정할수있다.
# 방법은 print함수 제일 마지막 인자값에 "sep"인자값을 추가하면 된다
mass = 10; height = 20;
print(mass , height, mass * height, sep="____") # seprator 구분자


print("import " , "=="*60)
# import 키워드를 사용해서 외부 lib를 참조할수있다.
import sys
print(sys.version)

# Python에서 기본적으로 제공하는 "math"모듈을 import한다.
import math
print(math.pi)
print(math.sqrt(16))

r = 10
cir = 2 * math.pi * r
print('반지름이 ', r, '인 원의 둘레는 ', cir, '이다')

print("변수 " , "=="*60)
# 변수
# 파이썬의 자료형을 사용자정의 키워드로 지정하는 방법이다.
# 변수의 자료형은 지정하지 않는다. (var , const , let 로 변수를 지정하지 않는다.)
apple = 10
lemon, banana = 20, 50
fruit = apple + lemon + banana
print(apple)
print(banana)
print(fruit)

# 한줄에 하나의 변수나, 구문만 입력하면 ";"를 입력 안해도 되지만
# 한줄에 여러개의 변수를 선언할경우에는 ";"를 구분자로 입력한다.
num1 = 10; num2 = 20; num3 = 30;
print(num1)
print(num2)
print(num3)

# 변수는 자료형의 변경이 가능하다.
apple = 30
print(apple)

print("문자열" , "=="*60)
# 문자열
# 문자열은 '' , "" 으로 선언한다.

city = 'seoul'
dosi = "미래도시"
print(city)
print(dosi)

# ' , " 든 열고 닫는건 같아야 한다.
print("88서울 올림픽 마스코드는 '호돌이'다")
print('그는 이렇게 말했다. "사랑해.." 라고.')


text2 = '작은따옴표안에(") 문자 하나'
print(text2)
text3 = "큰따옴표안에(') 문자 하나"
print(text3)

text4 = '특수문자열 \" 이렇게 \' 출력되요.'
print(text4)

text5 = '''그런데
  여러줄을 
     사용하면 
         이렇게 출력된다.
'''
print(text5)

text6 = '문자열 \n 줄바꿈 \t 탭도 가능합니다.'
print(text6)

# 문자열의 길이가 길어져서 개행이 질요한 경우 문자열이나 구분의 끝에 "\"를 남겨서 개생이 가능하다.
num1 = 10; num2 = 20; num3 = 30;
num4 = 40; num5 = 50; num6 = 60;
sum = num1 + num2 + num3 \
    + num4 + num5 + num6
print(sum)


# 문자열 인덱스(Index)
#          N   A   T   U   R   E
# 정방향    0   1   2   3   4   5
# 역방향    -6 -5  -4  -3  -2  -1

# 시퀀스형 객체로는 문자열과 리스트(list) , 튜플(tuple) , range 등이 있다.
natureText = "NATURE"
print(natureText[0], natureText[1] , natureText[2])  # N A T
print(natureText[-3], natureText[-2], natureText[-1]) # U R E


#문자열 슬라이싱
# 변수 [시작인덱스, 끝인덱스]
# 주의 : 정방향인덱스든 역방향 인덱스든 혼용하든, 값을추출하려면 시작인덱스가 끝인덱스보다 앞을 가리켜야 한다.


# 문자열의 끝에 "\"을 남겨 개행하면 다음행의 공백문자를 그대로 인식한다.
color = [
're\
d'
,'gr\
    een' # 개행 다음줄 앞의 빈공백도 문자로 인식한다.
,'blue']
print(color)

print("자료형 type확인하기" , "=="*60)
# 자료형 type확인하기
age = 42
name = "홍길동"
pi = 3.14
boot = True  # bool은 예약어라 사용불가
print("type(age) :",type(age))
print("type(name) :",type(name))
print("type(pi) :",type(pi))
print("type(boot) :",type(boot))

# bool DataType는 0은 False , 0이 아니면 True로 인식한다.
birds = 3
print('11 birds : ', birds , bool(birds) , sep=" ,, ") # 0 아니면 True

birds = 0
print('22 birds : ', birds , bool(birds) , sep=" ,, ") # 0 이면 false

print("Function " , "=="*60)
# function(함수)은 연산/ 수행문을 하나로 묶어놓은 제공하는것이다.

print("안녕! 나도함수야")

length = len("이 문자열의 길이")
print(length)

max_number = max(11, 2, 63, 47, 50)
print(max_number)

print("사용자 정의 입력값 받기" , "=="*60)
# 사용자 정의 입력값은 input함수를 이용하여 받을수있다.

print("회원가입 기본정보") # Test수행은 주석을 제거하여 Test할것
"""
name = input("이름을 입력하세요 :")
age = input("나이를 입력하세요 :")
print('당신의 이름과 나이는 다음과 같습니다.')
print(name)
print(age)
"""

