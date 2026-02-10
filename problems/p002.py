# Project Euler Problem 2

a = 1
b = 2

def fibonacci(maxval):
	x = 1
	y = 2
	n = 2
	while True:
		z = x + y 
		if z > maxval:
			return n
		else:
			if z % 2 == 0:
				n += z
			x = y 
			y = z

	return(n)

print(fibonacci(4000000))