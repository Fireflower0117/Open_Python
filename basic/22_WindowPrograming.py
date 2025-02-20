# 파이썬 윈도우 프로그래밍
# ---   학습목표 ---
# ■ 파이썬에서의 윈도우 프로그래밍 관련 툴을 알고 설명할수있다.
# ■ GUI지원 라이브러리와 프레임워크 종류를 알고 설명할수있다.
# ■ Tkinter표준 GUI라이브러리에서 제공되는 Label위젯을 활용하여 윈도우창 안에 텍스트나 이미지를 나타낼수있다.

print("=== 파이썬 윈도우 프로그래밍" , "="* 60)
# - 파이썬 윈도우 프로그래밍 종류
# - GUI지원 라이브러리 : tkinter[티-케이-인터]내부 라이브러리, pillow외부 라이브러리
# - 파이썬에서 데스크탑 프로그램 혹은 GUI 프로그램을 만들기 위해서는 여러 GUI Framework(혹은 Toolkit)들을 사용할수있음

#     애플리케이션       │                                      개요
#--------------------------------------------------------------------------------------------------------------
#   PYQT5, 오픈소스             ● Tkinter로부터 Qt[큐브,큐티] 프레임워크를 파이썬에서 사용하도록 지원함
#   개인용만 무료                  동일한 파이썬 코드를 사용하여 Windows,Mac,Linux에서 모두 동작하는 GUI프로그램을 작성
#   RiverBank에서              ● Qt는 C++로 작성된 크로스 플랫폼 프레임워크로 하나의 언어에서 작성된 라이브러리나 서비스를
#   지속적인 관리                  다른 언에에서 사용할수있도록 하는 Language Binder중 하나임 Qt v4는 더이상 지원되지 않으며 Qt v5사용권장
#--------------------------------------------------------------------------------------------------------------
#   PyGTK                     ● C언어로 작성된 객체지향 위젯인 GTK툴킷을 파이썬에서 사용가능
#--------------------------------------------------------------------------------------------------------------
#   PySide                    ● PYQT4버전과 비슷하며 상업용으로도 무료, 관리소홀로 상업용 프로젝트에는 권장하지 않음
#--------------------------------------------------------------------------------------------------------------

print();print()
print("=== GUI지원 라이브러리" , "="* 60)
# - Tkinter 표준 GUI라이브러리 Python 설치시 기본적으로 내장되어 있는 파이썬 표준 라이브러리이기때문에 쉽고 간단한 GUI(Graphic User Interface)프그래금을 만들경우 활용
#   1) Tcl/Tk : 간단한 형태의 스크립트 프로그래밍 언어인 Tcl(Tool Command Language)과
#               이것의 라이브러리인 Tk를 파이썬에서 사용할수있도록한 경량 GUI모듈이다.
#   2) Tkinter를 사용하기 위해서는 먼저 tkinter모듈을 import해야 한다.
#      ex)  from tkinter import *  # GUI 관련 모듈을 제공해주는 표준 윈도우 라이브러리
# - pillow 외부 라이브러리인 경우 별도의 설치과정이 필요함
#   ex)  $$>pip install pillow # 이미지 필터 처리를 위한 외부 라이브러리, 밝기, 노이즈, 흑백처리 등

from tkinter import *  # GUI관련 모듈을 제공해주는 표준 윈도우 라이브러리
window = Tk()          # Root window, Base window

#window.mainloop()      # window 관련작업 완료후, 이벤트 메시지 루프 (mainloop()) 호출


print();print()
print("=== root window 생성하기" , "="* 60)
#window.title()                             # Window 제목
#window.geometry()                          # 창 "가로x세로"  ("*"이 아니라 영문소문자"x" ,  '"' 큰따옴표로 묶을것)
#window.resizable(width=True, height=False) # False지정 창크기가 고정됨

'''
window.title("오픈노트 파이썬 윈도우")
window.geometry("600x600")                  # 창 "가로x세로"
window.resizable(width=True, height=False)  # 가로(width)는 사이즈 조절가능 , 세로(height)는 사이즈조절 불가
window.mainloop()                           # window 관련작업 완료후, 이벤트 메시지 루프 (mainloop()) 호출
'''

print();print()
print("=== Label위젯" , "="* 60)
window.title("오픈노트 파이썬 윈도우")
window.geometry("480x150")
window.resizable(width=False, height=False)

# label 생성
label1 = Label(window, text="안녕하세요 오픈노트에 오신것을 환영합니다.")
label1.pack()

# fg = "글자의 전경색" (ForeGround Color)
label2 = Label(window, text="폰트 및 색상 지정",\
               font = ("나눔고딕",24) , fg='blue')
label2.pack()

# bg = "글자의 배경색" anchor = N NE E SE S SW W NW CENTER 중 하나를 지정
label3 = Label(window,\
               text = "문단의 배경색상, 크기, 문단의 글자 위치지정",\
               bg="yellow", width=50, height='3', anchor=SW)
label3.pack()
window.mainloop()


#  ---  Python tkinter 강좌 참조 ---
#  https://076923.github.io/posts/Python-tkinter-1/