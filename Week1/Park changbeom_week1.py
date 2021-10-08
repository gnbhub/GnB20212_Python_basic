#Q1
print(type('hello'))
print(type(123))
print(type(3.22))
print(type('2'))
print(type("3"))

#Q2
number = input("0~63사이 정수 선택: ")
number = int(number)

if (number != 0):
    num1 = number%2
    number = number//2
else:
    num1 = 0

if (number != 0):
    num2 = number%2
    number = number//2
else:
    num2 = str("")
    
if (number != 0):
    num3 = number%2
    number = number//2
else:
    num3 = str("")
    
if (number != 0):
    num4 = number%2
    number = number//2
else:
    num4 = str("")
    
if (number != 0):
    num5 = number%2
    number = number//2
else:
    num5 = str("")
    
if (number != 0):
    num6 = number%2
    number = number//2
else:
    num6 = str("")
    
if (number != 0):
    num7 = number%2
    number = number//2
else:
    num7 = str("")

print(str(num7)+str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1))
