#Q1

print(type('Hello'))
print(type(123))
print(type(3.22))
print(type(True))
print(type('2'))
print(type("3"))

#Q2

a = int(input('\n0~63 사이의 정수를 입력하세요 : '))

r0 = 0
if a % 2 == 0 :
    r0 = 0
    a = a / 2
elif a % 2 == 1 :
    r0 = 1
    a = a / 2 - 0.5

r1 = 0
if a % 2 == 0 :
    r1 = 0
    a = a / 2
elif a % 2 == 1 :
    r1 = 1
    a = a / 2 - 0.5

r2 = 0
if a % 2 == 0 :
    r2 = 0
    a = a / 2
elif a % 2 == 1 :
    r2 = 1
    a = a / 2 - 0.5

r3 = 0
if a % 2 == 0 :
    r3 = 0
    a = a / 2
elif a % 2 == 1 :
    r3 = 1
    a = a / 2 - 0.5

r4 = 0
if a % 2 == 0 :
    r4 = 0
    a = a / 2
elif a % 2 == 1 :
    r4 = 1
    a = a / 2 - 0.5

r5 = int(a % 2)

print(r5,r4,r3,r2,r1,r0)
