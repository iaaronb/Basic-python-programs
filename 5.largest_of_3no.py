#taking input and storing in a variable
x=int(input("Enter A no.=="))
#taking input and storing in a variable
y=int(input("Enter A no.=="))
#taking input and storing in a variable
z=int(input("Enter a no.=="))
#making if statements for the calculations
if x>y>z or x>z>y:
	print(f"{x} Is the largest no.")
#making if statements for the calculations
elif y>z>x or y>x>z:
	print(f"{y} is the largest no.")
#making if statements for the calculations
elif z>y>x or z>x>y:
	print(f"{z} is the largest no.")
