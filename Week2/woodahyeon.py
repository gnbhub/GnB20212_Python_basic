
#Q1

while True:
    num = int(input("숫자 입력 : "))
    if num < 1 :
        print("1 이상의 정수를 입력해주세요.")
        continue
    break
sum = 0
for i in range (1,num+1):
    sum = sum + i
print ("합 :",sum)


#Q2

n = int (input("숫자를 입력하세요 ( 0: 종료 ) : "))
while True:
    if n == 0: break
    else:
        for i in range (2,n):
            if n % i == 0:
                print("소수가 아닙니다.")
                break
        else:
            print("소수입니다.")
    break
