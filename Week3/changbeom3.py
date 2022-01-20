x=input('문자열을 입력:')
def split(x):
  y=x.split()
  k = len(y)
  for i in range(0, k, 1):
    print(y[i])
split(x)
