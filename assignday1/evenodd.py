x=int(input('enter a number:'))

print("the even numbers are:")
for i in range(x,x+10):
	if(i%2==0):
		print(i)

print("the add numbers are :")
for i in range(x,x+10):
	if(i%2==1):
		print(i)