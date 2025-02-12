# File I/O Control
# --- 학습목표 ---
# ■ 파일 입출력 3단계 과정을 설명할수있다.
# ■ 텍스트 파일과 바이너리 파일의 차이를 설명할수있다.
# ■ write()함수를 사용하여 파일을 열고 데이터를 쓸수있다
# ■ readline() , readlines() 함수를 사용하여 파일을 열고 데이터를 읽을수있다.

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