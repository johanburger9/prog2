#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

def main():
	#f = Integer(5)
	#print(f.get())
	#f.set(7)
	#print(f.get())
	
	timings1 = []
	for n in range(30, 46):
		start1 = pc()
		fib_py(n)
		end1 = pc()
		timings1.append(end1-start1)
	plt.figure()
	plt.plot(range(30, 46), timings1, '.')
	plt.show()
	plt.savefig('30_to_45python.png')

	
	"""timings2 = []
	for n in range(30, 46):
		start2 = pc()
		f = Integer(n)
		end2 = pc()
		timings2.append(end2-start2)
	plt.figure()
	plt.plot(range(30, 46), timings2, '.')
	plt.show()
	plt.savefig('MA4_files' + '30_to_45cplusplus.png')"""


if __name__ == '__main__':
	main()
