meraList=[ [111,'AaaA', 5000.43,'female'],
          [123,'AaBB', 4000.43,'male'],
          [121,'AACC', 9780.43,'female'],
          [131,'AddA', 2300.43,'male'] ]
print(*meraList,sep='\n')

print("This is the original list", meraList)

M=len(meraList)

for i in range(M):
    for j in range(3):
        if(meraList[j][0] > meraList[j+1][0]):
            meraList[j][0],meraList[j+1][0]=meraList[j+1][0],meraList[j][0]

for i in range(M):
    if(meraList[i][3]=="male"):
        meraList[i][1]="Mr." + meraList[i][1]

    elif(meraList[i][3]=="female"):
       meraList[i][1]="Ms." + meraList[i][1]

    meraList[i][2]=meraList[i][2] +  (meraList[i][2]*0.1)



print("This is the list after SORTING, PREFIXING AND ADDING 10% TO SALARY",*meraList,sep='\n')
