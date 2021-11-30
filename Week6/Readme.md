# Static함수, 클래스 함수, Map()함수
## Class Methods
클래스 함수는 클래스 변수와 클래스 내부 다른 함수들에 대해서만 접근 권한을 가지는 함수이다.
<br> 보통은 `cls`라는 parameter를 설정해주어 그 함수를 호출한 클래스를 가리킨다. 다른 글자로 설정해주어도 상관없다.
<br> 매개변수로 클래스를 가리키기 때문에 클래스 내부에 있는 모든 것들을 가리킬 수 있다. 선언할 때는 `@classmethod`를 붙여주고 선언해야 한다.

## Static Methods
static 함수는 클래스 내부의 어떤 것에도 접근할 수 없는 함수이다. 이 함수는 클래스 내부의 어떤 변수도 참조하거나 수정할 수 없고
클래스 내의 다른 함수도 호출할 수 없다. 이 static 함수는 클래스 내부에 존재하는 특별한 종류의 함수라고 생각하면 된다.
<br> 보통은 내부의 값과 관계 없이 매개변수를 전달받아서 전달받은 값으로 동작을 하도록 작성된다.
<br> 선언할 때는 `@staticmethod`를 붙여주고 선언해야 한다.

<br> `@staticmethod, @classmethod`는 decorator라 부른다.
<br>에문을 보면
```python
class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')

newPerson = person('tim', 18)
print(person.getPopulation()) #객체가 아니라 클래스 이름으로 참조하는것을 확인할 수 있다.
print(person.isAdult(17)) #객체가 아니라 클래스 이름으로 참조하는것을 확인할 수 있다.
```
예문에서 class함수는 getPopulation을 static함수는 isAdult가 선언되어있는데
객체 선언과 상관없이 `person.함수`를 통해 클래스 이름으로 호출하는 것을 볼 수 있다.<br>
`객체이름.함수`로도 호출할 수 있다.<br>
`print(person.getPopulation())`하게 되면 매개변수 cls에는 person 자기자신 클래스가 들어가게 되고 population값을 반환한다.
<br>
`print(person.isAdult(17))`하게 되면 17이 age에 대입되고 false를 반환한다. 즉, 클래스 내부의 값들과는 상관없이 입력 받은 값에 의해서만 결과를 출력하는것을 확인할 수 있다.

## Map()함수
map함수는 함수를 리스트에 적용할 때 유용하게 사용할 수 있는 함수이다.
```python
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x**x

newList = []
for x in li:
    newList.append(func(x))

print(newList)

print(list(map(func, li)))

print([func(x) for x in li if x%2==0])
```
```python
>>>
[1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000]
[1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000]
[4, 256, 46656, 16777216, 10000000000]
```
실행 결과를 보면 `print(newList)`와 `print(list(map(func, li)))`가 같은 결과를 출력하는것을 볼 수 있다.
<br>반복 루프를 사용해서 각 원소에 함수를 적용한 것을 배열에 집어넣고 출력한 것과 `list(map(함수, 배열))`을 사용해서 출력한 것과 결과가 같다.
<br>추가적으로 `print([func(x) for x in li if x%2==0])` 또한 비슷한 결과를 만들어 내는데 일종의 '조건제시법'으로 배열의 원소를 나열한 것이라고 생각하면 되겠다.

## Quiz
※피보나치 수열
<br>![image](https://user-images.githubusercontent.com/79446573/144033350-27b049ba-b2ec-418e-9e43-f1b894e7dc62.png)
<br> 다음과 같이 첫번째 두번째 항이 1이고 마지막 두개 항의 합이 다음 항의 수가 되는 수열이다. 
<br>
![image](https://user-images.githubusercontent.com/79446573/144033289-837a6c3a-d8c5-437e-aefe-682f62b7f661.png)
<br>예시처럼 3 이상의 정수를 입력받아 해당 숫자만큼 피보나치 수열을 리스트 형태로 출력하도록 작성하기
```python
num = input("3 이상의 정수 입력")
list = [ 1, 1]
## 코드 작성


```
