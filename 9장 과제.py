#9-1
(200).__sub__(100)
(200).__mul__(100)
(200).__truediv__(100)
[10, 20, 30, 40].pop()

#9-2
#객체 지향 프로그래밍:컴퓨터가 수행하는 작업을 객체들 사이의 상호작용으로 표현해서 프로그램을 실제 세상에 가깝게 모델링하는 기법
#절차적 프로그래밍:함수나 모듈을 만들어두고 이것들을 문제해결 순서에 맞게 호출하여 수행하는 방식
#그래픽 사용자 인터페이스:사용자가 컴퓨터와 상호작용할 때, 텍스트 대신 그래픽 요소를 사용하는 환경
#객체 지향 프로그래밍은 데이터와 기능을 하나로 묶은 객체간의 상호작용 중심이고, 절차적 프로그래밍 기법은 프로그램의 실행 순서와 절차 중심

#9-3
#클래스:프로그램 상에서 사용되는 속성과 행위를 모아놓은 집합체
#객체:클래스를 바탕으로 구현되는 실체
#인스턴스:클래스로부터 만들어지는 각각의 개별적인 객체
#클래스의 속성:객체가 가지는 데이터
#클래스의 동작:객체가 수행할 수 있는 기능

#9-4
class Dog:
    def bark(self):
        print("멍멍~~")
my_dog = Dog()
my_dog.bark()

#9-5
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("멍멍~~")

my_dog = Dog('Jindo')
my_dog.bark()

#9-6
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Dog(name = ' + self.name + ')'

my_dog = Dog('Jindo')

print('my_dog의 정보 :', my_dog)

#9-7
n=100
m=100
if n is m:
    print('n is m')

else:
    print('n is not m')

#9-8-1
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)

print('v1 * v2 =', v1 * v2)
print('v1 / v2 =', v1 / v2)

#9-8-2
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
v1_simple = Vector2D(10, 20)

print('-v1 =', -v1_simple)

#9-9 (어려움★)
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)

print('v1 > v2 =', v1 > v2)
print('v1 >= v2 =', v1 >= v2)
print('v1 < v2 =', v1 < v2)
print('v1 <= v2 =', v1 <= v2)

#9-10-1
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['width'])

#9-10-2
class Rect:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['_Rect__width'])
