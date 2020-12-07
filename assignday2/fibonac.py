num = int(input('enter number:'))
def Fibonacci(n):
	a = 0
	b = 1
	if n<0:
		print("positive number")
	elif n==0:
		return b
	else:
		for i in range(1,n):
			c = a + b
			a = b
			b = c
		return b
print(Fibonacci(num))