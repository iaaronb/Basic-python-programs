#taking input and storing in a variable
x=input("Enter the First No.for comaprison==")
#taking input and storing in another variable
y=input("Enter the Second No.for comaprison==")
#implementing if statement to chechk whether which no. is greater
if int(x>y):
	print(f"{x} Is the largest no.")
elif int(y>x):
	print(f"{y} Is the largest no.")
