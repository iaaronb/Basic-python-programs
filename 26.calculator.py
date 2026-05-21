def calc():
	print("*************************Welcome to python Calculator!***************************************************")
	x=int(input("Enter 1st no. ="))
	if x!=int():
		print("!")

	print("*******************************************************************************************************************")
	y=input("Enter  2nd no.=")
	if y!=int():
		print("!1")

	print("*******************************************************************************************************************")
	print("""
	For Addition    Enter       = = 1 
	For Subraction     Enter     = = 2
	For Multilplication  Enter    = = 3
	For Division         Enter    = = 4
	For Floor Division Enter     = = 5
	For Exponent    Enter       = = 6
	""")
	print("*******************************************************************************************************************")

	z=input("Enter ur method ==")
	def add():
		print(x+y)
	def sub():
		print(x-y)

	def div():
		print(x/y)

	def floor():
		print(x//y)

	def mult():
		print(x*y)

	def expo():
		print(x**y)
	if int(z)==1:
		add()
	if int(z)==2:
		sub()
	if int(z)==3:
		mult()
	if int(z)==4:
		div()
	if int(z)==5:
		floor()
	if int(z)==6:
		expo()
	if ValueError:
		print("hi")
	print("Do You Want to countinue?")
	x=input("y/n?")
	if x=="y" :
		calc()
	else:
		print("Thank You!!")
		
calc()

	
