file = open('ex.txt','r')
f = file.readlines()
listensum = 0
readsum = 0
for line in f:

  #  newList.append(line.strip())
    b = line.split(" ")
    if(b[0]!="name"):
        print(b[0]+"점수 :"+str(int(b[1])+int(b[2])))
        readsum +=int(b[1])
        listensum +=int(b[2])

readavg=readsum/5
listenavg=listensum/5
print("reading평균 : "+str(readavg)+", listening평균 : "+str(listenavg))
file.close()
