x=input("enter a word")
v=["a","e","i","o","u","A","E","I","O","U"]
c=0
for g in x:
	if g in v:
		c=c+1	
print(c)