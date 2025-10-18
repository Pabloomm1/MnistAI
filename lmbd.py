x = []
for i in range (3):
	x.append(lambda: i**2)

print (x[1]())