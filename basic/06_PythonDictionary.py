# Dictionary(사전) 자료형의 특성
# Key와 Value의 쌍으로 구성된 자료형으로 Key를 이용해서 Value를 가져올수있다.
# Key는 불변객체여야 하며 key는 중복될수없지만 value는 중복될수 있다.
# index를 지원하지 않으며 존재하지 않는key를 조회할경우 오류가 발생한다.
# Dictionary도 집합(set)처럼 줄괄호"{}"를 이용하여 정의하지만,
# 사전에 포함되는 각항목은 ":"을 중심으로 Key,Value를 쌍으로 묶어준다. 각 항목간에는 ","를 사용하여 구분한다.

# Dictionary(사전)을 만들떄 중괄호 안을 비워 두면 빈사전이 만들어진다.
#  ex) myDict = {}
#      myDict = {'fishing':'낚시질', 'fishing banks':'어초',\
#                'fishing boat': '낚시배'}

#      myDict = {1:"수소",2:"헬륨",3:"리튬1",3:"리튬2}
# Dictionary(사전)을 만들떄 key가 중복되면 하나만 남고 나머지 중복된 항목은 사라진다.
# 가장 마지막에 선언한 key외에는 사라진다. (3:"리튬1" 제거된다.)
# Dictionary(사전)은 Python내장함수인 "dict()"를 사용하여 정의내릴수도 있다.
print("=== Dict 정의 " , "="* 60)
myDict = {}
print("type(myDict) : ",type(myDict), myDict)

myDict = {'fishing':'낚시질', 'fishing banks':'어초','fishing boat': '낚시배'}
print(myDict)

# key중복 Test
myDict = {1:"수소",2:"헬륨",3:"리튬1",3:"리튬2"} # 3:"리튬1"값은 제거된다.
print(myDict)

# Dictionary 속성이 많은경우의 개행
myDict = {"name" : "Mr.Kim" \
         , 1004  : [4,3,0,2,1]
          }
print(myDict)

# Python 내장함수 "dict()"를 사용한경우
myDict = dict([(1,'서울'),(2,"부산")])
print("type(myDict) : ",type(myDict), myDict)

# Dictionary에는 순서가 없기때문에 key를 이용해 값에 접근한다.
# 사전에서 값을 조회하는 방법은 key를 직접 이용하는 방법과 get() 메서드를 이용하는 방법이 있다.
#  1) get() 메서드를 이요하여 사전에 값을 가져올떄 사전에 존재하지 않는 key가 지정되면 None를 반환 받을뿐 오류는 발생하지 않는다.
#  2) key를 직접 이용해서 사전에서 값을 가져올때, 사전에 존재하지 않는 key가 지정되면 KeyError오류가 발생한다.

# Dictionary(사전)에 없는 key를 통해 직접 값을 대입하여 수정하려는경우
#  1) Dictionary(사전)에 key가 존재하면 기존에 값을 새로운 값으로 수정
#  2) Dictionary(사전)에 key가 존재하지 않으면 새로운 key,value를 추가한다.

print("=== Dict 추가/조회 " , "="* 60)
opntDev1Dept = {"사원1":"노은비","사원2":"전대혁","사원3":"이설아","사원4":"김민정"\
               ,"사원5":"곽승옥","사원6":"유가영","사원7":"이상일","사원8":"김하영" \
               ,"개발2팀":"김진남"}

print('opntDev1Dept.get(사원5) : ', opntDev1Dept.get("사원5")) # 곽승옥
print('opntDev1Dept.get(사원9) : ', opntDev1Dept.get("사원9")) # None
print('opntDev1Dept[사원5] : ', opntDev1Dept["사원5"])         # 곽승옥
#print('opntDev1Dept[사원9] : ', opntDev1Dept["사원9"])        # KeyError: '사원9'
opntDev1Dept["사원5"] = "홍길동"                               # 항목수정
print('opntDev1Dept[사원5] : ', opntDev1Dept["사원5"])         # 홍길동
opntDev1Dept["사원9"] = "김승현"                               # 항목추가
print('opntDev1Dept[사원9] : ', opntDev1Dept["사원9"])         # 김승현
print('opntDev1Dept : ', opntDev1Dept)

# Dict Keys Base Foreach
for key in opntDev1Dept.keys() :
    print("opntDev1Dept[",key,"] : ", opntDev1Dept[key])


print();print()
print("=== Dict 삭제/제거 " , "="* 60)
# Dictionary(사전)에서 값을 삭제하는 방법은 관련메서드와 "del"문을 이용하는 방법이 있다.
#  dict변수.pop(key[,default])  => Dictionary(사전)에 key가 있으면 대응하는 value를 return, 없으면 default 값을 return
#  dict변수.popitem()           => Dictionary(사전)에 임의의 항목을 return하고, 사전에서 항목을 삭제한다.
#  dict변수.clear()             => Dictionary(사전)의 모든 항목을 삭제한다. (Empty Dictionary로 수정한다 = "{}")
#  del문을 이용하면 항목뿐 아니라, Dictionary(사전)변수 자체도 삭제 할수있다.

myInfom ={"name":"김진남","job":"SW_Devlop","age":"43","address":"JunNamNaju"}
print('myInfom : ',myInfom)
print("pop age ------------")
print(myInfom.pop("age"))
print(myInfom.pop("hobby","sleep")) # "hobby" Key가 없으니, default인 "sleep"이 반환된다.
print(myInfom)

print("popitem ------------")
print(myInfom.popitem()) # 임의의하기보단 사실 제일마지막 key,Value속성이 반환된다. (stack 구조인듯..)
print(myInfom)

print("del attribute ------------")
del myInfom["job"]
print(myInfom)

print("clear ------------")
myInfom.clear()
print(myInfom)

print("del dict ------------")
del myInfom
#print(myInfom) #NameError: name 'myInfom' is not defined

print();print()
print("=== Dict 관련 메서드 " , "="* 60)
# Dictionary(사전)의 내용을 받는데 사용하는 메서드는 items(), keys(), values()가 있다.
#  1) 이 세가지 메서드는 반복문과 함께 많이 사용된다.
#  2) 이 세가지 메서드를 통해 반환받은 리스트(list)나 튜플(tuple)로 형변환(Type Convert)하여 사용할수있다.
#    dict변수.items()    => Dictionary(사전)의 key,value를 dict_items DataType 형태로 반환한다.
#    dict변수.keys()     => Dictionary(사전)의 key들만 dict_keys  DataType 형태로 반환한다.
#    dict변수.values()   => Dictionary(사전)의 value들만 dict_value  DataType 형태로 반환한다.

#   ====  중요  ===
#   dict_items, dict_keys, dict_values는 Dictionary(사전)이 가지고있는 원본의 상대를 그대로 반영해주는 특별한 시퀀스형객체 이다.(시퀀스형객체=순서가 존재하는 객체)

myInfom ={"name":"김진남","job":"SW_Devlop","age":"43","address":"JunNamNaju"}
viewMyAttr = myInfom.items()
viewMyKeys = myInfom.keys()
viewMyValues = myInfom.values()
print('11 type(myInfom) :',type(myInfom),', myInfom : ',myInfom)
print('11 type(viewMyAttr) :',type(viewMyAttr),', viewMyAttr : ',viewMyAttr)
print('11 type(viewMyKeys) :',type(viewMyKeys),', viewMyKeys : ',viewMyKeys)
print('11 type(viewMyValues) :',type(viewMyValues),', viewMyValues : ',viewMyValues)

print(" myInfom.pop(address) ---------")
myInfom.pop("address")  # 원본(myInfom)의 address속성을 반환후 제거.
print('22 type(myInfom) :',type(myInfom),', myInfom : ',myInfom)                        # 원본(myInfom)의 영향을 받아 address속성은 제거 되었다.
print('22 type(viewMyAttr) :',type(viewMyAttr),', viewMyAttr : ',viewMyAttr)            # 원본(myInfom)의 영향을 받아 address속성은 제거 되었다.
print('22 type(viewMyKeys) :',type(viewMyKeys),', viewMyKeys : ',viewMyKeys)            # 원본(myInfom)의 영향을 받아 address속성은 제거 되었다.
print('22 type(viewMyValues) :',type(viewMyValues),', viewMyValues : ',viewMyValues)    # 원본(myInfom)의 영향을 받아 address속성은 제거 되었다.




