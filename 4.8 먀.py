person = {'이름' : '홍길동', '나이' : 26, '몸무게' : 82 }
person['국적'] = '대한민국'

for key in person:
    print('{} : {}'.format(key, person[key]))
