
'''
# if 문의 기본 예제

num = int(input('숫자를 입력하세요. : '))

if num > 10: # 조건문

    print('num은 10보다 크다.') # 실행문


# if문을 사용한 프로그램 : 속도 위반 경고하기

carSpeed = int(input('자동차의 현재 속도는 : '))

if carSpeed >= 50:

    print('속도 위반입니다.!!')


# 어린이의 신장을 입력하면 놀이기구 탑승 여부가 출력되는 프로그램(놀이기구 탑승은 신장이 최소 120cm부터 최대 160cm까지 가능하다.)

height = int(input('신장을 입력해주세요 : '))

if height >= 120 and height <= 160:

    print("탑승 가능")


# 코드 블럭의 마지막
    # 들여쓰기를 하지 않으면 코드 블록이 종료됐다고 간주한다.

num = int(input('숫자를 입력하세요. '))

if num > 10:

    print("num은 10보다 크다.")

print('num : ', num)    # 들여쓰기를 하지 않았기 때문에 조건문과 무관하게 항상 실행된다.


# 두번째 예제

# num = int(input('숫자를 입력하세요. '))

# if num > 10:

#     print('num은 10보다 크다.') # 들여쓰기를 하지 않음
#     print('num : ', num) # 들여쓰기를 하지 않음


# 코드 블록의 마지막 -2

height = int(input('신장을 입력해주세요 : '))

if height >= 120 and height <= 160:

    print('탑승 가능')

print('이것은 마지막 문장입니다.')


# 점수 합격 여부 확인 프로그램을 if문으로 작성

score = int(input('점수를 입력하세요 : '))

if score >= 80:

    print('합격입니다.')


# if문을 두개 사용하여 점수 합격 여부 프로그램 작성

score = int(input('점수를 입력해주세요 : '))

if score >= 80:

    print('합격입니다.') # 80 이상인 경우 실행

if score < 80:

    print('아쉽습니다. 다시 도전해주세요') # 80 미만인 경우 실행


# 놀이기구 탑승 여부를 if-else문을 사용하여 구현

height = int(input('신장을 입력해주세요 : '))

if height >= 120 and height <= 160:

    print("탑승이 가능합니다.")

else:

    print("탑승이 불가능합니다.")


# if-else문을 이용하여 점수 합격 여부 확인

score = int(input('점수를 입력하세요 : '))

if score >= 80: # 80이상인 경우 실행

    print('합격입니다.')

else:

    print('아쉽습니다. 다시 도전해주세요')


# pass 키워드 사용
# 프로그램에서 조건문을 코딩할 때 실행문이 아직 정해지지 않은 겅우에 사용함

score = int(input('점수를 입력해주세요 : '))

if score >= 80:

    pass

else:

    pass



# 자동 온도 조절 장치 만들기

temp = int(input('기계 온도를 입력하세요. : '))

if temp >= 40:

    print('팬(Fan) 가동')

else:

    print('팬(Fan) 중지')


# 사용자가 입력한 양의 정수를 3으로 나눈 후 소수점 첫 자리에서 반올림한 정수 출력

number = int(input('양의 정수 입력 : ')) # 사용자가 양의 정수 입력

result = number / 3 # 3으로 나눈다.

if(result - int(result)) >= 0.5: #소수 첫 번째 자리가 5 이상이면

    result = int(result) + 1 # 올림

else:

    result = int(result) # 버림

print('결과 : ', result) # 반올림한 결과 출력


# while True에 사용자가 입력한 양의 정수를 3으로 나눈 후 소수점 첫 자리에서 반올림한 정수 출력

while True:

    number = int(input('양의 정수 입력 : ')) # 사용자가 양의 정수 임력

    result = number / 3 # 3으로 나눈다.

    if (result - int(result)) >= 0.5: # 소수 첫 번째 자리ㅏ 5이상이면

        result = int(result) + 1 # 올림

    else:

        result = int(result) # 버림

    print('결과 : ', result) # 반올림한 결과 출력


# 다이어그램을 보고 조건문을 이용한 프로그램 작성

mileage = 1200

if mileage >= 1000:

    print('마일리지 사용 가능')

else:

    print('마일리지 사용 불가능')


# if elif else문을 사용하여 요구사항에 맞는 프로그램 작성

score = int(input('점수를 입력하세요 : '))

if score >= 90: # 점수가 90점 이상이면 'A'출력

    print('A')

elif score >= 80: # 점수가 90점 미만 80점 이상이면 'B' 출력

    print('B')

elif score >= 70: # 점수가 80점 미만 70점 이상이면 'C' 출력

    print('C')

elif score >= 60: # 점수가 70점 미만 60점 이상이면 'D' 출력

    print('D')

else: # 점수가 60점 미만임년 'F'를 출력

    print('F')


# score가 점수에 상관없이 모두 'D'를 출력하게 하기

score = int(input('점수를 입력하세요 : '))

if score >= 60: # 60점 이상이면 'D' 출력

    print('D')

elif score >= 80:

    print('B')

elif score >= 70:

    print('C')

elif score >= 90:

    print('A')

else:

    print('F')


# 복합 연산을 사용하여 요구 사항에 맞는 프로그램 만들기

score = int(input('점수를 입력하세요 : '))

if score >= 60 and score < 70: # 60 이상 70 미만이면 'D' 출력

    print('D')

elif score >= 80 and score < 90: # 80이상 90 미만이면 'B' 출력

    print('B')

elif score >= 70 and score < 80: # 70이상 80 미만이면 'C' 출력

    print('C')

elif score >= 90: # 90 이상이면 'A' 출력

    print('A')

else: # 60 미만이면 'F' 출력

    print('F')


# 자동 주문 시스템 만들기

print('Good morning. Nice to meet you.')

print('Where are you from?')

print('Please select a number.')

choiceNumber = int(input('1. 대한민국 2. USA 3. 中国'))


if choiceNumber == 1:

    print('주문하시겠어요?')

elif choiceNumber == 2:

    print('Would you like to order?')

elif choiceNumber == 3:

    print('您要点菜吗？')

else:

    print('Would you like to order?')


# 국가재난지원금 수령액 조회하기

peopleNumber = int(input('인원수를 입력해주세요 : '))

if peopleNumber == 1:

    print('400,000원 지원')

elif peopleNumber == 2:

    print('600,000원 지원')

elif peopleNumber == 3:

    print('800,000원 지원')

elif peopleNumber == 4:

    print('1,000,000원 지원')


# 컴퓨터가 임의로 생성한 난수가 홀수인지 짝수인지 판별

# 컴퓨터가 임의로 생성한 난수가 홀수인지 짝수인지 맞추는 게임

import random

randNum = random.randint(1, 100)

print('홀짝 맞추기 게임')

userNum = int(input('홀수이면 1, 짝수이면 2번을 눌러주세요 : '))

print('생성된 난수는 ', randNum, '입니다.')

if randNum % 2 == userNum % 2:

    print('정답')

else:

    print('오답')


# 난수를 이용한 가위바위보 게임 만들기.py

import random

randNum = random.randint(1, 3)

print('가위바위보 게임')

userNum = int(input('가위면 1, 바위면 2, 보면 3을 입력해주세요 : '))

print('컴퓨터가 만든 수', randNum)

if (userNum == 1 and randNum == 3) or (userNum == 2 and randNum == 1) or (userNum == 3 and randNum == 2):

    print('너 이김')

elif (userNum == 1 and randNum == 2) or (userNum == 2 and randNum == 3) or (userNum == 3 and randNum == 1):

    print('너 짐')

elif userNum == randNum:

    print('비김')


# if~elif문을 사용하여 BMI 지수 출력

bmi = int(input('BMI 지수를 입력하세요. '))

if bmi > 140:

    print('고도 비만')

elif bmi > 120:

    print('비만')

elif bmi > 110:

    print('과체중')

elif bmi > 90:

    print('정상 체중')

elif bmi <= 90:

    print('저체중')


# 중첩 조건문 사용

num = int(input('정수 입력 : '))

if num > 0:

    if num % 2 == 0:

        print('num은 짝수입니다.')

else:

    print('num은 양수가 아닙니다.')


# 중첩 조건문 사용 -2

num = int(input('정수 입력 : '))

if num > 0:

    if num % 2 == 0:

        print('num은 짝수')

    else:

        print('num은 홀수')

else:

    print('num은 양수가 아닙니다.')


# 짝수 / 홀수를 판단하는 중첩 조건문

num = int(input('양의 정수를 입력하세요. : '))

if num > 0: # num이 양수라면

    print('num : ', num)

    if num % 2 == 0: # num을 2로 나눈 나머지가 0이라면

        print('num은 짝수')

    else: # num을 2로 나눈 나머지가 0이 아니라면

        print('num은 홀수')

else:

    print('num은 양수가 아니다.')


# 버스 전용차로 단속 프로그램

print('1. 월 ~ 금, 2. 토요일, 3. 공휴일')

dayWeek = int(input('요일을 선택하세요. : '))

if dayWeek == 1:

    print('버스 전용차로 단속 중입니다.')

    print('1. 버스, 2. 승용차')

    carType = int(input('차종을 선택하세요. : '))

    if carType != 1:

        print('버스 전용차로 위반!!')

    else:

        print('버스입니다.')

else:

    print("토요일 및 공휴일은 단속하지 않습니다.")


# 출생연도 끝자리와 나이를 입력하면 요구사항에 맞춰 마스크를 구입할 수 있는 요일 출력

endBirthYear = int(input('출생 연도 끝자리 입력 : '))

age = int(input('만 나이 입력 : '))

if age < 65:

    if endBirthYear == 1 or endBirthYear == 6:

        print('월요일에 구매 가능합니다.')

    elif endBirthYear == 2 or endBirthYear == 7:

        print('화요일에 구매 가능합니다.')

    elif endBirthYear == 3 or endBirthYear == 8:

        print('수요일에 구매 가능합니다.')

    elif endBirthYear == 4 or endBirthYear == 9:

        print('목요일에 구매 가능합니다.')

    elif endBirthYear == 5 or endBirthYear == 0:

        print('금요일에 구매 가능합니다.')

else:

    print('언제든지 구매 가능합니다.')


# 올림픽 오륜기 그리기

import turtle

t = turtle.Turtle()

t.shape('turtle')

t.speed(8)

t.circle(50) # 반지름이 50인 원을 그린다.

t.up() # 그리기를 중단한다.
t.goto(90, 0) # 좌표를 (90, 0)으로 이동한다.
t.down() # 그리기를 시작한다.

t.circle(50) # 반지름이 50인 원을 그린다.

t.up() # 그리기를 중단한다.
t.goto(180, 0) # 좌표를 (180, 0)으로 이동한다.
t.down()

t.circle(50)

t.up() # 그리기를 중단한다.
t.goto(45, -50) # 좌표를 (45, -50)으로 이동한다.
t.down()

t.circle(50)

t.up()
t.goto(135, -50) # 좌표를 (135, -50)으로 이동한다.
t.down()

t.circle(50)

'''

'''
# 올림픽 오륜기 그리기

import turtle 

t = turtle.Turtle()

t.shape('turtle')

t.speed(10)

t.circle(50) #반지름이 50인 원을 그린다.
t.up() # 그리기를 중단한다.

t.goto(80, 0) # 좌표를 (80, 0)으로 이동한다.
t.down() # 그리기를 시작한다.
t.circle(50) # 반지름이 50인 원을 그린다.
t.up() # 그리기를 중단한다.

t.goto(160, 0) # 좌표를 (160, 0)으로 이동한다.
t.down() # 그리기를 시작한다
t.circle(50) # 반지름이 50인 원을 그린다.
t.up() # 그리기를 중단한다.

t.goto(40, -70) # 좌표를 (40, -70)으로 이동한다.
t.down() # 그리기를 시작한다.
t.circle(50) # 반지름이 50인 원을 그린다.
t.up() # 그리기를 중단한다.

t.goto(120, -70) # 좌표를 (120, -70)으로 이동한다.
t.down() # 그리기를 시작한다.
t.circle(50) # 반지름이 50인 원을 그린다.
t.up() # 그리기를 중단한다.


# 올림픽 오륜기 채색

import turtle

t = turtle.Turtle()

t.shape('turtle')

t.speed(10)

t.fillcolor('blue') # 색상을 blue로 설정한다.
t.begin_fill() # 채색 시작
t.circle(50) # 반지름이 50인 원 그리기
t.end_fill() # 채색 종료

t.up() # 그리기 종료

t.goto(80, 0) # 좌표를 (80, 0)으로 이동한다.
t.down() # 그리기 시작
t.fillcolor('black') # 색상을 'black'으로 설정한다.
t.circle(50) # 반지름이 50인 원 그리기
t.end_fill() # 채색 종료
t.up() # 그리기 종료

t.goto(160, 0) # 좌표를 (160, 0)으로 이동한다.
t.down() # 그리기 시작
t.fillcolor('red') # 색상을 'red'로 설정한다.
t.circle(50) # 반지름이 50인 원을 그린다.
t.end_fill() # 채색 종료
t.up() # 그리기 종료

t.goto(40, -70) # 좌표를 (40, -70)으로 이동한다.
t.down() # 그리기 시작
t.begin_fill('yellow') # 색상을 'yellow'로 이동한다
t.circle(50) # 반지름이 50인 원을 그린다.
t.end_fill() # 채색 종료
t.up() # 그리기 종료

t.goto(120, -70) # 좌표를 (120, -70)으로 이동한다.
t.down() # 그리기 시작
t.begin_fill('green') # 색상을 'green'으로 설정한다.
t.circle(50) # 반지름이 50인 원을 그린다.
t.up() # 그리기 종료


# 차량 2부제 프로그램

from datetime import datetime # 날짜 모듈 불러오기

dayNum = datetime.today().day # 현재 일(날짜) 구하기
carNum = int(input('차량 번호 4자리를 입력하세요 : ')) # 차량 번호 입력하기

print('오늘 날짜 : ', dayNum, '일')

if dayNum % 2 == 0:

    print('오늘 입차 : 번호가 짝수인 차량')

else: 

    print('오늘 입차 : 번호가 홀수인 차량')

if dayNum % 2 == carNum % 2:

    print('귀하의 차량은 입차 가능합니다.')

else:

    print('귀하의 차량은 입차 불가합니다.')

# 차량 2부제 프로그램 -2

from datetime import date, datetime # 날짜 모듈 불러오기

dayNum = datetime.today().day # 현재 일(날짜)구하기
carNum = int(input('차량 번호 4자리를 입력해주세요 : ')) # 차량 번호 입력하기

print('오늘 날짜는 %d일 입니다' %dayNum)

if dayNum % 2 == 0:

    print('오늘 짝수 가능')

else:

    print('오늘 홀수 가능')

if dayNum % 2 == carNum % 2:

    print('입차 가능')

else:

    print('입차 불가능')
    
    
# 생존율 출력 프로그램

lifetime = int(input('최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요 : '))

if lifetime <= 60:

    print('생존율 : 85%')

elif lifetime <= 120:

    print('생존율 : 76%')

elif lifetime <= 180:

    print("생존율 : 66%")

elif lifetime <= 240:

    print('생존율 : 57%')

elif lifetime <= 300:

    print('생존율 : 47%')

elif lifetime <= 360:

    print('생존율 : 37%')

else:

    print('생존율 : 25% 미만')
    
    
# 생존율 출력 프로그램 -2


while True:

    lifetime = int(input('최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요 : '))

    if lifetime <= 60:

        print('생존율 : 85%')

    elif lifetime <= 120:

        print('생존율 : 76%')

    elif lifetime <= 180:

        print("생존율 : 66%")

    elif lifetime <= 240:

        print('생존율 : 57%')

    elif lifetime <= 300:

        print('생존율 : 47%')

    elif lifetime <= 360:

        print('생존율 : 37%')

    else:

        print('생존율 : 25% 미만')
        
        
# 전기 요금 계산 프로그램

basicPrice = 0 # 기본 요금
unitPrice = 0 # 단가
totalPrice = 0 # 전기 요금

amount = float(input('전기 사용량을 입력하세요. : '))

if amount > 400:

    basicPrice = 7300
    unitPrice = 280.6

elif amount > 201:
    basicPrice = 1600
    unitPrice = 187.9

else:

    basicPrice = 910
    unitPrice = 99.3

totalPrice = amount + unitPrice + basicPrice

print('사용량 : ', amount, 'kwh')
print('기본요금 : ', basicPrice, '원')
print('단가 : ', unitPrice, '원')
print('전기 요금 : ', totalPrice, '원')


# 반복문 없이 '안녕하세요'를 5번 출력하기

print('안녕하세요')
print('안녕하세요')
print('안녕하세요')
print('안녕하세요')


# 반복문을 사용하여 '안녕하세요'를 100번 출력하기
# '안녕하세요'를 100번 출력

for i in range(100):

    print('안녕하세요')
    
    
# 반복문을 사용하여 안녕하세요를 100번 출력하기 -2

for i in range(100):

    print('안녕하세요 %d' %i)

print(i)


# for in문 구성
for i in range(1, 11, 1):

    print(i)
    
    
# 1~10까지 출력하기

for i in range(1, 11, 1): # 1부터 10까지 1씩 증가하면서

    print(i) # print(i)를 10회 실행한다.
    

# 2 ~ 8 사이의 짝수 출력하기

for num in range(2, 10, 2): # 2부터 9까지 2씩 증가
    print('num = ', num)
    
    
# 0부터 9까지 3씩 증가

for i in range(0, 10, 3):

    print('안녕하세요 %d' %i)

print(i)


# 1부터 9까지 3씩 증가

for i in range(1, 10, 3): # 1부터 9까지 3씩 증가
    print('안녕하세요 %d' %i)

print(i) 


# 사용자가 입력한 횟수만큼 '메일 발송!' 문자열 출력하기

num = int(input('메일 발송 횟수를 입력하세요. : ')) # 메일 발송 횟수 입력


for num in range(1, num + 1, 1): # 1부터 num + 1까지 1씩 증가
    print('메일 발송')
    

# for in문 활용

num = int(input('수 입력'))

for i in range(num):
    print('안녕하세요 %d' %i)
    
    
# 1 ~ 10사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수 짝!'을 출력

for num in range(1, 11, 1): # 1부터 10까지 1씩 증가

    print('num = %d' %num)

    if num % 3 == 0:

        print('3의 배수 짝!')
        
        
# 1 ~ 10 사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수' 출력

for num in range(1, 11, 1): # 1부터 10까지 1씩 증가

    print('num = %d' %num)

    if num % 3 == 0:

        print('3의 배수!')
        
        
# 1 ~ 10 사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수!'출력

for num in range(1, 11, 1): # 1부터 10까지 1씩 중가

    print('num = ', num)

    if num % 3 == 0:
        print('3의 배수!')
        
        
# 구구단 5단 출력하기 -1

for num in range(1, 10, 1): # 1부터 9까지 1씩 증가
    print(5, end = '')
    print(' * ', end = '')
    print(num, end = '')
    print(' = ', end = '')
    print(5 * num)
    
    
# 구구단 5단 출력하기 -2

for num in range(1, 10): 
    print('5 * %d = %d' %(num, 5 * num))
    
    
'''

'''
# 1 ~ 10까지 정수의 합 출력

sum = 0

for num in range(1, 11, 1): # 1부터 10까지 1씩 증가
    sum = sum + num


print('sum = ', sum)


# 사용자가 원하는 곳에서 사용자가 원하는 값까지 구하기

sum = 0

start = int(input('몇부터 더할까요? : '))
limit = int(input('몇까지 더할까요? : '))

for num in range(start, limit + 1, 1): # start부터 limit + 1까지 1씩 증가

    sum = sum + num

print('sum = %d' %sum)


# for문을 이용해서 문자열 'hello Python!'을 5번 출력하는 프로그램

for i in range(1, 6, 1): # 1부터 5까지 1씩 증가

    print('Hello Python!')
    
    
# for문을 이용해서 1 ~ 100까지 정수 중에서 3과 7의 공배수와 최소공배수 출력

minNum = 0

for num in range(1, 101, 1): # 1부터 100까지 1씩 증가

    if num % 3 == 0 and num % 7 == 0:

        print('3과 7의 공배수 : ', num)

        if minNum == 0 : minNum = num

print('3과 7의 공배수 : ', minNum)


# for문을 이용해서 1 ~ 100까지의 정수 중에서 3과 7의 공배수와 최소공배수 출력

min = 1

for num in range(1, 101, 1): # 1부터 100까지 1씩 증가

    if num % 3 == 0 and num % 7 == 0:
        
        print('공배수 %d' %num)

        if min == 1:

            min = num

print('최소공배수 %d' %min)


# range 함수 단계 생략

for i in range(1, 11):  # 단계 생략 (단계에 들어가는 데이터를 1이라 생각하고 1씩 증가시킴)

    print(i)


# range()함수 시작 생략

for i in range(11): # 시작이 생략된 경우 시작에 해당하는 데이터를 0으로 생각한다.(0부터 10까지 1씩 증가하며 출력)
    print(i)
    
    
# range() 함수 단계 감소

for i in range(10, 0, -1): # 10부터 1까지 -1씩 감소

    print(i)
    
    
# for문 이터러블(문자열 이용)

for c in 'hello':
    print(c, end = ' ')
    
# for문 이터러블 -2.py

for c in "Hello":

    print(c)
    
# 50보다 작은 7의 배수를 출력하는 프로그램

for num in range(50):

    if num % 7 == 0:

        print(num)
        

# 50보다 작은 7의 배수를 출력하는 프로그램

for num in range(1, 50): # 1부터 49까지 1씩 증가

    if num % 7 == 0:

        print(num, end = ' ')
        
        
# while문을 이용해서 1 ~ 10까지 출력

num = 1

while num <= 10: # num이 10보다 작거나 같다면

    print('num : ', num) # num을 출력하고
    num += 1 # num을 1 증가하는 실행을 반복
    
    
# 1 ~ 30까지의 정수 중 홀수와 짝수를 구분하여 출력

num = 1

while num <= 30:

    if num % 2 == 0:

        print('짝수 : ', num)

    else:

        print('홀수 : ', num)

    num += 1
    
    
# 1 ~ 30까지의 정수 중 홀수와 짝수를 구분하여 출력

num = 1

while num <= 30:

    if num % 2 == 0:

        print('짝수 : %d' %num)

    else:

        print('홀수 : %d' %num)

    num += 1
    
    
# 0 ~ 100까지의 정수 중 3과 8의 공배수와 최소공배수 구하기

num = 1

minNum = 0

while num <= 100:

    if num % 3 == 0 and num % 8 == 0:

        print('공배수 : ', num)

        if minNum == 0: minNum = num

    num += 1

print('최소공배수 : ', minNum)


# 0 ~ 100까지의 정수 중 3과 8의 공배수와 최소공배수 구하기 -2.py

num = 1
min = 1

while num <= 100:

    if num % 3 == 0 and num % 8 == 0:

        print('공배수 : %d' %num)

        if min == 1:

            min = num

    num += 1

print('최소공배수 %d' %min)


# for문을 이용해서 1부터 5까지의 정수를 순차적으로 출력

for num in range(1, 6, 1):

    print('num : ', num)
    
    
# while문을 이용해서 1부터 5까지 정수를 순차적으로 출력

num = 1

while num < 6:
    print('num' ,num)

    num += 1
    
    
# for문을 이용해서 0부터 10까지 정수의 합 구하기

sum = 0

for num in range(0, 11):
    sum += num


print('sum : ', sum)


# while문을 이용해서 0부터 10까지 정수의 합 구하기

sum = 0
num = 0

while num <= 10:

    sum += num

    num += 1

print('sum : ', sum)


# while문을 이용해서 0부터 10까지 정수의 합 구하기 -2.py

sum = 0
num = 1

while num <= 10:

    sum += num # sum = sum + num
    num += 1

print(sum)


# while문을 이용해서 정수의 곱 구하기

sum = 1
num = 1

while num <= 10:

    sum *= num # sum = sum * num
    num += 1 

print(sum)


# 냉방기능 프로그램 for문 이용

currentTemperature = 30.0
targetTemperature = float(input('희망 온도를 입력해주세요 : '))

for i in range(1000): # 반복 횟수를 정확히 설정할 수 없다.

    currentTemperature -= 0.1

    print('현재 온도 : ', format(currentTemperature, '.2f'))

    if currentTemperature <= targetTemperature:

        break

print('냉방 기능 종료!!')


# 냉방 기능 프로그램 while문 이용

currentTemperature = 30.0
targetTemperature = float(input('희망 온도를 입력하세요 : '))

while targetTemperature < currentTemperature:

    currentTemperature -= 0.1

    print('현재 온도 : ', format(currentTemperature, '.2f'))

print('냉방 기능 종료 !!')


# 냉방 기능 프로그램 while문 이용 -2

cT = 30.0
tT = float(input('희망 온도 : '))

while tT < cT:

    cT -= 0.1

    print('햔제 온도 %5.2f' %cT)
    print('현재 온도 ', format(cT, '.2f'))

print('에어컨 끔')


# num이 3보다 작을 경우 '안녕하세요'를 출력

num = 0 

while num < 3:
    print('안녕하세요')

    # 안녕하세요가 무한 반복됨 - while문의 조건식 결과가 프로그램을 실행하는 내내 참(True)이기 때문이다.
    
    
# 무한 루프 해결

# 무한 루프란? : 반복문을 빠져나오지 못하고 영원히 반복하는 것을 말한다.

# 조건식의 결과로 거짓이 나올 수 있어야 무한루프에 빠지지 않는다.

num = 0

while num < 3:

    print('안녕하세요')

    num += 1
    
    
# 사용자의 선택에 따라 게임의 종료와 진행을 결정하는 프로그램

flag = True

while flag:

    inputData = int(input('1 : 진행, 2. 종료'))

    if inputData == 1:
        flag = True
        print('게임 진행')

    else:
        flag = False
        print('게임 종료')
        
        
# 1 ~ 10까지의 정수 중 홀수만 더하기(continue 키워드 사용)

for num in range(1, 11): #1부터 10까지 1씩 증가

    if num % 2 == 0: 
        continue # 짝수는 생략
    print(num)
    
    
# 1 ~ 10까지 정수를 더하되 결과가 30이상이 될 때 정수를 찾기(break 키워드 사용)

num = 1
sum = 0

while num < 11:

    sum += num

    if sum >= 30:

        print('num : ', num)

        break

    num += 1


# 1부터 5까지 정수를 출력하고 반복문이 끝나면 완료메세지 출력(for~else문 사용)

for num in range(1, 6): # 1부터 5까지 1씩 증가

    print(num)

else:

    print('반복이 끝났습니다.')
    
    
# pass 키워드 사용

for i in range(5):
    pass


# 삼각형의 넓이 구하기

count = 1
maxArea = 150

while True:

    result = ((count * 2) * (count * 3)) / 2

    if result > maxArea:
        break

    print('삼각형의 넓이 : ', result)

    count += 1
    

# 삼각형의 넓이 구하기 -2

count = 1
maxArea = 150

while True:

    result = ((count * 2) * (count * 3)) / 2

    if result > maxArea:

        break

    print('삼각형 넓이 : %d' %result)

    count += 1
    
    
# 삼각형의 넓이 구하기 -3.py

count = 1
maxArea = 150

while True:

    result = ((count * 2) * (count * 3)) / 2

    print('삼각형 넓이 : %d' %result)

    if result > maxArea:

        break

    count += 1
    
    
# 1부터 100까지의 숫자 중 5또는 7의 배수를 제외한 나머지 정수를 출력하는 프로그램

for num in range(1, 101): # 1부터 100까지 1씩 증가

    if num % 5 == 0 or num % 7 == 0:

        continue

    print(num)
    
    
# 1부터 100까지의 숫자 중 5또는 7의 배수를 제외한 나머지 정수를 출력하는 프로그램

for num in range(1, 101): #1부터 100까지 1씩 증가

    if num % 5 == 0 or num % 7 == 0:

        continue

    print(num)
    
    
# 중첩 반복문을 이용하여 점찍기
# 1행에서는 한 개, 2행에서는 두 개, 3행에서는 세 개, .... 5행에서는 다섯 개를 출력

for num1 in range(1, 6): # 1에서 5까지 1씩 증가

    for num2 in range(num1): # num만큼 매번 반복

        print('*', end = '')

    print()
    
    
# 구구단 전체 출력(일반)

for n1 in range(1, 10, 1): # 1부터 9까지 1씩 증가
    for n2 in range(2, 10, 1): # 2부터 9까지 1씩 증가
        print(n2, end = '')
        print(' x ', end = '')
        print(n1, end = '')
        print(' = ', end = '')
        print(n2 * n1, '\t', end = '')

    print()
'''
# 구구단 전체 출력(한줄로)

for n1 in range(1, 10, 1): # 1부터 9까지 1씩 증가
    for n2 in range(2, 10, 1): # 2부터 9까지 1씩 증가

        print(f'{n1} x {n2} = {n1 * n2}')

    print()
