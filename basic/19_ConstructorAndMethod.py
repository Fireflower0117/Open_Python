# Class 생성자(Constructor)와 메소드(Method : function : 함수)
# ---   학습목표 ---
# ■ 생성자인 __init__() 메서드에 역할을 이해하고 정의할수있다.
# ■ 클래스 안에 생성자인 __init__()외에 필요한 메서드를 추가 정의 내릴 수 있다.
# ■ 특별한 메서드인 __str__()의 역할을 이해하고 정의 할수있다 .
# ■ 클래스 변수와 인스턴스 변수의 차이점을 설명할수있다.

print("=== __init__() 생성자" , "="* 60)
# - 생성자(Constructor)란 ?
#    ● 객체를 만들때마다 맨 처음 자동으로 실행되는 메서드
#    ● 파이썬에서는 __init__()메서드가 생성자이다.
#    ● 객체 생성시 변수를 초기화 시킬 목적으로 많이 사용된다.
#    ● __init__() 메서드는 메서드 이기때문에 "def" 키워드로 정의하고,
#      필수적으로 관례상 self가 첫번쨰 매개변수로 사용된다.
#      (생성자의 첫번째 매개변수 self는 생성되는 자신의 객체 자신을 의미한다.)
#           ex)    classe OpenNote :
#                      def __init__(self) :  # 자신의 객체 자신이다 (class OpenNote  = self)
#                           self.companyName = "OpenNote"
#                           self.address     = "전남 나주 빛가람동"

#    etc) 생성자와 반대로 소멸자 ( __del__() )도 있으나 사용될일이 사실상 거의 없다.
#         Class가 소멸될때 호출되는 함수이다.

class OpenNote :
    ''' Open Note Class Document이다.
        동료개발자와 원활한 정보공유를 위해 반드시 작성할것을 권고 한다.
    '''

    def __init__(self):  # class OpenNote의 생성자 , self = class OpenNote객체
        self.companyName = "OpenNote"
        self.address     = "전남 나주 빛가람동"

openNote1Comp = OpenNote()
openNote2Comp = OpenNote()

print("---  base  ---")
print("openNote1Comp.companyName : ", openNote1Comp.companyName, ", openNote1Comp.address", openNote1Comp.address)
print("openNote2Comp.companyName : ", openNote2Comp.companyName, ", openNote2Comp.address", openNote2Comp.address)
print()


print("---  after  ---")
openNote1Comp.companyName = "CloseNote"
openNote1Comp.address     = "전남 고담시 흑가람동"
print("openNote1Comp.companyName : ", openNote1Comp.companyName, ", openNote1Comp.address", openNote1Comp.address)
print("openNote2Comp.companyName : ", openNote2Comp.companyName, ", openNote2Comp.address", openNote2Comp.address)









