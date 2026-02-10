# Project Euler Problem 3

import numpy as np
import sys
sys.path.append('../utils/')
from isprime import is_prime

m = 600851475143
n = int(np.sqrt(m) + 1)

#prime_factors = np.array([1])
prime_factors = []

# using isprime from sympy is kinda cheating,
# but right now I'm being lazy

for i in range(3, n + 1, 2):
	if m / i % 1 == 0:
		if is_prime(i):
			prime_factors.append(i)

prime_factors = np.asarray(prime_factors)
print(max(prime_factors))