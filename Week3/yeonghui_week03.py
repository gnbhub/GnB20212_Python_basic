def tosplit(x):
    a = x.split(" ")
    return a
st=input("문자열을 입력하세요 : ")
newst= tosplit(st)
for new in newst:
    print(new)
