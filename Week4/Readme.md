# 4주차 파일 입출력 및 모듈러 프로그래밍
## Text File Reading
우선 불러오고자 하는 txt파일의 경로는 .py파일과 같은 곳에 있어야 한다.
<br> 만약 같은 곳에 있지 않다면 상대 경로가 아니라 절대 경로를 이용하여 불러오고자 하는 파일을 참조해야 할 것이다.
```python
file = open('file.txt', 'r')
```
r을 써 주지 않거나 w를 써주거나 혹은 아무것도 작성하지 않고 ('file.txt')처럼 한다면 읽기 모드가 아니라 쓰기 모드가 되어 원래의 파일의 내용은 모두 지워지므로 꼭 'r'을 써주어야 한다.
<br> close()는 파일을 불러 온 후 open메소드가 정상적으로 종료될수 있도록 한다.
만약 선언해주지 않
```python
f = file.readlines()
print(f)
```
```python
>>>
['hello \n', 'python\n', 'learning\n', 'easy']
```
f = file.readlines()를 통해 파일을 줄단위로 읽는다. <br>
그리고 f를 출력하면 파일 텍스트가 줄단위로 출력되는데, 마지막 문장을 제외한 나머지들에는 \n이 붙는것을 확인할 수 있다.<br> 왜냐하면 직접 \n을 입력한 것은 아니지만, 파일에서 엔터로 줄바꿈을 할 때 마다 \n이라는 확장 문자 **(escape chararcter)** 를 만들어 내기 때문이다.
<br> 이 확장문자는 텍스트편집기에서는 줄바꿈으로 인식해서 줄을 바꾸어서 표시하지만 python 파일 입력으로 읽게 되면 다음과 같이 존재함을 볼 수 있다.
<br><br>
\n을 출력하지 않고 원소를 출력하는 방법을 알아보자. 반복 루프를 이용하면 된다.
```python
f = file.readlines()

newList = []
for line in f:
 newList.append(line[:-1])
print(newList)
 ```
 ```python
 >>>
 ['hello ', 'python', 'learning', 'eas']
 ```
 인덱스에서 -1은 마지막 원소를 가리키는데, [:-1]을 하게 되면 시작부터 마지막 앞까지의 원소를 슬라이싱 하게 된다. 따라서 마지막 글자를 제외한 String들이 newList의 원소가 된다. 하지만 이것이 마지막 문장까지도 적용되어 easy가 아나라 eas가 출력되는 것을 볼 수 있다.
 <br>이것을 해결하여 보면
 ```python
 newList = []
for line in f:
    if(line[-1]=='\n'):
        newList.append(line[:-1])
    else:
        newList.append(line)
print(newList)
```
```python
['hello', 'python', 'learning', 'easy']
```
반복 루프 안에 조건문을 첨가하여 줄 단위로 읽은 String이 \n으로 끝날때는 \n을 제하고 newList에 추가하고, 그렇지 않은 경우엔 그대로 newList에 추가한다. 그러면 텍스트 편집기로보는, 즉 우리가 평상시 보는 것과 같은 형식으로 출력됨을 볼 수 있다.
```python
newList = []
for line in f:
     newList.append(line.strip())

print(newList)
```
```python
>>>
['hello', 'python', 'learning', 'easy']
```
저번 시간에 배웠던 strip()를 이용하여 간단하게 작성할 수도 있다. line.strip()을 통해 \n이 있다면 \n이 제거되고 추가되고, 없다면 그대로 추가된다.
<br>
- `file.close()
이렇게 되면 `file = open('file.txt', 'r')`을 통해 선언된 파일 객체를 종료하는것을 말한다. 파일 객체는 사용하고 난 후 종료해주는 것이 바람직하다. 그렇지 않으면 불필요한 자원이 계속 소모되거나,
정상적인 종료및 저장이 이루어지지 않을 수 있다.
## Text File Writing
```python
file = open('file2.txt', 'w')

file.write('python')
file.close()
```
만약 파일이 존재하지 않는다면 file2.txt가 py파일이 위치하는곳에 생성된 것을 볼 수 있고, 만약 기존에 존재했다면 그 전의 내용은 지워지고 새롭게'python' 이 작성될 것이다.
```python
file.write('python')
file.write('i am learning how to write to a file')  
```
이렇게 작성하면 python바로 옆에 다음 문장이 위치하는것을 파일을 열어 확인할 수 있다.
<br>이것을 피하기 위해선 위에서 언급한 확장 문자\n을 통해 줄을 바꾸어 작성할 수 있다.
```python
file.write('python\n')
file.write('i am learning how to write to a file')  
```
줄을 바꾸어 작성된 것을 확인할 수 있다. file.close()는 file객체를 모두 사용하고 난 후 끝에 작성해주면 된다.

## String/List methods
### find
```python
string = 'hello'
print(string.find('l'))
```
`.find()` 메소드는 String이나 List에서 사용할 수 있는 메소드인데, 예문과 같이 작성하고 실행하면 2가 반환된다. 이것은 string에서 최초의 'l'이 몇번째 인덱스에 위치하는지 표시한다. 갯수를 나타내는 것이 아니다!
<br>예를 들어 'o'를 넣어보자.
```python
string = 'hello'
print(string.find('o'))
```
4가 출력되는 것을 볼 수 있는데, o의 인덱스가 4이기 때문이다.
```python
string = 'hello'
print(string.find('7'))
```
이번엔 '7'을 찾아보았는데 -1이 출력되는것을 볼 수 있다. 이것은 찾고자 하는 변수 안에 해당하는 변수가 없을때 -1이 출력되는것을 볼 수 있다.
<br>어떻게 사용할 수 있냐면 password를 입력받는데 공백이 포함되있는지 검사하거나 특정 문잘를 입력받지 않도록 하거나 혹은 특정 문자가 password안에 포함되도록 하는데 유용하게 사용될 수 있다.
### count
find가 인덱스를 찾는 메소드라면, count는 갯수를 찾는 메소드이다.
```python
string = 'hello'
print(string.count('l'))
```
여기서도 2를 출력하겠지만, 여기서 2는 'l'의 인덱스가 아니라 갯수이다!
```python
string = input("please type something")
if string.count('_') > 0:
    print('Not good!')
```
특정 문자를 입력받아서 '_'는 포함하지 않고 입력받도록 작성할 수 있다.

## Introduction to Modular Programming
파이썬은 모듈러 프로그래밍 언어이다. 이 말은, 동시에 여러개의 파일을 함께 사용해서 하나의 프로그램을 만들수 있다는 것이다.
<br>파이썬에는 우리가 사용할 수 있는 다양한 함수와 클래스를 포함하고 있는 모듈들을 사용할 수 있는데, import 라는 keyword를 사용하여 쓸 수 있다. 내장된 모듈은 당연히 import로 사용할 수 있고 또는 기본으로 설치되지 않은 모듈들도 설치하여 불러올 수 있다.
```python
import math
math.sqrt(2)
```
내장된 math 모듈을 불렀는데, 여기는 제곱근`.sqrt`와 같은 함수들이 있다.
```
import pygame
```
pygame 모듈은 파이썬으로 게임 개발을 하는데 이용하는 외장 모듈이다. 모듈에 어떤것이 있는지 일일이 알 필요는 없다. 필요한 함수가 있다면 검색해보고 해당 메소드를 포함하는 모듈을 불러와서 사용하면 되겠다.
```python
print(math.pi)
```
3.141592653589793가 출력되는것을 볼 수 있다. 파이가 상수로써 math 모듈 안에 내장되어 있다.
```python
print(math.degrees(math.pi))
```
파이를 math 모듈 안의 degrees메소드를 이용하여 출력해보면 180.0이 출력된다.
```python
print(math.radians(60))
```
math 모듈 안의 radians 메소드를 이용하여 60도를 라디안각으로 바꾸면
<br>1.0471975511965976 가 출력된다.

```python
import myModule
```
내장 모듈 중에 myModule는 없다. 프로그램은 py 파일이 위치한 곳에서 myModule이 있는지 찾는다.
<br>같은 디렉토리안에 myModule을 작성해보자. 첨부된 파일을 다운로드하여 같은 디렉토리에 위치시켜주거나 작성하면 된다.
```python
def myFunc(x):
    return x + 5
def anotherFunc(x):
    return x//5
```
myModule안에 간단하게 myfunc를 정의하면 우리는 myModule을 import하여 myModule안의 myfunc를 사용할 수 있다.
```python
import myModule
print(myModule.myFunc(6))
print(myModule.anotherFunc(365000))
```
메인 스크립트에서 다음과 같이 myModule안에 정의된 함수를 불러와서 사용할 수 있다.
<br>추가적으로 다른 파이썬 내장 모듈들에 대해 알고싶다면 python 공식 홈페이지에 방문하면 찾아볼 수 있다.
