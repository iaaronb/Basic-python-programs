x=int(input("Enter"))
def prime():
    for a in range(2,x):
        if x%a==0:
            print("it is not a prime no")
            break
    else:
        print("it is  a prime no")
prime()