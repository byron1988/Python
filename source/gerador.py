# Generators (geradores)
# Fibonacci: 1, 1, 2, 3, 5, 8 ...

def fib(max):
	x, y = 1, 1
	while x < max:
		yield x
		x, y = y, x + y


gen = fib(10)
'''
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
'''

for i in gen:
	print(i, end=' ')