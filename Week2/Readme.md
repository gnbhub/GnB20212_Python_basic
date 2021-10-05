# 다중 조건, 중첩 if문
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
