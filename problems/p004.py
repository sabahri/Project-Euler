# Project Euler Problem 4
import numpy as np

palindromes = []

for i in range(100, 1000):
	for j in range(100, 1000):
		k = i*j
		rev_k = int(str(k)[::-1])
		if k == rev_k:
			palindromes.append(k)

palindromes = np.asarray(palindromes)
print(max(palindromes))
