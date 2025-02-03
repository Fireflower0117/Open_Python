# 함수 (Function)
print();print()
print("=== 두개이상의 매개변수가 있는 함수" , "="* 60)
#  ■ 매개변수는 함수가 필요로 하는 만큼 정의할수있다. (최대 255개)
#  ■ 일반적으로 함수 호출시 매개변수의 개수만큼 값을 입력해준다.
#  ■ 매개변수가 여러개일때 호출시 입력된 값이 차례대로 저장된다.
#  ex) def fnArguments(a, b, c) :
#           함수내부수행로직1
#           함수내부수행로직2
#
#      fnArguments(10, 20, 30)
#
#      fnArguments의 A는 10, B는 20, C는 30이 대입된다.

def fnHap(a, b) :
        result = a + b
        print('두수의 합을 구해 출력해주는 함수입니다.')
        print(a,',', b, '두수의 합은 ',result,'입니다.')

fnHap(10, 20)
fnHap(-87, 172)


print("=== 함수의 return 값" , "="* 60)
#  ■ return문이 없는 함수는 None값을 반환한다.
#  ■ return문은 하나의 객체만 반환할수 있다.
#  ■ 리스트, 튜플, 사전등과 같은 군잡자료형을 사용하면 한번에 여러개의 값을 반환할수있다.

def fnTurnNone(value) :
    x = value

def fnTurnValue(value) :
    x = value * 10
    return x

def fnTurnDict(value) :
    x = {value, value+1 , value +2} # 군집자료형인 Dictionary(사전)로 반환
    return x

def fnTurnDictKv(value) :
    x = {'value':value, "value1":value+1 , "value2":value +2} # 군집자료형인 Dictionary(사전)로 반환
    return x

def fnTurnSet(value) :
    return value, value-1, value-2

print('fnTurnNone : ', fnTurnNone(10) )
print('fnTurnValue : ', fnTurnValue(100) )
print('------')
rtnDict = fnTurnDict(10)
print('fnTurnDict:', rtnDict)
print('fnTurnDict:', rtnDict , "rtnDict.pop():",rtnDict.pop()) # Key가 없으면 pop로 값을 찾는다. 그후 값은 소멸된다.(우측 함수먼저수행되어 10이 없어졌다.)
print('------')
rtnDictKv = fnTurnDictKv(10) #
print("rtnDictKv[value]:",rtnDictKv["value"]
    , ", rtnDictKv[value1]:",rtnDictKv["value1"]
    , ", rtnDictKv[value2]:",rtnDictKv["value2"])
print('------')
rtnSet = fnTurnSet(10)
print( "fnTurnSet:", rtnSet
     , ", rtnSet[0]:",rtnSet[0]
     , ", rtnSet[1]:",rtnSet[1]
     , ", rtnSet[2]:",rtnSet[2])

print("=== 매개변수의 기본값 설정하기" , "="* 60)
#  ■ 매개변수에 기본값을 설정할수있다.
#  ■ 기본값이 설정된 매개변수는 함수 호출시 값 지정을 생략하면 기본값이 할당된다.
#  ■ 기본값이 설정된 매개변수는 반드시 기본값이 없는 매개변수 뒤에만 배치할수 있다.
#  ex)  func(message, who='Everyone')              # 가능
#       func(message, who='Everyone', when='am')   # 가능
#       func(who='Everyone', message, when='am')   # 불가능 (기본값이 없는 매개변수 앞에 기본값이 있는 매개변수가 위치)
#       func(who='Everyone', when='am', message)   # 불가능 (기본값이 없는 매개변수 앞에 기본값이 있는 매개변수가 위치)

def report(message, who='EveryOne') :
    print(message , who)

report('Good Morning')  # 기본값적용
report('Good Morning', 'Mr. Kim')

print("=== 가변인수" , "="* 60)
#  ■ 함수에 필요한 값이 여러개이면서 가변적일떄는 가변인수를 사용한다.
#  ■ 가변인수는 함수의 매개변수에 '*'를 붙여 지정한다.
#  ■ 가변인수는 한 함수에 하나만 사용할수있다.
#  ■ 가변인수뒤에 매개변수는 올수없다.
#   ex)  def func(*arg)          # 가능
#        def func(a, *arg)       # 가능
#        def func(a, b, *arg)    # 가능
#        def func(*arg1, *arg2)  # 오류발생(가변인수는 한 함수에 하나만 사용할수있다.)
#        def func(*arg1, c)      # 오류발생(가변인수뒤에 매개변수는 올수없다.)

def select_even(*arg) :
    result = []
    for num in arg :
        if num%2 == 1:   # 나머기자 1이면 홀수
            continue
        result.append(num)
    return result

print(select_even(1,2,3,4))
print(select_even(-12,2,81,99,48,20))


print("=== 함수정보 표시하기(__doc__)" , "="* 60) # '__'는 Double UnderScore라고 한다. 통칭 약어로 던더(DunDer)라고 칭한다.
#  ■ 함수에대한 정보를 얻고 싶을떄 내장함수인 help()함수를 하용해서 함수의 정보를 파악할수있다.
#  ■ 함수 설명문은 여러 쥴 문자열 지정('''~''')을 이용해야 하며, 반드시 내부에서 사용되는 명령어 앞에 작성되어야 한다.
#  ■ 이미 지정된 함수 설명문을 수정하고 싶다면 __doc__ 속성을 이용해 재정의 할수있다.

def fnPrint_odd(start, end) :
    '''주어진 범위에서 홀수를 리스트로 만들어 주는 함수입니다.
    :param start: 시작값을 지정함니다. (정수형, int)
    :param end: 종료값을 지정합니다. (정수형, int)
    :return: list(홀수값들)
    '''
    result = []
    for num in range(start, end+1) :
        if num % 2 == 0 :
            continue
        result.append(num)

    return result

print("함수의 doc문서 파악", "-"*30)
help(fnPrint_odd) # 함수의 doc문서 파악
print("-"*30)
fnPrint_odd.__doc__ = '''이건 연습삼아서 재정의Test'''
help(fnPrint_odd) # 함수의 doc문서 파악
print("-"*30)
print(fnPrint_odd(3,19))



