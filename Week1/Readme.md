# 1주차 자료형, 연산자
## 자료형
다른프로그램과 유사하게 정수형, 문자열, 부울타입, 실수형 등이 있다. 다른점은 변수를 선언할때 모두 참조형으로 선언한다는 것이다.
변수가 직접 어떠한 값을 가지는게 아니라 특정 값의 위치를 변수가 가지는 것이다.<br>
파이썬에서는 변수를 선언할때 그 변수가 어떤 자료형을 가지는지 선언하지 않아도 된다는 특징이 있다.

```python
int 1,4, 76, -5, 0
str "Tim", "Hello", '1', '34353'
bool True, False
float 0.32, 1.232
```
true는 안됨 

**문자열(String)** 은 " "나 ''로 선언하는데, 이 두개는 구분이 없고 보통은 포함관계를 나타내주기 위해 선택적으로 사용한다.
문자열은 한글자도 가능하다.

변수의 이름은 대소문자를 꼭 구별하여서 선언하여야 한다.
```python
name = 'Tim'
print(name)
name = 'Bob'
print(name)

age = 18
print(age)
```
- 파이썬에서 #은 주석을 나타낸다. 해당 줄은 읽지 않는다.

## 연산자
```python
num1 = 45
num2 = 3
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
```
 - / : 나누기
 - // : 몫
 - % : 나머지

### input?
`변수이름 = input()` 하게 되면 입력받은 값을 변수에 지정할 수 있다. 매우 간편하다.
```python
print('Pick a number: ')
num1 = input()
print("Pick another number: ")
num2 = input()
SUM = num1 + num2
print(SUM)
```

## Question
다음 글자들의 dataype?
```python
'Hello'
123
3.22
True
'2'
"3"
```

