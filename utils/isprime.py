# Determine if a number is prime
# Definition of prime: it has no other positive divisors than 1 and itself

def is_prime(y):
	l = []
	for x in range(2, y):
		l.append(y % x)
	if 0 in l:
		return(False)
	else:
		return(True)