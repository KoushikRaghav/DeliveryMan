def main():
	n = int(input("\nEnter the N: "))
	x = int(input("\nEnter the x: "))
	y = int(input("\nEnter the y: "))
	print "\nEnter a & b\n"

	a = [int(i) for i in raw_input().split()]
	b = [int(i) for i in raw_input().split()]
	c= {}
	
	for i in range(n):
		c[i] = (a[i] - b[i])
	
	d= sorted(c.keys(), key=lambda x:c[x])
	sum = 0
	i = 0
	# import pdb;pdb.set_trace()
	j = n-1
	for z in range(len(d)):
		if (abs(c[d[i]]) > abs(c[d[j]])):
			if(i<y):
				sum = sum + b[d[i]]				
				i = i+1
			elif (n-j-1) < x:
				sum = sum + a[d[j]]
				j = j-1					
		else:
			if (n-j-1) < x:
				sum = sum + a[d[j]]
				j = j-1		
			elif(i<y):
				sum = sum + b[d[i]]
				i = i+1					
	print sum

if __name__ == '__main__':
    main()































