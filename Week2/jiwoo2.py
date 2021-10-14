a = int(input('숫자 입력 : '))
c=0

for r in range(0,a+1,1) :
    c = c+r 
    
    
print(c)


b = int(input('숫자를 입력하세요 (0 : 종료) : '))
while True :
    if b == 0 :
        break
    else :
        
        for r in range(2,b-1,1):
            c=b%r
            if c == 0 :
                print('소수가 아닙니다.')
                break
        else :
            
            print('소수입니다.')
            break
        break






