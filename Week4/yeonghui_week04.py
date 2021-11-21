file = open('ex.txt', 'r')
def tosplit(x):
    a = x.split(" ")
    return a

f = file.readlines()

newList = []
for line in f:
   if(line[-1]=='\n'):
       newList.append(line[:-1])
   else:
       newList.append(line)
count1 = 0
count2 = 0
for x in range(1,6) :
    newarr= tosplit(newList[x])
    print(newarr[0]+"점수 : "+str(int(newarr[1])+int(newarr[2]))+"\n")
    count1=count1+int(newarr[1])
    count2=count2+int(newarr[2])
print("reading 평균 : "+str(count1/5)+","+"listening평균 : "+str(count2/5))
    
