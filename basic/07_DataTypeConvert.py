# Data Type Convert (Data 형태 변환)
# ---  학습목표 ---
# ■ 특정 자료형에서 다른 자료형으로 바꾸는 형변환(Data Type Convert)의 개념을 이해한다.
# ■ %를 이용해 원하는 위치에 값을 형식에 맞춰 출력할수있다.
# ■ format() 메서드를 이용해 원하는 위치에 값을 형식에 맞춰 출력할수있다.

# 다른형태의 자료구조로 변경하는것을 형변환이라 한다.
#  1) 문자열 -> 정수형으로 변환하려면, int()함수를 이용한다.
#  2) 문자열 -> 실수형으로 변환하려면, float()함수를 이용한다.
#  3) 정수,실수 -> 문자열형으로 변환하려면, str()함수를 이용한다.
#  4) 리스트(list)는 tuple() 함수를 이용하여 튜플로 변환한다.
#  5) 튜플(tuple)은 list() 함수를 이용하여 리스트로 변환한다.
# 변수값이 어떤 자료형인지 확인하려면 "type()" 함수를 사용하여 확인할수있다.

print("=== 형변환 Basic " , "="* 60)
iStr = "7"
iNumber = int(iStr)
iFloat = float(iNumber)
iString = str(iNumber)
print("type(iStr) : ",type(iStr),", iStr : ",iStr)
print("type(iNumber) : ",type(iNumber),", iNumber : ",iNumber)
print("type(iFloat) : ",type(iFloat),", iFloat : ",iFloat)
print("type(iString) : ",type(iString),", iString : ",iString)
# print(iString + 1) # 오류발생 TypeError: can only concatenate str (not "int") to str ==>> 문자열과 정수형의 합은 "+" 산식으로 수행불가하다.
# print(iNumber + "1") # 71
# print(iNumber + 1)   # 8

print();print()
print("=== list, tuple 형변환 " , "="* 60)
myList = [1,2,3]
print("type(myList) :",type(myList), ", myList : ",myList)
myTuple = tuple(myList)
print("type(myTuple) :",type(myTuple), ", myTuple : ",myTuple)


print();print()
print("=== %를 이용한 형변환 " , "="* 60)
# ■ %를 이용하면 문자열 내부 "형식문자열"이 놓이 위치에 원하는 형식의 값을 출력할수있다.

# 형식문자열   , 내용                      ,   예시                       , 결과출력
# %s         , 문자열 출력                ,   company="Open노트";
#                                           print('%s' % company)      , "Open노트"
# %d         , 십진 정수출력              ,   number = 255
#                                           print('%5d' % number)      , 255
# %f, %F     , 실수출력                  ,   pi = 3.141592654319
#                                           print('%6.2F' % pi)        , 3.14
# %o         , 8진수 출력                ,   number = 255
#                                           print('%3o' % number)      , 377
# %x, %X     , 16진수 출력               ,   number = 65535
#                                           print('%4x' % number)      , FFFF
# %e, %E     , 실수를 지수승 형태로 출력    ,   eNumber = 0.000123
#                                       ,   print('%e' % eNumber)      , 1.230000e-04

print('%s' % "Open노트")                 #
print('%s, %s' % ("하나","둘"))           # Set의 구성요소를 문자열로 변경하며 출력한다.
print("--------")
print('작품번호 : %5d' % (365))           # 전체 5개칸을 만들고 뒤에서 365값을 채운다.             => | | |3|6|5|
print('%d, %d, %d' % (1,2,3))            # 형식문자열순서와 일치하는 set의 Index를 찾아 출력한다.
print("--------")
# 형식문자열의 값과, Set의 Index와 일치하는 값을 찾아출력한다.
# 전체 6개칸을 만들고 뒤에 두자리를 소수가 위치하게 만든다. => | | |8|.|1|2|4|
print('작품번호 : %5d ,작품선호도 : %6.2f' % (365, 9.22854)) # 전체 6개칸을 만들고 뒤에 두자리를 소수가 위치하게 만든다. => | | |9|.|2|3|
print('작품번호 : %5d ,작품선호도 : %6.2f' % (486, 8.124))    # 전체 6개칸을 만들고 뒤에 두자리를 소수가 위치하게 만든다. => | | |8|.|1|2|
print('작품선호도 : %6.2f' % (5.234))     # 전체 6개칸을 만들고 뒤에 두자리를 소수가 위치하게 만든다. => | | |5|.|2|3|

print("--------")
""" 
weight = int(input('체중(Kg)을 입력 하세요 :'))
height = float(input('키(m)을 입력 하세요 :'))
bmi = weight / (height * height)
comment = 'BMI는 %d / ( %.2f * %.2f) 이므로 %6.2f 입니다.'
print(comment % (weight, height, height, bmi))
"""

print("=== format()을 이용한 형변환 " , "="* 60)
# ■ % 연산자을 이용하는방식보다 format()를 이용하는것이 더 효율적인 방식이다.
# ■ format()을 이용해 형식에 맞춰 출력하려면, 출력하려는 문장 안에 값을 넣고싶은 위치에 인수번호를 가지는 중괄호"{}"를 기재한다.
# ■ format()메서드의 괄호안에 출력할 값이나 변수등을 인수로 지정하여, 각인수에 첫번째 인수"0"부터 시작하는 인수가 차례대로 대입된다.
#   ex  "{1} , {0}".format("하나","둘") ==> "둘","하나"
#                   index (0    , 1)

print("{0}, {1}".format("하나","둘"))
print("{0}, {1}, {2}".format(1,2, [3,4,5] ))
print("index가 없어도 {}, {}, {}".format("하나","둘","셋"))
print()
print("index를 바꾸면...")
print("{2}, {1}, {0}".format("A","B","C"))
print("{0} {1} {0}".format("장발장", "은 뒤집어도"))
print()
""" 
weight = int(input('체중(Kg)을 입력 하세요 :'))
height = float(input('키(m)을 입력 하세요 :'))
bmi = weight / (height * height)
formatComment = 'BMI는 {0} / ({1} * {1}) 이므로 {2:6.2f} 입니다.' # "2:6.2f"의 뜻은 2번 Index의 값은 전체 6자리를 만들고 그중 뒤에 2자리는 실수(float)로 출력
print(formatComment.format(weight, height , bmi))
"""

print("=== format()더 알아보기 " , "="* 60)
#  ■ format()을 사용할때 중괄호 안에 인수번호 대신 키워드 인수를 사용할수있다.
#  ■ format()은 여러줄 문자열에도 사용할수있다. (여려줄문자열 = 블록주석)
print("햄버거를 만들어 보자.")
basemat = ("빵","토마토", "야채", "소스")
coremat = ("새우","불고기","한우","치즈")
print('''{food}의 기본재료는 {base}이고,핵심재료에 따라 이름이 달라져'''.format(food="햄버거", base=basemat))
for item in coremat : # Python의 반복문 => for "변수" in 자료
    print("핵심재료가 {core}면 {core}버거".format(core=item))  # 변수 item을 core에 대입한다.

