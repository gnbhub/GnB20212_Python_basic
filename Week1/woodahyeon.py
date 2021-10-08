#Q1

print (type('hello'))
print (type(123))
print (type(3.22))
print (type(True))
print (type('2'))
print (type("3"))
 

#Q2_1

n = int(input("0~63 사이의 정수를 입력해주세요. : "))
if n >= 0 and n <= 63:
    n0 = int(n%2)
    n = n//2
    if n != 0:
        n1 = int(n%2)
        n =n//2
    else: print (n0)
    if n != 0:
        n2 = int(n%2)
        n = n//2
    else: print (n1,n0)
    if n != 0:
        n3 = int(n%2)
        n = n//2
    else: print (n2,n1,n0)
    if n != 0:
        n4 = int (n%2)
        n = n//2
    else: print (n3,n2,n1,n0)
    if n != 0:
        n5 = int (n%2)
        print(n5,n4,n3,n2,n1,n0)
    else: print (n4,n3,n2,n1,n0)


#Q2_2

num = int(input ("0~63 사이의 정수를 입력해주세요. : "))
if num >= 0 and num <= 63:
    print (bin(num)[2:])
    
    
