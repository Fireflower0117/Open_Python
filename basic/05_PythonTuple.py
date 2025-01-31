# Tuple 자료형의 특성
print("=== 01 " , "="*60)
# 01) 튜플은 소괄호"()"를 이용하여 정의 한다.
#     ex)   myTuple = ()
baseTuple = (1, "Python", 3.14)
print("baseTuple : ",baseTuple, ", type(baseTuple) : ",type(baseTuple))

print("=== 02,03", "="*60)
# 02) 값의 나열이며 순서가 존재한다.
# 03) 하나의 튜플안에 여러 종류(자료형)을 담을수있다.
#     ex)   myTuple = (1, "python", 3.14)
multipleTuple = ("문자열도 넣고", (1,2,3) , [4,5,6])
print("multipleTuple : ",multipleTuple)
#     튜플 슬라이싱
print("multipleTuple[0] : ",multipleTuple[0])
print("multipleTuple[1] : ",multipleTuple[1])
print("multipleTuple[1][0] : ",multipleTuple[1][0])
print("multipleTuple[1][1] : ",multipleTuple[1][1])
print("multipleTuple[1][2] : ",multipleTuple[1][2])
#  튜플 수정
#  문자열 객체와 튜블은 대표적인 불변객체(수정이 불가한 객체)이다.
#  multipleTuple[1] = "AAA"  #multipleTuple[1]의 값은 tuple이라서 수정불가
#  그러나 수정이 가능한 경우도 있다. 튜플인덱스의 값이 수정가능한 객체인경우가 그렇다.
multipleTuple[2][0] = 1  #multipleTuple[2]의 값은 배열이라 수정가능
print("multipleTuple[2] : ",multipleTuple[2])

#multipleTuple[2] = [6,7,8] # TypeError: 'tuple' object does not support item assignment
#그러나 multipleTuple[2]의 값을 수정하는것은 불가능 => 수정이 불가능한 튜플의 값을 수정하는것으로 간주한다.
#print("multipleTuple[2] : ",multipleTuple[2])


print("=== 04", "="*60)
# 04) 0부터 시작하는 정방향 인덱스 -1부터 시작하는 역방향 인덱스가 존재 하며, 슬라이싱도 가능하다. (list객체와 동일하다)
multipleTuple2 = ('p','y','t','h','o','n')
# 정방향 인덱스      0 , 1 , 2 , 3 , 4 , 5
# 역방향 인덱스     -6 ,-5 ,-4 ,-3 ,-2 ,-1
print("multipleTuple2[1:4] : ",multipleTuple2[1:4]) # 정방향 1 ~ 3까지 (끝 인덱스-1)
print("multipleTuple2[:-2] : ",multipleTuple2[:-2]) # 역방향 -최저Index ~ -3인덱스까지 (끝 인덱스-1)
print("multipleTuple2[:] : ",multipleTuple2[:])     # 정향방 처음인덱스부터 끝인덱스까지

tupleTst3 = ('A','B','C')
print("tupleTst3[0] : ", tupleTst3[0])
#print("tupleTst3[3] : ", tupleTst3[3])     # IndexError: tuple index out of range (크기를 벗어난 인덱스번호 사용불가)
#print("tupleTst3[2.0] : ", tupleTst3[2.0]) # TypeError: tuple indices must be integers or slices, not float (반드시 정수사용 )


print("=== 05",  "="*60)
# 05) **** 읽기전용이다.(항목을 변경할수없는 불변 객체이다.) **** (list는 항목가공가능 ,tuple은 항목가공 불가능)
#multipleTuple2[1] = "Update"  # TypeError: 'tuple' object does not support item assignment
# 튜블속성은 수정 불가, insert , add , delete가 없다.

print("=== 06" ,"="*60)
# 06) 값이없는 비어있는 Tuple를 만들때는 빈괄호"()"나 "tuple()"함수를 사용한다.
#     ex)   myTuple = tuple()
emptyTuple = tuple()
print("type(emptyTuple) : ",type(emptyTuple))

print("=== 07" ,"="*60)
# 07) 값이하나만 있는 튜플을 정의할땐 반드시 ","를 뒤에 넣어야한다.
#     ex)   myTuple  = ("tupleTest",)  <= tuple객체 (항목뒤에 ","가 있는경우)
#           myString = ("tupleTest")   <= 문자열객체 (항목뒤에 ","가 없는경우)
tupleTst = ("tuple",)
strTst   = ("string")
print('type(tupleTst) : ', type(tupleTst))
print('type(strTst)   : ', type(strTst))

print("=== 08" , "="*60)
# 08) 튜플을 정의내릴때 소괄호 사용은 생략할수있다.
#     ex)   myTuple = 1, 2, "number"
tupleTst2 = 1,2,3
print('tupleTst2 : ', tupleTst2, " type(tupleTst2) : ", type(tupleTst2))

print("=== 09" , "="*60)

# 09) 튜플을 정의내릴때 괄호안에 하나의 항목만 넣으면 튜플로 인정하지 않는다.
#     ex)   myTuple = 1
myTupleType = 1, 2, "Number"
print(myTupleType, ", type(myTupleType) : ", type(myTupleType))
a, b, c = myTupleType  #javascript 의 변수분리와 같음.
print("a : ", a)
print("b : ", a)
print("c : ", a)

print("=== 10" , "="*60)
# 튜플의 연산자
fnTestTuple1 = ("1", "2", ("가","나","다"), "3", ["100","200", 300], "김" )
fnTestTuple2 = ("4", "5", "1")

# 튜플과 튜플을 연결(합)하려면 "+"연산자를 사용
fnSumTuple = fnTestTuple1 + fnTestTuple2
print('fnSumTuple : ', fnSumTuple)

# 튜플을 반복하려면 "*"연산자를 사용
fnMtplTuple =  fnTestTuple2 * 2
print('fnMtplTuple : ', fnMtplTuple)

# 튜플의 값이 존재하는지 여부를 확인하려면 "in" 또는 "not in"을 사용
print("2 in fnTestTuple1 : " , "2" in fnTestTuple1)
print("10 in fnTestTuple1 : " , "10" in fnTestTuple1)

# 튜플을 삭제 하고자 할경우 "del"명령을 사용
#del fnTestTuple1 #튜플겍체는 수정은 불가하지만 삭제는 가능하다.
#print("fnTestTuple1 : ", fnTestTuple1)

# 튜플객체 안에 특정객체의 존재숫자를 알고싶으면 "count"함수 사용
chkCnt = fnSumTuple.count("1")
print("chkCnt : ", chkCnt)

# 튜플객체 안에 특정객체를 찾을때는 "index"함수 사용, 튜플내부에 특정객체가 여러건 존재할경우 가장낮은 정방향 인덱스를 반환한다.
chkIdx = fnSumTuple.index("1")
print("chkIdx : ", chkIdx)

print("=="*20 , "  튜플내장함수  ", "=="*20)
fnChkTuple = (1,3,2,5,4,8,3)
addStrTple = ("가","나")
sumTstTuple = fnChkTuple + addStrTple

# 튜플에 내부 항목의 갯수를 알고싶을땐 "len" 함수를 사용
print("len(fnChkTuple) : ", len(fnChkTuple))

# 튜플내부 최대값을 알고싶을경우 "max"함수를 사용
print("max(lenChkTuple) : ", max(fnChkTuple))
#print("max(sumTstTuple) : ", max(sumTstTuple)) # not supported between instances of 'str' and 'int'

# 튜플내부 최소값을 알고싶을경우 "min"함수를 사용
print("min(lenChkTuple) : ", min(fnChkTuple))
#print("min(sumTstTuple) : ", min(sumTstTuple)) # not supported between instances of 'str' and 'int'

# 튜플내부 값의 합계를 알고싶을땐 "sum"함수를 사용
print("sum(lenChkTuple) : ", sum(fnChkTuple))
#print("sum(sumTstTuple) : ", sum(sumTstTuple)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 튜플내부의 값을 오름차순(asc)으로 정렬하고싶을경우 "sorted"함수를 사용
print("sorted(lenChkTuple) : ", sorted(fnChkTuple))
# print("sorted(sumTstTuple) : ", sorted(sumTstTuple)) # TypeError: '<' not supported between instances of 'str' and 'int'

# 튜플안에 지정한 시퀀스형 객체의 튜플을 만드려면 "tuple(seq)" 함수를 사용
intList = [1,2,3,4]
intTupleConvert = tuple(intList)
print("type(intList) : ",type(intList), ", intList : ", intList)
print(" type(intTupleConvert) : ",type(intTupleConvert), ", intTupleConvert : ", intTupleConvert)
