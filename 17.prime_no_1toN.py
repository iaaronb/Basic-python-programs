x=int(input("Enter the starting digit=="))
y=int(input("Enter the ending digit=="))
if x%2==0:
	for a in range (y-x):
		print(x)
		x+=2
		if y%2==0:
			print(y)
		if x>=y:
			break
elif x%2==1:
	x+=1
	for a in range (y-x):
		print(x)		
		x+=2
		if y%2==0:
			print(y)
		if x>=y:
			break


