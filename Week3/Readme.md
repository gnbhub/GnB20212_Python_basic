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
## slicing
앞에서 인덱스틀 통해서 특정 순서에 있는 원소를 가리킬 수 있는것을 배웠는데 
