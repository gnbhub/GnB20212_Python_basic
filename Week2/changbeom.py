#Q1
x=input("정수를 입력하세요: ")
z=0
k=int(x)
for y in range(1, k+1, 1):
  z = z+y
print("1부터 정수까지의 합: ",z)

#Q2
x=input("정수를 입력하세요: ")
z=0
k=int(x)
for y in range(1, k+1, 1):
  if k%y == 0:
    z=z+1
if z == 2:
  print('소수입니다.')
else:
  print('소수가 아닙니다.')
