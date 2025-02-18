# 예외처리
# ---   학습목표 ---
# ■ 예외 및 예외 처리에 대한 개념을 이해하고, 예외 처리를 위한 코드를 작성할수있다.
# ■ 예외 처리를 위한 코드작성에 as 문 funally문, raise문 등을 사용할수이다.
# ■ 사용자 정의 예외처리문을 작성할수있다.

print("=== 예외처리의 기본" , "="* 60)
# - 예외란 프로그램 실행중 발생할수있는 오류를 말한다.
# - 예외처리란 프로그램 실행중에 발생한 오류때문에 프로그램이 정지되는것을 막기위한 방법을 말한다.
# - 예외처리 형식
#   ex) try블록에는 오류가 생길수있는 코드를 넣고, 해당 오류를 처리하기위한 코드는 except블록에 작성한다.
#       try :
#           <오류가 발생할수있는 코드>
#       except <오류종류>:
#           <오류가 발생했을때 처리할 코드>
#       else:
#           <오류가 발생하지 않았을때 처리할 코드>

#fstInputNum = int(input("나눌숫자를 입력하세요."))
fstInputNum = 4

try:
    result = 10 / fstInputNum
except ZeroDivisionError:
    print("0으로 값을 나눌수는 없습니다.")
else :
    rsltMsg = '10을 {}으로 나눈 결과값 : {}'.format(fstInputNum, result)
    print(rsltMsg)

print();print()
print("=== 예상되는 오류가 여러개일떄 " , "="* 60)
# - 예외가 발생할수있는 종류가 여러개라면 종류별로 except문을 만든다.
# - except문에 오류명을 생략하면 모든 종류의 오류를 받을수있다.
# - except문 옆에 두개 이상의 오류를 나열할수있다.


try:
    #scdInputNum = int(input("나눌숫자를 입력하세요."))
    scdInputNum = 5
    scdResult = 10 / scdInputNum
except ValueError:
    print('숫자만 입력하세요')
except ZeroDivisionError:
    print("0으로 값을 나눌수는 없습니다.")
except : # except문에 오류명을 생략하면 모든 종류의 오류를 받을수있다.
    print("2가지 외에 개발자가 예측하지 못한 에러발생")
else:
    rsltMsg = '10을 {}으로 나눈 결과값 : {}'.format(fstInputNum, scdResult)
    print(rsltMsg)

print();print()
print("=== as 문 " , "="* 60)
# - as 문을 이용해 파이썬이 제공해주는 예외에 대한 정보를 얻을수있다.
# - as <변수명>일때, '변수' 대신 '변수.args'를 이용할수도 있다.
# - args는 튜플의 형태라서 인덱싱으로 일부분만 가져올수 있다.

def openFile():
    file = open('없는파일.txt')
    line = file.readline()
    inpNum = int(line.strip())

try:
    openFile()
except OSError as err:
    print('11시스템 에러 : ', err) #시스템 에러 :  [Errno 2] No such file or directory: '없는파일.txt'
    print('22시스템 에러 : ', err.args)
    print('22시스템 에러 : ', err.args[0])  # err.args[0] = 에러코드
    print('22시스템 에러 : ', err.args[1])  # err.args[1] = 에러메세지
except :
    print('내가 예측할수없는 오류 T.T')
else :
    print(inpNum)


print();print()
print("=== finally 문 " , "="* 60)
# - finally문은 try문이 실행된 이후 무조건 실행된다.
# - 따라서 예외의 발생과 무관하게 무조건 실행해야 하는코드를 넣는데 적합하다.
# - finally문이 있을땐 except문을 생략할수있다.
#   ex) try :
#           <오류가 발생할수있는 코드>
# [
#       except <오류종류1>:
#           <오류가 발생했을때 처리할 코드>
#       except <오류종류2>:
#           <오류가 발생했을때 처리할 코드>
#  ]
#       else:
#           <오류가 발생하지 않았을때 처리할 코드>
#       finally:
#           <오류발생과 무관하게 무조건 실행해야할 코드>


def writeFile():
    try:
        f = open('fileIO/exceptFile.txt', 'w')
        try :
            f.write('Hello World!!')
        finally:
            f.close()
    except IOError:
            print("oops~!")

def readFile():
    try:
        f = open('fileIO/exceptFile.txt', 'r')
        line = f.readline()
    except IOError:
        print('oops!!')
    else :
        print(line)
    finally:
        f.close()

writeFile() # File 쓰기
readFile()  # File 읽기

print();print()
print("=== raise 문 " , "="* 60)
# - raise문은 개발자가 의도적으로 예외를 발생시킬때 사용한다.
# - raise문을 이용하면서 에러정보를 개발자가 작성할수도있다.
# - 개발자가 작성한 에러 정보는 as 문을 이용하여 얻을수있다.

try :
    raise IndexError
except:
    print('인덱스 에러 발생!!')


print();print()
print("=== 사용자 정의 예외 " , "="* 60)
# - 파이썬은 내장 예외 외에 사용자가 직접 예외를 만들어 쓸수있는 사용자 정의 예외도 제공한다.
# - 사용자 정의 예외는 Exception또는 그 하위 클래스를 상속 받아야 한다.

import math

class QuadError(Exception):
    pass

def quad(a, b, c):
    if a == 0:
        qe = QuadError("이차 방정식이 아니에요.")
        qe.member = (a, b, c)
        raise qe
    if b*b-4*a*c < 0:
        qe = QuadError("이차 방정식이 아니에요.")
        qe.member = (a, b, c)
        raise qe

    x1 = (-b+math.sqrt(b*b-4*a*c)) / (a*a)
    x2 = (-b-math.sqrt(b*b-4*a*c)) / (a*a)
    return (x1, x2)

def getQuad(a, b, c):
    try:
        x1, x2 = quad(a, b, c)
        print("방정식의 근은 ",x1, x2)
    except QuadError as err:
        print(err, err.member)

getQuad(200, 100, 10)

