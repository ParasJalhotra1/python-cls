num=int(input('Enter a number: '))

t = num%2==0

if(t):
    print('Even:', end=' ')
    for i in range(num,num+10,2):
        print(i, end=' ')
    print()
    print('Odd: ', end=' ')
    for i in range(num+1,num+10,2):
        print(i, end=' ')
else:
    print('Odd: ', end=' ')
    for i in range(num,num+10,2):
        print(i, end=' ')
    print()
    print('Even:', end=' ')
    for i in range(num+1,num+10,2):
        print(i, end=' ')
