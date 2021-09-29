# 1주차 자료형, 연산자, 조건, 조건문
## 자료형(Datatypes)
다른프로그램과 유사하게 정수형, 문자열, 부울타입, 실수형 등이 있다. 다른점은 변수를 선언할때 모두 참조형으로 선언한다는 것이다. (: 포인터를 생각하면 될 듯 하다.)
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

## 연산자(Operators)
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
<br><br>매력적인 점은 Python에서 변수를 선언할 때 자료형을 선언하지 않아도 된다고 했다. 즉, 연산할 때도 casting이 필요하지 않다는 것이다.
<br> 더 큰 자료형으로 알아서 casting된다.
```python
num1 = 3.5
num2 = 2
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
```

### input?
`변수이름 = input()` 하게 되면 입력받은 값을 변수에 지정할 수 있다. 매우 간편하다.<br>
'변수이름 = input(내용)'하게 되면 내용을 출력하고 값을 입력받을 수 있다.
<br> **입력받은 값은 String type으로 저장됨**
```python
print('Pick a number: ')
num1 = input()
print("Pick another number: ")
num2 = input()
SUM = num1 + num2
print(SUM)
```
## 조건(Conditon)
Operatior들이 산술연산을 하는데 사용되는것이라면 여기 있는 연산자들은 참/거짓 판별을 위한 연산자들이다.
<br>연산의 결과가 참/거짓 형태의 부울(bool)타입으로 반환된다.
```python
x=4
print(x == 4) # 우변과 좌변이 같은 데이터인지 확인
print(x != 4) # 우변과 좌변이 같지 않은 데이터인지 확인
print(x > 3)
print(x < 3)
print('hello' != 'Hello') # 대소문자를 구별하므로 True가 반환됨을 확인할 수 있다.
```

## 조건문 If, elif, else
조건에 따라 동작을 제어할 수 있는 도구이다. 조건이 True면 동작한다.
```python
age = input('Input your age: ')
if int(age) >= 16: # String type으로 입력받으므로 정수형으로 casting하여 비교한다.
    print('hey youre older than 16')
else : # if문의 조건이 False인 경우 동작
    print('hey youre younger than 16')
```
```python
height = input()

if int(height) < 1:
    print('you cannot right, under 1m')
elif int(height) > 2:
    print('you cannot ride, over 2m')
elif int(height) == 5: # 죽은 문장 : 앞선 조건에서 height가 2 이상인 경우를 제한하였으므로 이 문장은 실행 될 수 없다.
    print('wow youre tall)
else: #앞의 모든 if문과 elif문이 False인 경우 동작
    print('you can ride')
```
다른 프로그래밍 언어와 비슷하면서도 다른 점이 있다. if 다음으로 오는 조건문은 elif라 쓴다 else if는 동작하지 않는다. elif문은 if와 else사이 얼마든지 작성하여도 좋다. 

#### 참조 : tutorial 1 ~ tutorial 4

## Question
다음 글자들의 dataype?<br>
print(type(대상) 하여서 확인해보기
```python
'Hello'
123
3.22
True
'2'
"3"
```

## Q2
0-63 사이 정수를 입력받아서 반복문을 사용하지 않고 2진수로 출력하기 ex 50 입력 -> 110010
<br>0-63 이외의 입력에 대한 고려는 생략해도 좋음
