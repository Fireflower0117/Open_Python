# File I/O Control
# --- 학습목표 ---
# ■ 파일 입출력 3단계 과정을 설명할수있다.
# ■ 텍스트 파일과 바이너리 파일의 차이를 설명할수있다.
# ■ write()함수를 사용하여 파일을 열고 데이터를 쓸수있다
# ■ readline() , readlines() 함수를 사용하여 파일을 열고 데이터를 읽을수있다.

# ■ 파일로부터 데이터를 읽기 위해 사용되는 readlines()와 readline()함수의 차이점을 설명할수있다.
# ■ 파일객체 변수를 이용하여 파일로 부터 읽어 온 내용을 화면에 직접 출력할수있다.
# ■ with문을 이용하여 파일 입출력을 보다 안정적으로 처리하도록 코딩할수있다.
# ■ 기존 파일 데이터의 맨 끝에 새로운 데이터를 추가할수있다.

print("=== 파일입출력의 개요" , "="* 60)
# - 파일 입출력 단계
# 파일입출력은 파일열기 => 파일처리 => 파일닫기 3단계로 이루어진다.
# 1단계 : 파일열기  open()
# 2단계 : 파일처리  write(), readline(), readlines(), read()
# 3단계 : 파일닫기  close()

# 파일의 종류  텍스트파일 , 바이터리파일

# - open()함수의 형식
#   파일_객체_변수 = open('파일명', '파일모드')
#   파일모드 : 내용
#   w  : 쓰기모드. 파일에 데이터를 기록하고자 할때사용
#        파일이 폴더에 존재하지 않으면 신규로 파일을 생성함
#        만일 동일한 파일이 존재하면 기존파일을 삭제후, 파일을 생성함
#   r  : 읽기모드. 파일에 데이터를 읽어오고자 할때 사용
#        파일이 폴더에 존재하면 파일 객체를 반환하고, 존재하지 않으면 OSError이 발생
#        파일모드의 기본값이기 때문에 생각이 읽기모드로 열림
#   a  : 추가모드. 파일에 데이터를 추가하고자 할때 사용
#        파일이 폴더에 존재하지 않으면 파일을 신규 생성
#        만일 동일한 파일이 존재하면 파일안에서 기존 데이터에 이어서 추가함

f = open("fileIO/myfile.txt", "w") # 빈파일이 생성된다.
f.close() # 닫기


print();print()
print("=== 파일을 열고 데이터 쓰기 - write()" , "="* 60)
# - 파일에 데이터를 쓰기 위해서는 파일을 열때 파일 열기모드를 'w'로 지정해야 한다.
# - open()함수 안에 파일명을 적을떄 파일명 앞에 파일이 놓이 위치를 가리키는 경로를 같이 지정할수있다.
# - 절대경로와 상대경로
#   1) 절대경로 : 작업폴더와 무관하게 절대적인 위치를 가리키는 경로
#          ex) c:\\windows\\System32
#   2) 상대경로 : 소스코드(~.py)가 있는 작업폴더를 기준으로 상대적 위치경로
#          ex) ..\\Python37#
#               ./source/image
#               fileIO/image
# - 파일에 데이터를 기록하고자 할떄는 write()함수를 사용한다.

f = open("d://opennote//opentest.txt", "w") # 파일 폴더까지는 수동 생성해야함
memo = "파일을 열었으니 데이터를 저장하자"
f.write(memo)
f.close()


print();print()
print("=== 파일을 열고 데이터 읽기 - readline()" , "="* 60)
# - 파일의 데이터를 읽기 위해서는 파일을 열때 열기모드를 'r'로 지정해야 한다.
# - readline()함수는 파일의 데이터를 한줄씩 읽어오는 기능을 가진 함수다.
# - 파일의끝 (EOF : EndOfFile)에 도착하면 readline()함수는 None을 반환한다.1

f = open("d://opennote//myfile.txt", "w")  # 쓰기모드('r')로 파일열기
poem = '''
살어리 살어리랏다. 청산에 살어리랏다.
머위랑 달래랑 먹고 청산에 살어리랏다.
얄리얄리 얄랴셩 얄라리 얄라
'''
f.write(poem) # 내용작성
f.close() # 파일닫기

f = open("d://opennote//myfile.txt", "r") # 읽기모드로 파일 열기
while True:
    sentence = f.readline()  # 파일을 한줄씩 읽기
    if not sentence :  # 파일이 비어있으면(EOF)면 while문 탈출
        break
    print(sentence)
   #print(type(sentence)) # String 형식
f.close() #  파일 닫기


print();print()
print("=== 파일을 열고 데이터 읽기 - readlines()" , "="* 60)
# - readlines()함수는 파일의 모든 줄을 한꺼번에 읽어서 가져온다.
# - readlines()함수는 파일의 모든 내용을 줄 단위로 읽어서 각각의 줄을 항목으로 가지는 리스트 형태로 만들어 반환한다.
# - readlines()함수로 파일의 내용을 읽어올때 파일의 용량이 매유크면 처리시간이 오래걸릴수 있다.


f = open("d://opennote//myfile.txt", "w") # 쓰기모드로 파일 열기
poem = '''
살어리 살어리랏다. 청산에 살어리랏다.
머위랑 달래랑 먹고 청산에 살어리랏다.
얄리얄리 얄랴셩 얄라리 얄라

우러라 우러라 새여 자고 니러 우러라 새여
널라와 시름 한 나도 자고 니러 우리노라
얄리 얄리 얄라셩 얄라리 얄라
'''

f.write(poem) # 내용작성
f.close() # 파일닫기

f = open("d://opennote//myfile.txt", "r") # 읽기모드로 파일 열기
all = f.readlines()
print("-----")
print(all)
print("-----")

for sentence in all :
    print(sentence)
f.close()

print();print()
print("=== 파일을 열고 데이터 읽기 - read()" , "="* 60)
# - read()함수는 파일의 모든 내용을 읽어서 한꺼번에 가져온다.
# - read()함수는 파일의 모든 내용을 문자열 형태로 만들어 반환한다.
# - read()함수로 파일의 내용을 읽어 올때도 파일의 용량이 매우 크면 처리시간이 오래 걸릴수있다.

f = open("d://opennote//readFnTest.txt", "w") # 쓰기모드로 파일 열기
poem = '''
살어리 살어리랏다. 청산에 살어리랏다.
머위랑 달래랑 먹고 청산에 살어리랏다.
얄리얄리 얄랴셩 얄라리 얄라

우러라 우러라 새여 자고 니러 우러라 새여
널라와 시름 한 나도 자고 니러 우리노라
얄리 얄리 얄라셩 얄라리 얄라
'''

f.write(poem) # 내용작성
f.close() # 파일닫기

f = open("d://opennote//myfile.txt", "r") # 읽기모드로 파일 열기
string = f.read()  # 파일의 내용을 한번에 전부 읽는다.
print("type(string) : ",type(string) )
print(string)
f.close()

print();print()
print("=== 파일을 열고 데이터 읽기 - (파일 객체 변수 사용)" , "="* 60)
# - 파일 객체 변수를 이용하면 파일로부터 읽어 온 내용을 화면에 직접 출력 할수있다.
# - 파일 객체 변수에는 파일 내용이 줄 단위로 저장되어있다.
# - 파일 객체 변수를 이용하는 방법이 파일을 읽는 방법중 가장 간단하고 빠를 방법이다.

f = open("d://opennote//myfile.txt", "r")
for line in f:
    print(line)   # 개행문자가 포함된다.
f.close()



print();print()
print("=== 파일을 열고 데이터 읽기 - (With문 사용) ★ ★ ★ ★" , "="* 60)
# - with문을 이용하면 close()함수를 사용하지 않아도 파일처리를 끝내고 with문 블록을 벗어나는순간 파일을 자동으로 닫는다 ( auto close() )
# - with문을 이용한 파일 처리가 예외처리 (try ~~ exception) 보다 안전하다.
# - 파일 객체변수를 이용해서 read(), readline()등 다른 함수들을 사용할수있다.


f = open("d://opennote//fileWithTest.txt", "w") # 쓰기모드로 파일 열기
poem = '''
살어리 살어리랏다. 청산에 살어리랏다.
머위랑 달래랑 먹고 청산에 살어리랏다.
얄리얄리 얄랴셩 얄라리 얄라

우러라 우러라 새여 자고 니러 우러라 새여
널라와 시름 한 나도 자고 니러 우리노라
얄리 얄리 얄라셩 얄라리 얄라
'''

f.write(poem) # 내용작성
f.close() # 파일닫기

with open("d://opennote//fileWithTest.txt", "r") as f :
    for line in f:
        print(line)
# f.close()함수를 사용하지 않아도 자동으로 닫힌다.


print();print()
print("=== 파일에 데이터 추가하기" , "="* 60)
# - 파일에 데이터를 추가하기 위해서는 파일을 열때 파일 열기모드를 "a"로 지정해야 한다.
# - 새롭게 추가하는 데이터는 기존파일 데이터의 맨끝에 추가된다. ( append )
# - 파일에 데이터를 추가할 때도 처음 저장할떄와 마찬가지로 write()함수를 사용한다.

baseStr = '''
OpenNote는 전남 나주에 위치한 기업이다.
'''
with open("d://opennote//fileWriteTest.txt", "w") as wf :  # 쓰기모드 (기존파일이 있다면 지우고 내용을 신규작성)
    wf.write(baseStr)


with open("d://opennote//fileWriteTest.txt", "r") as rf :  # 읽기모드
    print("-------   원본 파일  -------")
    print(rf.read())

appendStr = """
주변에는 호수공원이 있어 산책하기 좋은 위치에 있다. 
멀지않은 곳에 빛가람 전망대도 있다.
"""

with open("d://opennote//fileWriteTest.txt", "a") as af :  # 추가쓰기모드 (기존파일이 있다면 내용을 가장뒤에서 추가로작성)
    af.write(appendStr)

with open("d://opennote//fileWriteTest.txt", "r") as rf : # 읽기모드
    print("-------   추가후 파일  -------")
    print(rf.read())




