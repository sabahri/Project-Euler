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
