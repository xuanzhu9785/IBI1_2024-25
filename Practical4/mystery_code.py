# What does this piece of code do?
# Answer: It shows how many trials are needed to randomly choose matching numbers from two separate (1,6) samples.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint #import randint function from random

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil #import ceil function from math

progress=0
while progress>=0: #circulation
	progress+=1
	first_n = randint(1,6)
	second_n = randint(1,6)
	if first_n == second_n:
		print(progress)
		break