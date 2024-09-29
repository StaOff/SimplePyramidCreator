# 몇층을 쌓을건지 사용자에게 질문
PL = int(input("몇층을 쌓으시겠습니까?   "))  # 입력값을 정수값으로 전환

if PL > 0:
    for height in range(1, PL + 1):
        # 공백 추가하여 중앙 정렬
        print(' '*(PL-height)+'*'*(2*height-1))
    for height in range(PL-1, 0, -1):
        # 공백 추가하여 중앙 정렬
        print(' '*(PL-height)+'*'*(2*height-1))
else:
    print("올바른 숫자를 입력하시오")
