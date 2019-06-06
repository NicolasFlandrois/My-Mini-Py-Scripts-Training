#!/usr/bin/python3
#Date : Mon 28 Jan 2019 03:24:59 PM CET 
#Author: Nicolas Flandrois
#Description: This short script will compute the Fibonacci sequence.
# n  = (n-2) + (n-1)
#1, 1, 2, 3, 5, 8, 13, 21, etc

def fib(n:int):
	"""This generator yield each iteration of the fibonacci sequence, 
	for iteration of a range n number."""
	a, b = 0, 1
	for i in range(n):
		yield a
		a, b = b, a+b
		
n = int(input("To what number of recurence do you want your fibonacci list? "))
fibonacci = [f for f in fib(n)]
#Comprehension list applying the fibonacci generator, and holding the result in 
#a list, sequences.

print(fibonacci)
