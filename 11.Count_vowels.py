#taking the 1st input from the user
x=input("enter a word")
#defining the variable in a list
v=["a","e","i","o","u","A","E","I","O","U"]
c=0
#adding a for loop for finding the vowels
for g in x:
	if g in v:
		#adding the count +1 for each time a vowel is detetcted
		c=c+1	
print(c)
