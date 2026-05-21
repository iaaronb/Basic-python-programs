x=[1,2,4,5,6,8]
even_no_count=0
odd_no_count=0
for a in x:
    if a%2==0:
        even_no_count+=1
    elif a%2==1:
        odd_no_count+=1
print(even_no_count)
print(odd_no_count)