ex = open('ex.txt', 'w')
ex.write("name reading listening\n"
"tim 300 300\n"
"yarn 285 350\n"
"tei 390 420\n"
"hyuk 250 400\n"
"hong 330 350")
ex.close()

ex2 = open('ex.txt','r')
name = ex2.readlines()
name1 = []
for line in name:
  if(line[-1]=='\n'):
    name1.append(line[:-1])
  else:
    name1.append(line)
print(name1)

sum1 = 0
sum2 = 0
for k in range(1, len(name1), 1):
    name2 = name1[k]
    name3 = name2.split()
    name4 = name3[0]
    name5 = int(name3[1]) + int(name3[2])
    name4_1 = str(name4)
    name5_1 = str(name5)
    print(name4_1+'점수: '+name5_1)
    sum1 = sum1 + int(name3[1])
    sum2 = sum2 + int(name3[2])

average1 = str(sum1/(len(name1)-1))
average2 = str(sum2/(len(name1)-1))
print('reading평균: '+average1+', listening평균: '+ average2)

ex2.close()
