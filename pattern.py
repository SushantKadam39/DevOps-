number=(1,2,3,4,5,6)
even_count=0
odd_count=0
for num in number:
	if num%2==0:
		even_count+=1
	else:
		odd_count+=1

print("Even number:",even_count)
print("odd number:",odd_count)

