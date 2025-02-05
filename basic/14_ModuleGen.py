# 모듈 만들기
# ---  학습목표 ---
# ■ 내가 만든 파이썬 파일을 다른 파일에서 모듈로 사용할수있다.
# ■ 모듈사용에 있어서 __name__ 변수의 역할을 이해하고 사용할수있다.
# ■ 파이썬 기본 내장 모듈 가운데 keyword모듈을 활용할수있다.

print();print()
print("=== 모듈만들기" , "="* 60)
# ** 모듈 **
# - 재사용하고 싶은 함수나 변수를 하나의 파일로 만들어 저장해 놓은 일종의 파이썬파일(~~.py)이다.
# - 모듈을 사용하는 가장 큰 이유는 '재사용'에 있다.
# - 필요한 모듈을 현재 내가 작성 중인 파일에 불러와 사용하고자 할경우에는 'import' 키워드를 사용하면 된다
#   ex)   import 모듈명
# ** 모듈을 불러오는 방법 **
#  모듈을 불러오는 방법에는 여러가지가 있다.
#   ex) 1) import myMath
#       2) import myMath as my
#       3) from myMath import pi, onHapN
#       4) from myMath import *

import basicModule.myMath as myMath  # 개발자 정의 모듈
import math                # 내장모듈

print('내가 만든 모듈 사용예제')
print("myMath.pi : ", myMath.pi)
print("math.pi : ", math.pi)

print("1부터 10까지의 합 : ", myMath.oneHapN(10))
print("1부터 10까지의 곱 : ", myMath.oneGopN(10))


print();print()
print("=== __name__ 변수" , "="* 60)
# - 파이썬 파일은 모듈을 임포트(import)될 때도 실행된다.
# - 모듈이 실행될떄 불필요한 출력이 생길수 있어서 이를 구분할 필요가 있다.
# - 파이썬 파일이 직접 실행되었는지? 모듈로 임포트 되어 실행되었는지는 '__name__'변수를 통해 확인 할수있다.
#   1) 파이썬 파일이 직접 실행된 경우에는 __name__변수에 '__main__'이 저장된다.
#   2) 파이썬 파일이 모듈로 임포트되어 실행된 경우에는 __name__변수에 '모듈명'이 저장된다.
#      ** Tip : 파이썬에서 어떤 변수나 함수에 특별한 의미또는 기능을 부여할때는
#               해당변수명이나 함수명 앞과 뒤에 두개의 언더스코더 '__'문자를 붙인다.
#               => '_'는 언더바가 아니고 언더스코어이며 두개의 언더스코어 '__'는 Double UnderScore이며 약칭 '던더' 라고한다.


# teminal 에서 cd basicModule로 이동하여 직접 openNode.py를 실행해본다.
# 실행결과
# 오픈노트는 대한민국 전남 나주 빛가람동에 위치한 회사이다.
# openNote.py 파일이 실행되었다.
# __name__ :  __main__

import basicModule.openNote as openNote
# 실행결과
# 오픈노트는 대한민국 전남 나주 빛가람동에 위치한 회사이다.
# openNote.py 파일이 실행되었다.
# __name__ :  basicModule.openNote

# 결과 __name__는 실행위치에 따라 결과가 달라진다.

print();print()
print("=== if __name__ == '__main__' " , "="* 60)
# - if __name__ == '__main__'문을 이용하면 임포트 되었을때와 그렇지 않을때를 구분하여 사용할수있다.

# teminal 에서 cd basicModule로 이동하여 직접 openNode2.py를 실행해본다.
# 실행결과
# 오픈노트는 대한민국 전남 나주 빛가람동에 위치한 회사이다.
# if In openNote2.py 파일이 실행되었다.

import basicModule.openNote2 as openNote2
# 실행결과
# 클로즈노트는 라는 회사는 없다.
# else In openNote2.py 파일이 실행되었다.

print();print()
print("=== 내장 모듈 연습-keyword 모듈 " , "="* 60)
# - 내가 만드려는 기능이 구현된 모듈이 이미있다면 그모듈을 적극 활용하는것이 좋다.
# - 모듈을 활용하면 개발시간을 절약할수있고 스트레스도 줄일수있다.
# - 파이썬 내장모듈 가운데 하나인 'keyword'모듈은 파이썬의 예약어에 관련된 함수와 변수를 가지고있다.

import keyword
print("keyword.iskeyword('None') : ", keyword.iskeyword("None")) # Keyword여부 판단
print("keyword.iskeyword('int') : ", keyword.iskeyword("int")) # Keyword여부 판단
print("keyword.kwlist : ", keyword.kwlist)  # 파이썬 Keyword 목록 (예약어)---

