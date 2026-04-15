Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a_list = [10, 20, 30, 40]
>>> 10 in a_list
True
>>> 50 in a_list
False
>>> 10 not in a_list
False
>>> 50 not in a_list
True
>>> #메소드 실습
>>> list1 = [20, 10, 40, 50, 30]
>>> list1.sort()
>>> list1
[10, 20, 30, 40, 50]
>>> list1.sort(reverse = True)
>>> list1
[50, 40, 30, 20, 10]
>>> list1 = [20, 10, 40, 50, 30]
>>> list2 = sorted(list1)
>>> print(list1)
[20, 10, 40, 50, 30]
>>> print(list2)
[10, 20, 30, 40, 50]
>>> list1 = [1, 2, 3, 4]
>>> list2 = [2, 3, 3, 4]
>>> list1 > list2
False
>>> list1 < list2
True
>>> #리스트 요소들을 하나하나 방문하며 10을 곱하는 기능
>>> list1 = [10,20, 30, 40, 50]
>>> i = 0
>>> for n in list1:
...     list1[i] = n * 10
...     i = i + 1
... 
...     
>>> print(list1)
[100, 200, 300, 400, 500]
