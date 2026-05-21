x=int(input("Enter =="))
if x%2!=1:	
	for A in range(x):
		x-=2
		print(x)
		if x==0:
			break 
if x%2==1:
	x-=1
	print(x)
	for A in range(x):
		x-=2
		print(x)
		if x==0:
			break 