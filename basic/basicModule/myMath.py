# myMath.py

pi = 3.14

def oneHapN(end) : # 1부터 N(end)까지의 합을 구하는 함수
    sum = 0
    for i in range(end) :
        sum += 1
    return sum

def oneGopN(end) : # 1부터 N(end)까지의 곱을 구하는 함수
    total = 1
    for i in range(end) :
        total *= i + 1
    return total