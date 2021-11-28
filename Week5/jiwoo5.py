balance = 0 #잔고

def deposit(money): #입금하는 함수
    try :
        global balance
        balance = money + balance
    except :
        print('숫자를 입력하세요.')
def withraw(money): #출금하는 함수
    try :
        global balance
        balance = balance - money
    except :
        print('숫자를 입력하세요.')
def display():
    print('잔액 : '+ str(balance) +'원')
    
'''python'''

display()
deposit(3000)
display()
withraw('a')
display()
