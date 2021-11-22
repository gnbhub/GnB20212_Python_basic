# 예외처리, 지역변수/전역변수, 클래스와 객체
## Optional Parameters
지난 시간에 함수 선언에서 괄호 사이에 parameter를 작성할 수 있다고 했다
<br>ex
```python
def func(x):
    print(x)
func("hello")
```
```python
>>>
hello
```
```python
def func(x, text):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')
func('Tim','1')
```
```python
>>>
Tim
Text is 1
```
이번에는 매개변수가 2개인데, 두번째 매개변수가 '1'이라서 If의 조건문도 실행되는 것을 볼 수 있다.
<br>함수를 여러번 사용하는데 똑같은 매개변수를 반복적으로 사용하기는 번거로울 것이다.
<br>만약 자주 사용되는 매개변수 값이 존재한다면 그것을 기본값(default value)으로 설정해준다면 더욱 유용하게 사용할 수 있다.
```python
def func(x, text='2'):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')
        print(text)
func('Tim')
```
매개변수를 선언 할 때, `text='2'`라고 되어 있다. text가 선언되어야 할 자리에 아무것도 없다면 기본값으로 '2'가 대입 될 것이다.
따라서 func('Tim')을 호출하면
```python
>>>
Tim
Text is not 1
2
```
print(text)를 통해 2가 출력됨을 확인할 수 있다.
```python
func('Tim','67')
```
text자리에 '67'을 대입해주면
```python
>>>
Tim
Text is not 1
67
```
다음과 같이 출력됨을 이해할 수 있다.
```python
def func(x=3, text='2'):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')
        print(text)
func()
```
이번에는 x도 default value를 설정해주고 `func()`에 아무 인수도 주지 않고 호출하면
```python
>>>
3
Text is not 1
2
```
x의 기본값 3이 출력됨을 확인할 수 있다. 매개변수 2개 모두 기본값을 가지는데, 왼쪽부터 첫 번째 매개변수를 선언하지 않고 두번째 매개변수만 선언할 수는 없다. 다시 말해서 `func()`함수를 호출할 때 매개변수가 존재한다면 왼쪽부터 순서대로 대입될 것이다.

## 예외처리
자바를 공부했다면 try-catch 구문을 보았을 것이다. python은 try-catch대신 try-except인데 알아보도록 하겠다.
<br> 동작을 하거나 어떤것을 시도할텐데 제대로 구동되는지 아닌지 모른다. 어떤 입력을 주는지 어떤 동작을 하는지 따라서 정상 동작할 수도 있고 동작하지 못할 수도 있다.
```python
text= input('Username: ')
number = int(text)
print(number)
```
무언가를 입력받는다고 가정하자. 이를 int형으로 바꾸어서 출력하도록 작성하였는데, 숫자가 아니라 문자를 입력했을때 오류가 나는 것을 볼 수 있다.
```python
try:
    number = int(text)
    print(number)
#시도한다는 뜻
except:
    print('Invalid Username')
```
`try:` 블록을 만들어서 안쪽에 선언해주면 블록 안의 코드를 실행하고 만약 실행 중 오류가 난다면 이후 문장은 수행하지 않고 `except:`블록 안의 문장을 수행한다.
<br>그래서 이번에 문자를 입력했을때 오류는 나지 않고'Invalid Username'이 출력되는것을 확인할 수 있다. 만약 숫자가 들어간다면 정상 동작할것이다.
이것이 간단한 예외처리이고 만약 예외처리 개념이 더 궁금하다면 이쪽을 참조하면 좋을 것 같다.
<br>자바스터디 예외처리part: https://github.com/gnbhub/gnb20211JavaStudy_2/tree/master/week7 

## Global and Local variables(전역변수와 지역변수)
`Global`은 말 그대로 파일 내의 모든 곳을 의미하고<br>
`Local`은 특정 블록이나 클래스 내부 만을 가리킨다.
<br>변수의 선언 위치에 따라서 전역변수 지역변수로 나뉘게 된다.
```python
var = 9

def func(x):
    newVar = 7
    if x == 5:
        return newVar

print(newVar)
```
```python
>>>
NameError: name 'newVar' is not defined
```
newVar은 함수 func안에 선언되었기 때문에 오직 함수 안에서만 접근할 수 있고 바꿀 수 있고 사용할 수 있다.
```
```python
def otherFunc():
    newVar = 5
    print(newVar)

newVar = 23
otherFunc()
```
```python
>>>
5
```
여기서 newVar = 23이라 선언했지만 이것은 otehrFunc함수 내의 newVar의 값을 바꿔준 것이 아니라 전역변수 newVar를 새로 설정해주게 된 것이다.
<br>따라서 otherFunc()함수를 호출해서 사용하면 출력값은 5가 나온다. 왜냐하면 otherFunc()가 사용하는 newVar는 지역변수이고 이는 5에서 변경된 적이 없다.
<br>이처럼 모듈이나 블록 바깥에서 지역변수를 접근하고 수정하고 사용하는 것은 불가능하지만, 반대로 모듈이나 블록 내에서 전역 변수는 접근하고 수정하고 참조할 수 있다.
<br>하지만 이것은 코딩 측면에서 바람직하지 못한게 모듈러 프로그래밍에 대해 간단히 학습했었는데, 만약 블록이나 함수 내에서 파일의 전역변수를 언급한다면 다른 파일에서는 제대로 변수를 가리키지 못하게 된다. 따라서 아래에서 전역 변수를 변경하는 방법을 배울텐데, 코드를 작성할때는 유의하여야 한다.
```python
loop = True
def func():
    loop = 7
    print(loop )
func()
print(loop)
```
어떤 결과를 출력할까? 
```python
>>>
7
True
```
이해가 되나요? func()함수를 호출해서 print(loop)를 할 때에는 func()함수 내의 loop 지역변수를 참조할 것이고, 그냥 print(loop)를 하게 되면
전역 변수 loop를 참조 할 것이다. 따라서 결과가 7/True가 된다. 여기서는 함수에서 전역변수의 값을 바꾸지 못하는것을 확인할 수 있다.
<br>다음은 함수 내에서 전역 변수에 접근하는 방법을 알아보자.
<br>만약 전역변수의 값을 바꾸고 싶다면 루프 내에서 global이라는 키워드를 사용해서 전역변수를 루프 내에 선언하고 그 값을 다음과 같이 바꿔줘야한다.
```python
loop = True
def func():
    global loop
    loop = 8
    print(loop )
func()
print(loop)
```
전역 변수 `loop = True`였는데 함수 내에서 `global`키워드를 사용해서 전역 변수 loop를 호출하였고 이 값을 8로 바꾸어주었다.
<br>func()를 통해 print(loop)를 실행하면 당연히 8이 출력될 것이고 print(loop)또한 8을 출력한다. 왜냐하면 전역변수 loop의 값을 바꿔주었기 때문이다.
```python
>>>
8
8
```

## Classes and Objects
### Objects
파이썬에서 보는 대부분은 Object(객체)이다. 우리가 어떤 변수를 선언하고 특정 자료형의 값을 넣어주는것이 하나의 객체를 만드는 것이다.
각각의 Object는 특정 속성을 가진다. ex)String형 변수와 int형 변수를 더할수는 없다.
```python
x = 'abc'
y = 23
print(type(x))
print(type(y))
```
```python
>>>
<class 'str'>
<class 'int'>
```
```python
print(y.count('1'))
```
```python
>>>
AttributeError: 'int' object has no attribute 'count'
```
String형 변수와 int형 변수를 더할수는 없다.
```python
print(x.count('1'))
```
```python
>>>
0
```
count는 String클래스에 내장된 method이고 우리는 String형 object에 대해 `.`을 사용해서 이용할 수 있다.
<br>각각의 자료형은 대게 클래스로 구성되어 있다. 각각의 자료형은 특정한 속성(메소드)를 가진다.
```python

boo = True
print(boo.count('1'))
```
```python
>>>
AttributeError: 'bool' object has no attribute 'count'
```
```python
def func():
    print('hello')

func()
```
함수와 메소드는 다르다. 함수는 `.`없이 함수만 호출해서 쓰지만, 메소드는 `object이름.메소드` 형태로 사용한다.
### Class
클래스는 간단히 말해 필드와 속성으로 정의하는 자료형이다. 즉, 변수와 함수로써 특수한 자료형을 만들수 있도록 하는것이다.
```python
class number():
    def __init__(self, num): self는 꼭 있어야 한다. 단지 자기 자신을 가리키는 것.
        self.var = num
        
    def display(self, x):
        print(x)
```
number라는 클래스를 선언해보는 것인데 class 옆에는 클래스 이름을 작성한다.
<br> 그리고 `def __init__(self, num):`생성자인데 이건 number형의 변수를 생성할때, 자동으로 호출하는 함수다.
self는 자기 자신을 가리키는 것으로 함수 선언시에 있어야 하는 parameter이다. 여기서 생성자는 num을 입력받아서 number라는 클래스의 변수 var에 대입해준다.
<br>`self.var`하게 되면 자기 자신의 var라는 변수를 가리킨다.
<br>아래에는 display라는 함수가 작성되어있는데 이 함수 또한 self라는 매개변수가 들어가있는 것을 볼 수 있다. 여기서는 x를 입력받아
출력하도록 한다.
```python
y = 23
y.display(21) #y는 int형 자료형
```
y는 int형 자료형이다. int클래스에는 display라는 함수가 없으므로 y.display()는 동작하지 않는다.
```python
>>>
AttributeError: 'int' object has no attribute 'display'
```
```python
A = number(23) #number클래스의 자료형으로 변수 선언
print(A)
```
여기서는 number클래스의 자료형으로 변수를 선언하였다. 이것을 number 클래스의 인스턴스 또는 객체가 생성되었다고 한다.
<br>number(23)을 해줌으로써 num에 23이 들어가고 이는 var에 대입된다. 즉, A가 가지는 var라는 변수의 값은 23이다.
```python
<__main__.number object at 0x0000012C0E871B20>
```
객체를 출력하면 어떤자료형인지, 메모리 어떤주소에 저장되어있는지 표시된다. 이 부분은 가볍게 보고 지나가면 된다.
```python
A.display(A.var)
```
A는 number클래스의 자료형이므로 display라는 함수를 호출할 수 있는데, A 자료형의 var변수가 괄호 속에 있다.
함수는 이를 매개변수로 전달받아 var의 값인 23을 출력한다.
<br>클래스에 대해선 쓸게 많지만 추후에도 계속 나올것이기 때문에 일단 간단히 쓰겠습니다. 클래스 구조를 처음본다면 가볍게만 보세요.


