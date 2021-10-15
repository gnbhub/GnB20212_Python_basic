# Quiz1
num = input("숫자 입력: ")
number = int(num)
sum1=0
for x in range(1,number+1,1):
    sum1=sum1+x
print("합 : ", sum1)

#Quiz2
loop = True
count = 0
while loop :
    num = input("숫자를 입력하세요(0: 종료) : ")
    number = int(num)
    if number==0 :
        break
    for x in range(2,number,1) :
        if (number%x==0) :
            print("소수가 아닙니다.")
            count=count+1
            break
    if count==0 :
        print("소수입니다.")
