# 코드 블럭의 마지막
    # 들여쓰기를 하지 않으면 코드 블록이 종료됐다고 간주한다.

num = int(input('숫자를 입력하세요. '))

if num > 10:

    print("num은 10보다 크다.")

print('num : ', num)    # 들여쓰기를 하지 않았기 때문에 조건문과 무관하게 항상 실행된다.

'''
두번째 예제

num = int(input('숫자를 입력하세요. '))

if num > 10:

    print('num은 10보다 크다.') # 들여쓰기를 하지 않음
    print('num : ', num) # 들여쓰기를 하지 않음