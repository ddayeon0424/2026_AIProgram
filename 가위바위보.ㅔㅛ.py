Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> selected = None
>>> while selected not in ['가위', '바위', '보']:
...     selected = input('가위, 바위, 보 중에서 선택하세요> ')
...     print('선택한 값은:', selected)
... 
...     
가위, 바위, 보 중에서 선택하세요> 가위
선택한 값은: 가위
