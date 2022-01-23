balance = 0
def deposit():
  money = int(input('입금할 금액: '))
  global balance
  balance = balance + money
  balance2 = str(balance)
  print('잔액: '+ balance2 + '원')

def withraw():
  money = int(input('출금할 금액: '))
  global balance
  balance = balance - money
  balance2 = str(balance)
  print('잔액: '+ balance2 + '원')

def display():
  global balance
  balance2 = str(balance)
  print('잔액: '+ balance2 + '원')

a = 'true'
while a == 'true':
  try:
    menu = input('입금: 1번, 출금: 2번, 잔액 확인: 3번, 종료: 0번 \n번호 입력: ')
    menu = int(menu)
    if menu == 1:
      deposit()
    elif menu == 2:
      withraw()
    elif menu == 3:
      display()
    elif menu == 0:
      print('프로그램을 종료합니다.')
      break
    else:
      print('번호를 다시 입력해주세요.')
  except:
    print('정수를 입력해주세요.')
