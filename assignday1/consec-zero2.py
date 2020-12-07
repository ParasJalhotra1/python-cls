lst=[]
FirstNum=int(input("Enter a number:"))
for cnt in range(100):
    lst.append(FirstNum+cnt)

print(lst)

for cnt in range(100):
    for num in range(2,lst[cnt]):
        if lst[cnt]%num==0:
            lst[cnt]=0
            break
print(lst)

ZeroCnt,MaxCnt=0,0
First,Last=0,0
for cnt in range(100):
    if lst[cnt]==0:
        ZeroCnt+=1
    else:
        if MaxCnt<ZeroCnt:
            MaxCnt=ZeroCnt
            First,Last=cnt-MaxCnt,cnt
print(f'ZeroCnt-{MaxCnt} between{lst[First]} and {lst[Last]}')