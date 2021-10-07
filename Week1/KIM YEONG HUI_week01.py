#Q1
print(type('Hello'))
print(type(123))
print(type(3.22))
print(type(True))
print(type('2'))
print(type("3"))
# Q2
pick = input("숫자를 선택하세요: ")
NUM = int(pick)
num1 = NUM%2
NUM = NUM//2
num2 = NUM%2
NUM = NUM//2
num3 = NUM%2
NUM = NUM//2
num4 = NUM%2
NUM = NUM//2
num5 = NUM%2
NUM = NUM//2
num6 = NUM%2
print(str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1))


