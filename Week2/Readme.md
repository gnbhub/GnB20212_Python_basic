# 2주차 다중 조건, 중첩 if문, 반복문, 배열, 튜플
## 다중 조건
앞서 if문 안에 condition을 걸어 동작을 제한할 수 있다. and, or, not 등을 이용하여 여러 조건을 걸 수 있다.
```python
X = 2
y = 3

if x == y and x + y == 5 : # x와 y가 같지 않으므로 거짓
    print('ran')
if y == 3 and x + y == 5 : # y = 3이고 x+y = 5이므로 참
    print('ran')
```
 - condition이 and로 연결되면 연결된 조건 모두 참이여야 참이다.
```python
if y == x or x + y == 5 : # x+y = 5 이므로 참
    print('ran')
else :
    print( ':(')
```
 - 조건문이 or로 연결되면 조건 중 하나만 참이면 참이다. 연결된 조건 모두 거짓이면 거짓이다.
```python
if not(x == y and x + y == 5) : # ( ) 안의 조건이 거짓이므로 참
    print('ran')
```
 - 부울법칙을 따르면 된다. ( ) 안의 논리 연산을 하고 결과에 부정을 취하면 된다.
## 중첩 if문
```python
if x == 2 : # x = 2인 경우 아래 문장 실행
    if y == 3:  # y = 3인 경우 실행
        print( 'x = 2, y = 3 ') # 이 문장이 실행되는 경우는 x = 2이고 y = 3인 경우 뿐이다.
    else :
        print( ' x =2, y != 3') # 이 문장이 실행되는 경우는 x = 2이고 y는 3이 아닌 경우이다.
else : # x가 2가 아닌 경우 실행
    print('x !=2')
```

## for 반복문
for를 이용하여 반복 루프를 만들 수 있다.
```python
for x in range(0, 10, 1) : # start stop step
    print(x)
```
지정한 변수에 start부터 시작해서 step만큼 증가시켜 stop이 될 때 까지 반복하는데 stop이 될 때 문장이 실행되지 않고 루프가 끝난다.
<br> ex) step이 2라면 2씩 증가, 5라면 5씩 증가

## while 반복문
while을 이용하여 반복 루프를 만들 수 있다.
```python
while condition:
    do this
    break
```
condition이 참인 동안 계속 반복하는 루프이다. 만약 condition이 참이고 변하지 않는 조건이라면, 루프를 탈출하지 못한다.
<br> 따라서 루프가 진행되는동안 조건을 거짓으로 만들수 있도록 하거나 혹은 반복문 내에 조건문을 작성하여 특정한 상황에서 break가 될 수 있도록 한다.
<br> break는 루프를 탈출한다. for문에서도 활용할 수 있다.
```python
loop = True

while loop: # condition이 그냥 True와 같은 상태이다. 직접 True가 들어가도 된다.
    name = input('Insert something: ')
    if name == 'stop' : 
        break # loop = False
```
stop을 입력받으면 반복 루프를 종료하는데, break로 탈출해도 되고 loop = False를 선언하여 종료하여도 같다.
<br> for이 변수에 수를 대입하여 수적으로 반복하는 경향이라면, while 은 무한 반복에서 탈출하는 경향이다.

## 배열(List)
여러 개의 변수를 하나로 모아서 순서를 부여한 집합이다. 다른 프로그램에서는 같은 자료형의 데이터로만 배열을 만들 수 있지만, 파이썬에서는 서로 다른 자료형도 배열에 같이 담을 수 있고, 중복된 데이터도 가능하다.
```python
fruits = ['apple', 'pear', 3] # String과 int형이 같이 담길수 있다.

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
```
fruit만 print한다면 배열 전체를 가리키는 것이 되고 index를 통해서 배열의 원소 하나만을 가리킬수도 있다. index는 왼쪽 원소 0부터 시작한다.
```python
>>>
['apple', 'pear', 3]
apple
pear
3
```
```python
fruits.append('strawberry')
print(fruits)
```
```python
>>>
['apple', 'blueberry', 3, 'strawberry']
```
 - `배열이름.append()`를 통하여 배열 마지막에 ( )의 내용을 추가할 수 있다.
```python
fruits[1] = 'blueberry'
print(fruits)
```
fruit[1] = 'pear'였지만 직접 선언을 통해 'blueberry'로 바꾸어주었다.
```python
>>>
['apple', 'blueberry', 3, 'strawberry']
```
```python
fruits.pop()
```
```python
>>>
['apple', 'blueberry', 3]
```
 - `배열이름.pop()`는 배열의 마지막 원소가 삭제된다. ( ) 안에 인덱스가 있다면 인덱스에 해당하는 원소를 삭제한다.

## 튜플(tuple)
리스트와 유사한 형태를 가진 순차타입의 자료형이다. 주로 좌표, 색깔, 도형을 나타낼때 사용한다.<br>
배열과의 차이점은 요소의 변경이 불가능하다는 점이다. 새로운 요소를 추가, 삭제, 변경이 불가능하고 정렬 또한 불가능하다.
```python
position = (2, 3)
color = (255, 255, 255)
print(type(color))
```
```python
>>>
<class 'tuple'>
```
#### 참조 #5~#8
## Quiz
### 1. 1부터 사용자가 입력한 정수까지 합 구하기
1보다 작은 숫자 입력, 혹은 다른 데이터타입 입력에 대한 경우는 고려하지 않아도 좋음. 
<br>ex)
```python
숫자 입력 : 100
합 : 5050
```
### 2. 숫자를 입력받아 소수 판별하기
소수 : 1과 본인만을 약수로 가지는 수
<br>마찬가지로 양의 정수의 입력만 고려한다고 가정.
<br>ex)
```python
숫자를 입력하세요 ( 0: 종료) : 11
소수입니다.
숫자를 입력하세요 ( 0: 종료) : 8
소수가 아닙니다.
숫자를 입력하세요 ( 0: 종료) : 0
```
