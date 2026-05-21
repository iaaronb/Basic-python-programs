x=input("Enter==")
y=["Q","W","E","R","T","Y","U","I","O","P","L","K","J","H","G","F","D","S","A","Z","X","C","V","B","N","M"]
z=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","m","n","b","v","c","x","z"]
l=["1","2","3","4","5","6","7","8","9","0"]
u=0
lo=0
no=0
for A in x:
	if A in y:
		u+=1

	elif A in z:
		lo+=1

	elif A in l:
		no+=1
print(f"{u} Upper charecters are there!")
print(f"{lo} Small charecters are there!")
print(f"{no} Number are there!")
