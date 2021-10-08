Q1
print(type('hello'))
print(type(123))
print(type(3.22))
print(type(True))
print(type('2'))
print(type("3"))

Q2
1) bin함수 이용하여 2진수 구현하기
num1 = int(input("0에서 63사이의 정수를 입력해주세요. :"))
if 0 <= num1 <=63:
    print(bin(num1))
else:
    print("정수를 다시 입력해주세요.")
   
2) format 함수 이용하여 2진수 구현하기
um1 = int(input("0에서 63사이의 정수를 입력해주세요. :"))
if 0 <= num1 <=63:
    print('{:#b}'.format(num1))
else:
    print("정수를 다시 입력해주세요.")
    
3) 몫과 나머지 이용하여 2진수 구현하기 
num = int(input("0에서 63사이의 정수를 입력해주세요. :"))
if 0<= num <= 63:
    num1 = num % 2
    num = num//2
    if num != 0:
        num2 = num % 2
        num = num//2
    else:
        print (num1)
    if num != 0:
        num3 = num % 2
        num = num//2
    else:
        print(num2,num1)
    if num != 0:
        num4 = num % 2
        num = num//2
    else:
        print(num3,num2,num1)
    if num != 0:
        num5 = num % 2
        num = num//2
    else:
        print(num4,num3,num2,num1)
    if num != 0:
        num6 = num % 2
        num = num//2
        print(num6,num5,num4,num3,num2,num1)
    else:
        print(num5,num4,num3,num2,num1)
else:
    print("정수를 다시 입력해주세요.")
