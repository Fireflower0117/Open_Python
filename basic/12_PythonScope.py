# 변수의 범위
# --- 학습목표 ---
#  ■ 전역변수와 지역변수의 차이점을 설명할수있다.
#  ■ 동일한 이름의 변수가 전역에 모두 있을때 변수의 우선적용 범위를 설명할수있다.
#  ■ 'global' 명령어의 역할을 설명 할수있다.

print("=== 전역변수와 지역변수" , "="* 60)
#  - 변수는 유효범위(Scope)에 따라 전역변수와 지역변수로 구분한다.
#  - 전역변수와 지역변수를 구분짓는 위치는 변수가 선언된 위치이다.
#    1) 전역변수
#       ● 프로그램 전체 역역(전역)에 사용할수있는 변수
#       ● 블록(함수블록 또는 클래스 블록) 밖에서 변수를 만들어야 한다.
#       ● 전역변수는 프로그램 실행 내내 사용할 수 있다.
#    2) 지역변수
#       ● 한정된 영역(지역)에서는 사용할수있는 변수
#       ● 함수블록 또는 클래스블록 내부에서 변수를 만들어야 한다.
#       ● 지역변수는 블록내 변수가 만들어 진 지점에서 생성,소멸된다.
#       ● 지역변수는 해당 지역변수가 만들어 진 함수 블록이나 클래스 블록 밖에서 사용할수없다.
#       ● 함수의 매개변수도 지역변수에 해당된다.

global_let = '전역변수'

def fnScopePrint() :
    local_let = '지역변수'
    print('fnScope내부 global_let : ', global_let)
    print('fnScope내부 local_let : ',local_let)

fnScopePrint()
print("--"*20)
print('fnScope외부 global_let : ', global_let)
#print('fnScope외부 local_let : ',local_let)  # NameError: name 'local_let' is not defined (함수내부에서 선언된 변수는 참조 불가능)

print();print()
print("=== 동일한 이름의 변수가 전역,지역에 있을떄" , "="* 60)
#  - 전역과 지역에 동일한 이름의 변수가 있어도 이 둘은 전혀 다른 변수이다.
#  - 동일한 이름의 변수가 전역과 지역에 모두 있을떄 변수 사용규칙
#    1) 먼저 해당 변수가 사용된 지역 내에서 동일한 이름의 변수를 찾는다.
#    2) 자신이 사용된 지역에서 동일한 이름의 변수가 없다면, 상위의 더 넓은 영역(상위지역 또는 전역)에서 그이름의 변수를 찾는다.

letScope = '전역변수'
def fnScope():
    letScope = '지역변수' #  변수명이 같아도 ,값을 덮어 쓰지는 않음
    print(letScope)

fnScope()  # 지역변수
print('--')
print(letScope) # 전역변수

print();print()
print("=== global 선언" , "="* 60)
#  - 지역에서 만들어 지는 변수를 전역 변수로 만들고자 할때 global 명령어를 사용 (지역변수를 전역변수로 만들떄)
#  - 전역변수의 유효범위는 프로그램 전체 이지만
#    지역 변수는 해당 지역 변수가 선언된 함수블록 이나 클래스블록 내부로 한정하기 때문에
#    함수블록이나 클래스블록 내부에서 선언된 변수에 저장된 내용을
#    함수나 클래스 외부에서 계속 사용하기 위해서 global 명령어가 사용된다.

const = "전역변수"
def fnGrobalScope():
    global const                             # 지역변수를 전역변수로 만들며, 값을 덮어 쓴다.
    const = 'Global 명령어의 역할'
    print('fnGrobalScope 함수 안 const : ',const)

fnGrobalScope()
print()
print('함수밖 const : ', const);  # let는 'global' 키워드를 사용해서 전역변수 Scope로변경,

print();print()
print("=== 변수의 범위" , "="* 60)
#  - 새로운 지역변수가 만들어 질수있는 영역은 함수내부, 클래스내부, 모듈내부 이다.

genLet = '전역변수'
def fnGenLetScope() :
    genLet = 'scope() 지역변수'
    print(genLet , '\t[fnGenLetScope 함수에서 출력]')  # 'scope() 지역변수'

    for i in range(3) :
        genLet = 'for 지역변수'
        aaa = ''
        print(genLet , '\t[fnGenLetScope for문에서 출력]') # 'for 지역변수'

    if True :
        print(genLet , '\t[fnGenLetScope if문에서 출력]')  # 'for 지역변수'


fnGenLetScope()
print(genLet, '\t\t[ scope() 함수 밖에서 출력]')
