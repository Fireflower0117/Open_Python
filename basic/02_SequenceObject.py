# 객체의 구성요소에 순서값(secuence)를 가지는 자료형은 전부 시퀀스형객체이다.
# 시퀀스형 객체로는 문자열과 리스트(list) , 튜플(tuple) , range 등이 있다.


# 문자열 인덱스(Index)가 있기 때문에 가능하다.
#          N   A   T   U   R   E
# 정방향    0   1   2   3   4   5
# 역방향    -6 -5  -4  -3  -2  -1

text7 = "NATURE"
print(text7[0], text7[1] , text7[2])  # N A T
print(text7[-3], text7[-2], text7[-1]) # U R E


#문자열 슬라이싱
# 변수 [시작인덱스, 끝인덱스]
# 주의 : 정방향인덱스든 역방향 인덱스든 혼용하든, 값을추출하려면 시작인덱스가 끝인덱스보다 앞을 가리켜야 한다.

print(text7[0:3])   # 정방향
print(text7[-6:-3]) # 역방향
print(text7[-6:3])  # 혼용
print(text7[2:-6])  # 조회값없음 (시작보다 종료인덱스가 더 앞이다.
print(text7[-5:])  # 시작인덱스만 지정하면 시작인덱스부터 끝까지
print(text7[:-4])  # 끝인덱스만 지정하면 시작위치부터 끝인덱스까지


print("="* 60)
text8 = "name"

capital = text8.upper()
print(capital)
print(text8)


print("="* 60)
# 문자열 관련 메서드
# upper() : 대문자로 변환
# lower() : 소문자로 변환
# count() : 문자열 갯수 집계
# startwith() : 문자열의 특정문자열로 시작여부 판단
# endwith() : 문자열의 특정문자열로 종료여부 판단
# split() : 문자열 분리하여 list로 만들어 반환
# xfill() : 지정한 길이만큼 문자열 채움

myStr = 'Hello, My little baby'
print(myStr.upper()) # 대문자로
print(myStr.lower()) # 소문자로
print(myStr.title()) # camelCase
print("*"*15)

#print(myStr.count()) 장애발생
print(myStr.count("b")) #2
print(myStr.endswith("y")) # True
print(myStr.startswith("h")) # false
print(myStr.lower().startswith("h")) # True
print("*"*15)


myStrList1 = myStr.split()
print('myStrList1 : ', myStrList1)
myStrList2 = myStr.split(",")
print('myStrList2 : ',myStrList2)
myStrFill = myStr.zfill(30) # LPAD(myStr, 30, '0')
print(myStrFill)