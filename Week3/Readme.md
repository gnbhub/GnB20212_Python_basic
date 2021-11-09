# 3주차 향상된 반복문, String, Slicing, Function
## 향상된 반복문
다른 언어들과 마찬가지로 변수를 선언하고 in range등을 통해서 반복 루프를 만들 수도 있지만,
<br>Python은 자료형에 구애받지 않고 리스트를 만들 수 있고 range 대신 리스트를 이용할 수 있다.
```python
fruits = ['apples','pears','strawberrys',3, 8, 90]
for fruit in fruits:
    print(fruit)
```
```python
>>>
apples
pears
strawberrys
3
8
90
```
변수 이름을 fruit로 하고 fruits 리스트를 이용하여 반복루프를 구성하였다. 반복할때마다 리스트의 원소들이 반환되는것을 알 수 있다.
```python
for fruit in fruits:
    if fruit == 'pears':
        print(fruit)
    else:
        print('not pears')
```
```python
>>>
not pears
pears
not pears
not pears
not pears
not pears
```
반복 루프에 조건문을 걸어주면 특정 원소를 찾을 수도 있다.
```python
for x in range(0,6):
    if fruits[x] == 'pears':
        print(fruits[x])
    else:
        print('not pears')
```
물론 range를 이용해서도 똑같은 동작을 하는 코드를 작성할 수 있다. 직접 변수를 반복문 안에서 사용하거나 range로 index를 이용하여 간접적으로 사용하거나 편한 방법으로 사용하면 되겠다.

## String 메소드
 - `.strip()` : 글자 앞의 모든 공백을 제거한다.
```python
text = "     abc"
print(text)
print(text.strip())
```
```python
>>>
     abc
abc
```
공백도 문자이므로 출력하게되면 그대로 출력하지만, strip()을 붙이면 글자 앞까지의 공백은 제거된다.
 - `len()` : String의 길이를 반환한다.
```python
text = "a b c"
print(len(text))
```
```python
>>>
5
```
공백도 하나의 글자로 카운트된다.
 - `.lower()` : 모든 텍스트를 소문자로 변환한다.
 - `.upper()` : 모든 텍스트를 대문자로 변환한다.
```python
text = "I want Some Rest"
print(text.lower())
print(text.upper())
```
```python
>>>
i want some rest
I WANT SOME REST
```
- `.split()` : 괄호 안의 문자를 기준으로 텍스트를 나누어 리스트로 반환한다.
```python
text = I_want_some_rest
print(text.split('_')
```
```python
>>>
['I', 'want', 'some', 'rest']
```
'_' 를 기준으로 하나의 원소가 되어 리스트형으로 반환됨을 알 수 있다.
<br>만약 () 사이에 아무것도 없다면 공백을 기준으로 스플릿한다.
## Slicing
앞에서 인덱스틀 통해서 특정 순서에 있는 원소를 가리킬 수 있는것을 배웠는데 리스트나 String 자료형을 range처럼 여러 원소를 한꺼번에 가리킬 수 있다.
```python
fruits = ['apples', 'pear', 'strawberrys']
text = "Hello I like Python"

print(fruits[1])
print(text[11])
```
```python
>>>
pear    #fruits의 두번째 원소
e       #text의 12번째 원소 
```
print(text[start:stop:step])의 형태, range(start:stop:step)과 동일하다. 
```python
print(text[:])
```
[:]라면 전체를 지칭한다.
```python
>>>
Hello I like Python
```
```python
print(text[0:4])
```
index 0부터 4 앞까지의 원소 출력
```python
Hell
```
```python
print(text[2:])
```
index 2부터 끝까지 출력
```python
>>>
llo I like Python
```
```python
print(text[::2])
```
처음부터 끝까지 출력하지만 index 2씩 증가하면서 출력 즉, 짝수번째 인덱스만 출력
```python
>>>
HloIlk yhn
```
String에서 슬라이싱을 나열하였는데, 리스트도 똑같이 할 수 있다.
<br> 앞서 `.append`를 통해 리스트에 원소를 추가하는것을 배웠는데, 인덱싱을 통하여 append와 유사한 동작을 하도록 만들 수 있다.
```python
fruits[3:3] = 'added'
print(fruits)
```
```python
>>>
['apples', 'pear', 'strawberrys', 'a', 'd', 'd', 'e', 'd']
```
`fruits[n:n]`하게 되면 n번째 인덱스위치에 원하는 것을 추가할 수 있다. 다만, char형태로만 들어가서 String을 대입하면 한 글자씩 끊어져서 입력이 된다.

## Function(함수)
수학적인 함수와 그 의미가 유사하다. 인수(argument)를 입력해주어 특정한 결과를 반환하도록 하는 것이다.
<br> 특정 동작을 여러번 반복할때 유용하게 사용할 수 있다.
```python
def addTwo(x):      #함수 선언. def 함수이름(매개변수)
    return x+2      #함수 내용

newNumber = addTwo(7)
print(newNumber)
```
x는 parameter, 매개변수이다. 매개변수는 하나일수도, 여러개일 수도, 없을수도 있다. 함수 내에서 필요한 매개변수만큼 만들면 된다.
<br>위에서는 def를 통하여 함수를 선언한다. 그리고 입력받을 매개변수를 정하고 동작을 선언해주면 된다.
<br>함수 선언 자체로는 동작이 없고 함수를 호출해서 사용을 함으로써 동작한다.
<br>아래에서 addTwo(7)을 통해서 x에 7이 대입되고 2를 더하여 9를 return한다. 여기서 (7)은 argument, 인수라고 한다.
```python
def accel(mass, force):
    a = force/mass
    return a
```
다음과 같이 매개변수를 두개 입력받도록 작성할 수 있다. 가속도 a = 힘F 나누기 질량m m과 f를 입력받아서 a 반환.
```python
def doSomething():
    print('hi')
```
또는 다음과 같이 매개변수를 입력받지않고 작성할 수도 있다.

## Example
따라해봤으면 좋겠어서 게시합니다.
- 이름, 비밀번호를 체크하여 처리하는 프로그램
- 비밀번호는 숫자나 문자 둘다 사용하여야 하며, 동일한 문자나 숫자는 연속으로 올 수 없다.
```python
name = input("이름을 입력하세요 : ")
name.strip()    #글자 앞의 공백 제거
name = name.replace(" ","") #공백을 모두 없앤다.

passwd = input("비밀 번호를 입력하세요 : ")
for count in range(0, len(passwd)-1):
    if passwd[count] == passwd[count+1]:
        print("연속된 문자가 존재합니다.")
        break;
    else:
        print("정상 처리 되었습니다.")
        print("이름 : %s, 비밀번호 : %s" %(name, passwd)) ##형식있는 출력방식. %s는 string을 받겠다는 것이고"뒤에 어떤것을 참조하는지 기록.
```
replace 메소드는 괄호안에서 , 앞쪽의 내용을 , 뒤쪽의 내용으로 바꾼다. 여기서는 공백을 아무것도 없도록 만들어준다.

## Quiz
- 입력된 문자열에서 공백을 구분하여 단어로 출력하기 함수 형태로 작성!
<br>ex
```python
문자열을 입력 : hello i am python
hello
i
am
python
```
        
