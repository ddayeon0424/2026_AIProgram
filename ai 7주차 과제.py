#LAB 7-1
import datetime

now = datetime.datetime.now()
hour = now.hour

print(f"오늘의 날짜 : {now.year}년 {now.month}월 {now.day}일")

if hour >= 12:
    if hour > 12:
        hour = hour - 12
    print(f"현재시간 : 오후 {hour}시 {now.minute}분 {now.second}초")
else:
    print(f"현재시간 : 오전 {hour}시 {now.minute}분 {now.second}초")

#LAB 7-2-1

import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
xMas = dt.datetime(2026, 12, 25)
time_gap = xMas - dt.datetime.now()
print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format(time_gap.days,time_gap.seconds // 3600))

#LAB 7-2-2
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
newyear = dt.datetime(2036, 1, 1)
time_gap = newyear - dt.datetime.now()
print('2036년 새해까지는 {}일 {}시간 남았습니다.'.format(time_gap.days,time_gap.seconds // 3600))

#LAB 7-2-3
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
birthday = dt.datetime(2026, 4, 24)
time_gap = birthday - dt.datetime.now()
print('2026년 생일까지는 {}일 {}시간 남았습니다.'.format(time_gap.days,time_gap.seconds // 3600))

#LAB 7-3-1
import datetime as dt
print('오늘 =', dt.datetime.now())
hundred = dt.timedelta(days = 1000)
plus1000day = dt.datetime.now() + hundred
print('1000일 후 =', plus1000day)

#LAB 7-3-2
import datetime as dt
today = dt.date.today()
couple_day = int(input('처음으로 사귄 연도와 월, 일을 입력하시오 :'))
#입력받은 날로부터 100일?

#LAB 7-4-1
import math
for i in range(2, 11):
    result = math.pow(4, i)
    print(f'4** {i} = {result}')

#LAB 7-4-2
import math
for degree in range(0, 181, 10):
    radian = math.radians(degree)
    print(f'{degree} degree = {radian} radian')

#LAB 7-4-2
import math
for degree in range(0, 181, 10):
    radian = math.radians(degree)
    sin = math.sin(radian)
    print(f'sin{degree}) = {sin}')

#LAB 7-5-1
import random

print("0에서 100 이하의 정수 중에서 5의 배수")

num1 = random.randrange(0, 101, 5)
num2 = random.randrange(0, 101, 5)
num3 = random.randrange(0, 101, 5)

#LAB 7-5-2
import random
random_list = random.sample(range(1, 11), 3)
print(f'1에서 10 사이의 임의의 정수 : {random_list}')

print([num1, num2, num3])

#LAB 8-1
try:
    a = [10, 20, 30]
    print(a[3])
except Exception as e:
    print(e)

try:
    n = int('20%')
except Exception as e:
    print(e)

try:
    a = 100 + '200'
except Exception as e:
    print(e)

#LAB 8-2
try:
    result = 10 * (30 / 0)
except ZeroDivisionError:
    print("오류: 0으로 나눌 수 없습니다.")

try:
    x = int(input('정수 x를 입력하세요: '))
except ValueError:
    print("오류: 유효한 정수를 입력해야 합니다.")

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
except FileNotFoundError:
    print("오류: 'myfile.txt' 파일을 찾을 수 없습니다.")


#LAB 8-3-1
try:
    print(10 * (30 / 0))
    
except:
    print("0으로 나눌 수 없습니다!!")

#LAB 8-3-2
try:
    x = int(input('정수 x를 입력하세요: '))
    print("정수:", x)

except:
    print("오류: 정수만 입력해야 합니다!")

#LAB 8-3-2
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    print(s)

except:
    print("오류: 'myfile.txt' 파일을 찾을 수 없어요!!")
