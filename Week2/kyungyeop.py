Q1
i = 0
hap = 0
num = 0
num = int(input("숫자 입력 :"))
while i <= num:
    hap = hap+i
    i = i+1

print("합 : %d" % hap) 

Q2
num = 0
num = int(input("숫자를 입력하세요.( 0 : 종료) :"))
while True:
    if num == 0 :
        print("실행을 종료하겠습니다.")
        break
    elif num == 1:
        print("소수가 아닙니다.")
        break
    else:
        for i in range(2,num,1) :
            if num % i == 0:
                print("%d는(은) 소수가 아닙니다." %num)
                break
            else:
                print("%d는(은) 소수입니다."%num)
                break
    break
