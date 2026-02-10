import numpy as np
from sympy import *

'''
# Project Euler Problem 1

n = 1000
base = np.array([3, 5])

max_mult = n/base

# Make max_mult the highest multiples of 3, 5 below 1000
for i in range(base.shape[0]):
	j = max_mult[i] % 1
	if j == 0.0 :
		max_mult[i] = int(max_mult[i]) - 1
	else:
		max_mult[i] = int(max_mult[i])

max_3 = int(max_mult[0])
max_5 = int(max_mult[1])

sum3 = 0
for k in range(1, max_3 + 1):
	sum3 += k*3

sum5 = 0
for l in range(1, max_5 + 1):
	if l % 3 != 0.0 :
		sum5 += l*5

sum_array = np.array([sum3, sum5])

print(sum3 + sum5)

# My favorite solution
#print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))
'''

'''
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
'''

'''
# Project Euler Problem 3

m = 600851475143
n = int(np.sqrt(m) + 1)

prime_factors = np.array([1])

# using isprime from sympy is kinda cheating,
# but right now I'm being lazy

for i in range(3, n + 1, 2):
	if m / i % 1 == 0:
		if isprime(i):
			prime_factors = np.append(prime_factors, i)

prime_factors = np.delete(prime_factors, 0)
print(max(prime_factors))
'''

'''
# Project Euler Problem 4

palindromes = np.array([1])

for i in range(100, 1000):
	for j in range(100, 1000):
		k = i*j
		rev_k = int(str(k)[::-1])
		if k == rev_k:
			palindromes = np.append(palindromes, k)

palindromes = np.delete(palindromes, 0)
print(max(palindromes))

'''

# Project Euler Problem 5

m = 20

primes = np.array([1])
not_primes = np.array([1])

for i in range(3, m+1):
	if isprime(i):
		primes = np.append(primes, i)
	else:
		not_primes = np.append(not_primes, i)







# # primes = np.array([1, 2, 5, 7])

# # prod_of_primes = (primes[:, None] * primes[None, :]).flatten()

# for i in range(3, m + 1, 2):
# 	if isprime(i): 
# 		primes = np.append(primes, i)


# def find_factors(number):
# 	factors = np.array([1])

# 	for j in range(2, int(number/2) + 1):
# 		if j/k % 1 == 0:
# 			factors = factors.append([j])
# 		return(favtors)










