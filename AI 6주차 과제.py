#LAB 6-1 1
capital_dic = { 'Korea':'Seoul', 'China':'Beiging', 'USA':'Washington DC'}
print(capital_dic['Korea'])
print(capital_dic['China'])
print(capital_dic['USA'])

#LAB 6-1 2
fruits_dic = {'apple': 5000, 'banana': 4000, 'grape': 5300, 'melon': 6500}
for fruit in fruits_dic:
    print('{}의 가격은 {}원입니다.'.format(fruit, fruits_dic[fruit]))

#LAB 6-2 1
person = {'이름': '홍길동', '나이': 26, '몸무게': 82}
person['특기'] = '분신술'
print(person)

#LAB 6-2 2
person = {'이름': '홍길동', '나이': 26, '몸무게': 82}
person['아버지'] = '홍판서'
print(person)

#LAB 6-2 3
person = {'이름': '홍길동', '나이': 26, '몸무게': 82}
del person['나이']
print(person)

#LAB 6-3
capital_dic = {'Korea': 'Seoul', 'China': 'Beijing', 'USA': 'Washington DC'}
print('Korea' in capital_dic)
print('China' in capital_dic)
print('Indonesia' in capital_dic)
print('Beijing' in capital_dic)

#LAB 6-4
# 1
fruits_dic = {'apple': 6000, 'melon': 3000, 'banana': 5000, 'orange': 7000}
print("1번:", fruits_dic)

# 2
print("2번:", fruits_dic.keys())

# 3
print("3번:", fruits_dic.values())

# 4
fruits_dic.pop('apple')
print("4번:", fruits_dic)

# 5
fruits_dic.clear()
print("5번:", fruits_dic)

#LAB 6-5
# 1
fruits_dic = {'apple': 6000, 'melon': 3000, 'banana': 5000, 'orange': 4000}
print(list(fruits_dic.keys()))

# 2
print(list(fruits_dic.values()))

# 3
count = len(fruits_dic)
print('fruits_dic 딕셔너리의 항목의 개수 : {}'.format(count))

# 4
if 'apple' in fruits_dic:
    print('apple is in fruits_dic.')
else:
    print('apple is not in fruits_dic.')

if 'mango' in fruits_dic:
    print('mango is in fruits_dic.')
else:
    print('mango is not in fruits_dic.')

#LAB 6-6 1
the_day = (1919, 3, 1)
year, month, day = the_day
print('{}년 {}월 {}일은 삼일절입니다.'.format(year, month, day))

#LAB 6-6 2
list = [10, 20, 30]
tuple = tuple(list)

c, b, a = tuple

print('a =', a)
print('b =', b)
print('c =', c)

#LAB 6-7
del list
del tuple #리스트랑 튜플 중복이라서 일단 del 넣어서 꼬인 변수 삭제?!?!?!?!
person = ('홍길동', 2020003, 179)
person_list = list(person)
person_list[1] = 2020003
person = tuple(person_list)
print('학번 변동 후 person = {}'.format(person))

#LAB 6-8 1
def square(x, y):
    return x**2, y**2
x = 10
y = 20
x_sq, y_sq = square(x, y)
print('{} 제곱 = {}, {} 제곱 = {}'.format(x, x_sq, y, y_sq))

#LAB 6-8 2
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

result_tuple = tuple1 + tuple2

print("2번:", result_tuple)

#LAB 6-8 3
print('Hello ' * 3)
print(('Hello ',) * 3)

#LAB 6-9 1
lst = ['apple', 'mango', 'banana']
s1 = set(lst)
print('s1 =', s1)

#LAB 6-9 2
greet = 'Good afternoon'
s2 = set(greet)
print('s2 =', s2)

#LAB 6-10
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60, 70}

print("1) s1 | s2 :", s1 | s2)
print("2) s1 & s2 :", s1 & s2)
print("3) s1 - s2 :", s1 - s2)
print("4) s1 ^ s2 :", s1 ^ s2)
print("5) s1.issubset(s2) :", s1.issubset(s2))
print("6) s1.issuperset(s2) :", s1.issuperset(s2))
print("7) s1.isdisjoint(s2) :", s1.isdisjoint(s2))

#LAB 6-11
def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)}
    return res

A = {1, 2}
B = {'A', 'B', 'C'}

print("1) A x B =", product_set(A, B))
print("2) B x A =", product_set(B, A))
print("3) A x A =", product_set(A, A))
print("4) B x B =", product_set(B, B))

#LAB 6-12 << 어려워요.......................
def tuple_sum(tup) : 
    if isinstance(tup, int) : 
        return tup
    else:
        accum = 0
        for element in tup : 
            accum += tuple_sum(element) 
        return accum

def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)} 
    return res

def exp(input_set, exponent) : 
    res = input_set
    for _ in range(exponent-1) : 
        res = product_set(res, input_set)
    return res

dice = {1, 2, 3, 4, 5, 6}
cases = exp(dice, 3)  

total_cases = len(cases)
print('주사위를 세 번 던져 발생할 수 있는 사건은 {} 가지 경우가 존재합니다.\n'.format(total_cases))

count_10_over = 0
for c in cases:
    if tuple_sum(c) >= 10:
        count_10_over += 1

print('주사위를 세 번 던져 나온 눈의 합이 10 이상인 경우는 {} 가지입니다.\n'.format(count_10_over))

def prob_over(x):
    count_x_over = 0
    for c in cases:
        if tuple_sum(c) >= x:
            count_x_over += 1
            
    probability = (count_x_over / total_cases) * 100
    
    print('눈의 합으로 {:2} 이상을 얻을 확률 {:6.2f}%'.format(x, probability))

for i in range(3, 19):
    prob_over(i)
