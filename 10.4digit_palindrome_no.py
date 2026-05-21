#taking the 1st input from the user
x=input("Enter the no.")
# setting the variable r with the reverse of x 
y=x[::-1]
#if statement to look whether it is a palindrome no.
if x==y:
	print("It is a palindrome number")
else:	
	print("It is not a palindrome number")
