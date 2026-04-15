Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
============= RESTART: C:/Users/an/Desktop/2026_AIProgram/4.8 먀.py =============
{'이름': '홍길동', '나이': 26, '몸무게': 82, '국적': '대한민국'}
>>> person = {'이름': '홍길동', '나이': 26, '몸무게': 82}
>>> len(person)
3
>>> '이름' in person
True
>>> 
============= RESTART: C:/Users/an/Desktop/2026_AIProgram/4.8 먀.py =============
Traceback (most recent call last):
  File "C:/Users/an/Desktop/2026_AIProgram/4.8 먀.py", line 4, in <module>
    print(person.key())
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> 
============= RESTART: C:/Users/an/Desktop/2026_AIProgram/4.8 먀.py =============
Traceback (most recent call last):
  File "C:/Users/an/Desktop/2026_AIProgram/4.8 먀.py", line 5, in <module>
    print('{}:{}'.format(key.person[key]))
AttributeError: 'str' object has no attribute 'person'
>>> 
============= RESTART: C:/Users/an/Desktop/2026_AIProgram/4.8 먀.py =============
이름 : 홍길동
나이 : 26
몸무게 : 82
국적 : 대한민국
