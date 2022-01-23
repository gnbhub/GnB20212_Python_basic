a = int(input('3이상의 정수 입력: '))
li = []
li.append(0)
li.append(1)
for k in range(0, a-2, 1 ):
  li.append(li[k+1] + li[k])
print(li)
