#!/usr/bin/env python3

from integer import Integer


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
	start2 = pc()
	f = Integer(8)
	print(f.fib())
	end2 = pc()
	

if __name__ == '__main__':
	main()
