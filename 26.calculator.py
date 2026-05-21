#It is the function for the whole calculator programme
def calc():
	print("*************************Welcome to python Calculator!***************************************************")
	#taking the 1st input from the user
	x=int(input("Enter 1st no. ="))
	#check whether the input is a integer
	if x!=int():
		print("!")

	print("*******************************************************************************************************************")
	#taking the 2nd input from the user
	y=input("Enter  2nd no.=")
	if y!=int():
		print("!1")

	print("*******************************************************************************************************************")
	#instructions to the user
	print("""
	For Addition    Enter       = = 1 
	For Subraction     Enter     = = 2
	For Multilplication  Enter    = = 3
	For Division         Enter    = = 4
	For Floor Division Enter     = = 5
	For Exponent    Enter       = = 6
	""")
	print("*******************************************************************************************************************")
	#getting input for the method of calculation
	z=input("Enter ur method ==")
	#makking functions for each calculations
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
	#making if statements for the calculations
	if int(z)==1:
		add()
	elif int(z)==2:
		sub()
	elif int(z)==3:
		mult()
	elif int(z)==4:
		div()
	elif int(z)==5:
		floor()
	elif int(z)==6:
		expo()
	elif ValueError:
		print("hi")
	#taking input whether to countinue or stop the program
	print("Do You Want to countinue?")
	x=input("y/n?")
	if x=="y" :
		calc()
	else:
		print("Thank You!!")
		
calc()

	
