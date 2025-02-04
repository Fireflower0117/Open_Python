# 파이썬 내장함수
# ---  학습목표 ---
# ■ 파이썬이 기본적으로 제공하는 내장함수를 파악한다.
# ■ abs(), bool(), dir(), help() 함수들의 기능을 이해하고 사용할수있다.
# ■ 인수를 가지지 않는 dir() 함수와 객체를 인수를 가지는 dir(객체)함수가 제공하는 기능의 차이를 설명할수있다.
# ■ eval() 함수의 기능을 이해하고 사용할수있다.
# ■ exec()함수의 기능을 이해하고 사용할수있다.
# ■ compile()함수의 기능을 이해하고 사용할수있다.


print("=== 내장함수 " , "="* 60)
# ■ 내장함수(Built-in Function)은 파이썬이 기본적으로 제공해주는 함수를 말한다.
# ■ 내장함수는 모듈을 임포트(import)하지 않고도 언제든지 사용할수있다.
# ■ 3.* Ver 파이썬에는 모두 69개의 내장 함수를 제공하고있다.
#    refUrl = https://docs.python.org/ko/3.9/library/functions.html

print("=== 내장함수 abs()" , "="* 60)
# - abs()는 절대값을 구해주는 함수이다.
# - abs()는 하나의 인수만 요구하는 함수이다.

pos = 10
neg = -10

print("abs(pos) : ",abs(pos))
print("abs(neg) : ",abs(neg))
print("abs(pos) == abs(neg) : ",abs(pos) == abs(neg))


print();print()
print("=== bool()" , "="* 60)
# - bool()함수는 참(True) , 거짓(False)를 알려주는 함수이다.
# - bool()함수는 하나의 인수만을 필요로 한다.
# - 숫자'0', 빈(Empty)문자열 , 빈(Empty)리스트 등은 False , 그외값은 True가 된다.

num0 = 0
num1 = 1
print("bool(num0) : ", bool(num0))
print("bool(num1) : ", bool(num1))

emptyList = []
funlList = [1,2,3]
print("bool(emptyList) : ", bool(emptyList))
print("bool(funlList) : ", bool(funlList))

emptyStr = ""
fullStr = "오픈노트"
print("bool(emptyStr) : ", bool(emptyStr))
print("bool(fullStr) : ", bool(fullStr))

print();print()
print("=== dir() , help() 함수" , "="* 60)
# - dir()함수는 현재 사용할수있는 변수들을 보여준다.
# - dir(객체)는 객체가 사용할수있는 메서드 들을 보여준다.
# - help()함수는 주어진 값에 대한 도움말을 보여준다.


print(dir())

print("-"*30)
print("List 객체의 사용가능한 함수")
myList = [1,2,3]
print(dir(myList))

#print("-"*30)
# print(help(myList.append)) # 오류발생  Help on built-in function append: .... None

print("-"*30)
print("List 객체의 도움말 함수")
#print(help(myList))


print();print()
print("=== eval() 함수" , "="* 60)
# - eval()함수는 파이썬 수식 형태의 문자열을 인수로 받아 실제로 실행시킬수있는 파이썬 수식으로 변환하여 실행까지 해준다.
# - eval()함수에는 파이썬 수식이 아닌 파이썬 문장을 넣으면 오류가 발생한다.
# - input() 함수로 받은 값은 문자열이기 때문에 eval()과 함께 사용하면 계산기와 같은 프로그램을 쉽게 만들수있다.

print("eval('1000 * 2') : ",eval('1000 * 2')) # 수식

number = 1
exp = 'print(number + 1)'  # 문장
eval(exp)

""" 
print("더할 두개의 수를 입력하세요")
inpA = input()
inpB = input()
print("문자열 + : ",inpA + inpB) # input 입력값은 문자열 형태이다.
print("eval(문자열) + : ", eval(inpA) + eval(inpB)) # 문자열을 숫자형으로 변환하여 수식을 수행한다.
"""

print();print()
print("=== exec() 함수" , "="* 60)
# - exec()함수는 문장을 받아 파이썬 코드로 변환하고 실행해주는 함수이다.
# - 수식은 변수, 연산자, 함수 등 최종 값을 만들수 있는것을 말한다.
#   ex)  1 + 2 + 3 + 4 + 5
#        10 * 3.14
#        int("1")
#        4 / 2 - 1
# - 문장은 수식을 포함해 하나의 파이썬 명을을 구성할수있는 모든것을 말한다.
#   num = 10
#   sum = 1 + 2 + 3 + 4 + 5
#   print("Hello, World")
#   for item in range(10) :

# 한줄 문자열
state1 = 'print("Beautiful, World")'
exec(state1)

# 여러줄 문자열
state2 = '''
number = 1
for item in [1, 2, 3, 4, 5] : 
    if item % 2 == 1 :
        continue 
    print(item) 
print(number)
'''
exec(state2)

print();print()
print("=== compile() 함수" , "="* 60)
# - compile()함수는 문자열을 미리 파이썬 코드로 변환해주는 함수이다.
# - 미리 변환해두기 때문에 실제 속도에서 빠르다. (속도개선)
# - 변환만 해주기 때문에 실행하기 위해서는 evel() 및 exec()함수와 함께 사용한다.
# - compile() 함수의 사용형식
#      compile( source, filename , mode )
#      ● source : 파이썬 코드 문자열
#      ● filename : 문자열이 저장된 파일명, 파일로부터 읽어들이지 않는 경우에는 <string>을 적는다.
#      ● mode : 변환 대상에 따라 다음 세가지중 하나를 선택한다.
#               1) eval   : 수식을 변환할때 선택         , evel을   선택하면 반환값이 있다.
#               2) single : 단 한줄의 문장을 변환할때 사용, single를 선택하면 반환값이 없다.
#               3) exec   : 여러줄의 문장을 변환할때 선택 , exec를   선택하면 반환값이 없다.

number = 0
exp = 'number + 1'  # 한줄수식
code1 = compile(exp, '<string>', 'eval') # 수식변환 , 반환값 있음
print('code1 : ', code1)
print("-"*20)

for h in range(10) :
    print("for in number : ",number, ", h :", h)
    number = eval(code1)
print('final : ', number)

state2 = ''' 
for item in [1, 2, 3] :
    number = number + 1 
    if item == 2 :
        break; 
print('3 : ', number)
'''

code2 = compile(state2, '<string>', 'exec')
print('code2 : ', exec(code2) )






