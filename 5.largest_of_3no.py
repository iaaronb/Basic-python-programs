x=int(input("Enter A no.=="))
y=int(input("Enter A no.=="))
z=int(input("Enter a no.=="))
if x>y>z or x>z>y:
	print(f"{x} Is the largest no.")
elif y>z>x or y>x>z:
	print(f"{y} is the largest no.")
elif z>y>x or z>x>y:
	print(f"{z} is the largest no.")