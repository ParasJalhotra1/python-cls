seq=[0,2,3,0,0,0,0,0,7,0,0,11]

result=1
max_result=0
test=seq[0]

for v in seq[1:]:
	if v==test:
		result += 1
	else:
		if result > max_result:
			max_result = result
		test = v
		result = 1 

if result > max_result:
	max_result = result
 
print(max_result)