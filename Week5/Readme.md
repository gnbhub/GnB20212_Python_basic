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
