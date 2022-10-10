# Import random
import random

# 2 lists, 10 random numbers each
numbers1 = []
numbers2 = []
result = []
for i in range(10):
	numbers1.append(random.randint(0,100))
	numbers2.append(random.randint(0,100))

# List for sum of each list at index
sumNums = []
for i in range(10):
	sumNums.append(numbers1[i] + numbers2[i])

print("First list:",numbers1)
print("Second list:", numbers2)
print("Sum of both lists:", sumNums)
