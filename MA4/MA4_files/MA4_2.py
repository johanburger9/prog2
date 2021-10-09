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

	timings2 = []
	
	for n in range(30, 46):
		start2 = pc()
		f = Integer(n)
		end2 = pc()
		timings2.append(f.fib())
	plt.figure()
	plt.plot(range(30, 46), timings2)
	plt.plt.savefig(30_to_45c++.png)


if __name__ == '__main__':
	main()
