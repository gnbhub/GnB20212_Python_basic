ex = open('ex.txt','r')
f = ex.readlines()

for i in range(1,6):
    x = f[i].split()
    print(x[0]+"점수 : "+str(int(x[1]) + int(x[2])))

z = 0
k = 0

for j in range(1,6):
    y = f[j].split()
    z = z + int(y[1])
    k = k + int(y[2])

z2 = z/5
k2 = k/5

print("reading 평균 : " + str(z2) + ", listening 평균 : " + str(k2))
