# Set(집합) 자료형의 특성
# 집합은 '중복이 없다' , '순서가 없다.' 와 같은 특성이 있다.
# 집합은 중괄호 '{}'를 사용하여 정의를 내린다.
# ex)  mySet = {1,2,3}
#      mySet = {"hello", 1.0, (1,2,3) }
# 집합도 list나 tuple처럼 다양한 자료형을 담을수 있으나
# **** list같은 가변 객체는 집합의 항목이 될수없다. ***
# 집합은 순서가 없기 때문에 인덱스를 사용해 항목에 접근할수 없다.
# 비어있는 Set(집합)을 만들땐 반드시 "set()" 함수를 사용해야 한다.
# ex) mySet = {}    # 사전형으로 만들어 진다.
#     mySet = set() # 비어있는 set(집합)이 만들어 진다.

print("=== 01", "="*60)
mySet1 = {1,2,3}
print("type(mySet1) : ",type(mySet1)," , mySet1 : " , mySet1)

mySet2 = {"hello", 1.0, (1,2,3)}
print("type(mySet2) : ",type(mySet2)," , mySet2 : " , mySet2)

mySet3 = {1,2,3,3,4,2} # 중복값은 자동으로 제거된다.
print("type(mySet3) : ",type(mySet3)," , mySet3 : " , mySet3)

#mySet4 = {1,2,3,3,[100,200],2} # TypeError: unhashable type: 'list' , # set객체 내부에는 list객체가 있을수 없다.
#print("type(mySet4) : ",type(mySet4)," , mySet4 : " , mySet4)

print(); print()
print("=== 02", "="*60)
# 집합관련 메서드 1
# 집합에 한개의 항목을 추가할땐 "add"함수를 사용
# set변수.add(obj)

# 집합은 순서가 없기때문에 값을 추가해도 어디에 배치될지 알수없다.
# 집합에 여러개의 항목을 추가할땐 "update"함수를 사용, 집합은 중복값을 알아서 제거한다.
# set변수.update(obj1, obj2)

# 집합에서 임의의 항목을 추출할땐 "pop"함수를 사용, 추출된 항목은 set에서 삭제된다.
# 집합은 순수가 없기때문에 값을 추출할때 어떤값이 나올지 알수 없다.
# set변수.pop(obj)

sNature = {"sky", "sea", "flower"}
print("02_01 : ", sNature)

# 항목하나 추가 (집합의 어느항목에 추가될지 알수없다.)
sNature.add("earth")
print("02_02 : ", sNature)

# 여러개 항목을 추가
sNature.update({"flower","water"},{"human","animal"}) # flower은 기존에 있어서 나머지만 일괄 추가되었다
print("02_03 : ", sNature)

print(); print()
print("=== 03", "="*60)
# 집합관련 메서드 2
# 집합내부 항목을 삭제하려할때사용은 "discard", "remove" 함수를 사용한다.
# discard : 집합 내부 항목이 없어도 오류를 발생시키지 않는다.  # set변수.discard(obj)
# remove : 집합 내부 항목이 없으면 오류를 발생시킨다.         # set변수.remove(obj)
# 집합의 모든 항목을 삭제 시킬땐 "clear" 함수를 사용한다.      # set변수.clear()

sPlanet = {"수성","금성","지구","화성","목성","토성", \
           "천왕성", "해왕성"}

print("03_01 : ", sPlanet)

# 항목 삭제하기(discard)
sPlanet.discard("금성")
print("03_02 : ", sPlanet)
sPlanet.discard("명왕성")  # 오류발생안함

# 항목 remove(discard)
sPlanet.remove("천왕성")
print("03_03 : ", sPlanet)
#sPlanet.remove("명왕성")  # KeyError: '명왕성' , 오류발생

sPlanet.clear()
print("03_04 : ", sPlanet)

print(); print()
print("=== 04", "="*60)
# 파이썬의 집합은 수학의 집합과 똑같은 연산을 제공해준다.
# 집합연산화 관련된 연산자와 메서드가 함께 있다.
# 집합연산을 해도 원본 집합은 변하지 않고 새로운 집합을 생성해 준다.



#  메서드                                  연산자   설명            리턴값
# set변수.union(set)                       |       합집합          합집합
# set변수.intersection(set)                &       교집합          교집합
# set변수.difference(set)                  -       차집합          차집합
# set변수.symmetric_difference(set)        ^       대칭차집합       대칭차집합
# set변수.issubset(set)                    <=      부분집합확인     부분집합:True , 아니면 False
# set변수.issuperset(set)                  >=      집합포함확인     포함하면:True , 아니면 False


setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3, 7, 8, 9}
# 합집합
print("== 합집합 ==")
print("setA | setB : " , setA | setB )
print("setA.union(setB) : " , setA.union(setB) )
print("setB.union(setA) : " , setB.union(setA) )

# 교집합
print("== 교집합 ==")
print("setA & setB : " , setA & setB )
print("setA.intersection(setB) : " , setA.intersection(setB))
print("setB.intersection(setA) : " , setB.intersection(setA))

#차집합
print("== 차집합 ==")
print("setA - setB : " , setA - setB )
print("setA.difference(setB) : " , setA.difference(setB))
print("setB - setA : " , setB - setA )
print("setB.difference(setA) : " , setB.difference(setA))

#대칭차집합 (전체집합 - 교집합)
print("== 대칭차집합 ==")
print("setA ^ setB : " , setA ^ setB )
print("setA.symmetric_difference(setB) : " , setA.symmetric_difference(setB))
print("setB ^ setA : " , setB ^ setA )
print("setB.symmetric_difference(setA) : " , setB.symmetric_difference(setA))

#부분집합
print("== 부분집합 ==")
print("{4,5,6} <= setA" , {4,5,6} <= setA)
print("{4,5,6}.issubset(setA)" , {4,5,6}.issubset(setA))
print("{4,5,6,8} <= setA" , {4,5,6,8} <= setA)

#집합 포함여부
print("{1,2,3,4,5,6} >= setA : ", {1,2,3,4,5,6} >= setA)
print("{1,2,3,4,5,6}.issuperset(setA)", {1,2,3,4,5,6}.issuperset(setA))
print("{1,2,3,4,5,8} >= setA : ", {1,2,3,4,5,8} >= setA)



print(); print()
print("=== 04", "="*60)
# 파이썬의 set(집합)의 내장함수

# 집합 내부 항목의 갯수를 알고싶을땐 "len" 함수를 사용
print("len(setA) : ", len(setA))

# set내부 최대값을 알고싶을경우 "max"함수를 사용
print("max(setA) : ", max(setA))

# set내부 최소값을 알고싶을경우 "min"함수를 사용
print("min(setA) : ", min(setA))

# set내부 값의 합계를 알고싶을땐 "sum"함수를 사용
print("sum(setA) : ", sum(setA))

# set내부 값을 오름차순(asc)으로 정렬하고싶을경우 "sorted"함수를 사용
print("sorted(setA) : ", sorted(setA))

# set객체를 만드려면 "set(obj)" 함수를 사용
intList = [1,2,3,4]
intSetConvert = set(intList)
print("type(intList) : ",type(intList), ", intList : ", intList)
print("type(intSetConvert) : ",type(intSetConvert), ", intSetConvert : ", intSetConvert)


