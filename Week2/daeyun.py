#Q1

number = int(input("숫자 입력 : "))
sum = 0
for x in range (1,number+1):
    sum = sum + x
print ("합 :",sum)


#Q2

number=int(input("숫자를 입력하세요 (0은 종료) : "))
if number==0:
    print("종료")
else:
    for divisor in range(2, number):
        while divisor < number:
             if number % divisor == 0:
                   break
             divisor += 1
        if divisor == number:
            print("소수입니다.")
            break
        else:
            print("소수가 아닙니다.")
            break
                
