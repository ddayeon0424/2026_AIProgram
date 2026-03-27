Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
score = [87, 84, 95, 67, 88, 94, 63]
print(score)
[87, 84, 95, 67, 88, 94, 63]
>>> print(type(score))
<class 'list'>
>>> score = [87, 84, 95, 67, 88, 94, 63]
>>> for i in score:
...     print(i)
... 
...     
87
84
95
67
88
94
63
>>> score = [87, 84, 95, 67, 88, 94, 63]
>>> names = ["영호", "순자", "영식", "순희"]
>>> for i in names:
...     print(i)
... 
...     
영호
순자
영식
순희
>>> score = [87, 84, 95, 67, 88, 94, 63]
... names = ["영호", "순자", "영식", "순희", score]
SyntaxError: multiple statements found while compiling a single statement
>>> score = [87, 84, 95, 67, 88, 94, 63]
>>> names = ["영호", "순자", "영식", "순희", score]
>>> adressbook=[["영호", 25, "010-3825-0000"], ["철수", 30, "010-3325-0000"]]
>>> for i in adressbook:
...     print(i)
... 
...     
['영호', 25, '010-3825-0000']
['철수', 30, '010-3325-0000']
>>> ri = list(range(5))
>>> print(ri)
[0, 1, 2, 3, 4]
