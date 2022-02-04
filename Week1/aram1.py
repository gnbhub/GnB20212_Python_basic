#Q1
print(type('Hello'))
print(type(123))
print(type(3.22))
print(type(True))
print(type('2'))
print(type("3"))

#Q2_1 (조건문)
print("0~63사이의 정수: ")
number = int(input())

num1 = number%2
number = number//2

num2 = number%2
number = number//2

num3 = number%2
number = number//2

num4 = number%2
number = number//2

num5 = number%2
number = number//2
    
num6 = number%2
number = number//2

print(num6,num5,num4,num3,num2,num1)
    

#Q_2 (bin())
number = int(input("0~63사이의 정수: "))
print(bin(number))

#Q_3 (format())
number = int(input("0~63사이의 정수: "))
print(format(number, 'b'))



