import datetime as dt

# 오늘 날짜 구하기
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))

# 크리스마스 날짜 설정 (2026년으로 수정)
xMas = dt.datetime(2026, 12, 25)

# 남은 시간 계산
time_gap = xMas - dt.datetime.now()

# 결과 출력
print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format(
    time_gap.days, time_gap.seconds // 3600))
