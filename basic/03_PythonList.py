# 리스트(list)
# 값의 나열이며 , 순서(index)가 존재
# list는 대괄호[]를 사용하여 정의한다.
# [1,2,3,4,5] , ["버스","택시","트럭"]
# 리스트를 할당받는 변수를 '리스트변수' 라고 한다.

count = [1,2,3,4,5]
cars = ['버스','트럭','승용차','벤']
wondolar = [1000, '1달러',2000, '2달러',3000, '3달러']
print(count)
print(cars)
print(wondolar)
print("="*20)
print(count[0]) # 1
print(cars[2]) # 승용차
print(wondolar[-1]) # 3달러
print("="*40)

# 리스트 조회 / 변경 / 추가
cheeses = ['체다','모짜렐라','까망베르','리코타']
print(cheeses)

cheeses[0] = '크림' # '체다'를 '크림'으로 변경
print(cheeses)

all = cheeses + ['블루'] # list = list + list
print(all)
print(cheeses) # 원본 chesses list는 변한게 없다.
print("="*40)

# 리스트 슬라이싱
# 리스트도 문자열과 같이 슬라이싱으로 일부만 추출할수있다.
# 슬라이싱을 하면 새로운 리스트가 생성되며(원본 리스트는 변함이 없으며), 이것을 사용하려면 별도의 변수에 저장해야 한다.
bucket = ['세계일주','악기 하나 배우기', '누군가의 후원자 되기','베스트셀러 작가']
print(bucket)

done = bucket[1:3]
print(done)

print(bucket[2:100])
print("-"*10)
print(bucket)
print("="*40)

# 리스트 관련 메서드
# list변수.index(obj) : list변수중 객체(obj)가 위치한 첫번째 인덱스를 반환한다.
# list변수.append(obj) : list변수의 끝에 obj를 추가 한다.
# list변수.insert(index , obj) : list변수의 index위치에 obj객체를 삽입한다.
# list변수.extend(list_obj) : 리스트변수에 list객체(list_obj)를 추가한다.

colors = ['red','orange','yellow']
print(colors)

print('red의 위치 : ', colors.index('red'))
print('orange의 위치 : ', colors.index('orange'))
print()

colors.append('puple') # list변수에 'puple' obj추가
print('11: ' ,colors)

colors.insert(3, 'green') # list변수의 3변 인덱스에 'green'추가
print('22: ' ,colors)

colors.extend(['yellow','black','white']) # lsit변수에 ['yellow','black','white'] 추가 (섞음, 상속) , 중복허용
print('33: ' ,colors)

print("="*40)
# 리스트 관련 메서드2
# list변수.sort()    : 리스트 구성항목 정렬
# list변수.reverse() : 리스트 구성항목 역순으로 정렬
# list변수.pop()     : 리스트의 마지막 인덱스의 항목을 반환, 반환후 인덱스가 삭제된다. (stack 구조와 비슷)
# list변수.remove()  : 지정한 항목을 리스트에서 삭제, 그러나 반환값은 없다.
# list변수.count()   : 리스트의 내무 항목의 개수를 셀때 사용한다.

colorss = ['red', 'orange','yellow','green','yellow']
print(colorss)

colorss.sort() # 항목 정렬하기
print('sort : ', colorss)

colorss.reverse() # 항목 역순으로 정렬하기
print('reverse : ', colorss)

print(colorss.pop()) # 마지막 항목 반환후 , 마지막 index삭제

colorss.remove('red') # 리스트중 해당 항목 삭제
print(colorss)

print(colorss.count('yellow')) # 리스트중 항목의 갯수 세기


print("="*40)
# 리스트 관련 메서드3
# len()     : 리스트항목 갯수를 리턴
# max()     : 리스트항목의 최대값 리턴
# min()     : 리스트항목의 최소값 리턴
# sum()     : 리스트항목의 합계값 리턴
# sorted()  : 리스트항목들을 오름차순으로 정렬
# list(seq) : 괄호안의 시퀀스 객체seq를 리스트로 만들어 준다.

floating = [12,837, 4.89, 4037.0, 11.19]
print('len : ', len(floating))
print('max : ', max(floating))
print('min : ', min(floating))
print('sum : ', sum(floating))
print()

print('sorted : ', sorted(floating)) # 오름차순 정렬한결과
print('floating : ', floating) # 정렬을 해도 원본리스트에는 영향이 없다.
string = "python"
print(list(string))
print("="*40)







