x= int(input('enter a number'))

b= []

for num in range(x, x+ 100):
	if num > 1:
		for i in range(2, num):
			if (num % i)==0:
				break
		else:
			b.append(num)
print(b)