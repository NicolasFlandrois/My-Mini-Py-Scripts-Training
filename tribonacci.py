#!/usr/bin/python3
#Date : Thu 06 Jun 2019 21:35:17 CEST 
#Author: Nicolas Flandrois
#Description: This short script will compute the Tribonacci sequence.
#The Tribonacci sequence is a variante of Fibonacci, where a number n in the 
#sequence is equal to the sum of the 3 previous n number in the sequence.
# n  = (n-3) + (n-2) + (n-1)
#1, 1, 1, 3, 5, 9, 17, etc.

def trib(n:int):
	"""This generator yield each iteration of the tribonacci sequence, 
	for iteration of a range n number."""
	a, b, c = 1, 1, 1
	for i in range(n):
		yield a
		a, b, c = b, c, a+b+c
		
n = int(input("To what number of recurence do you want your Tribonacci list? "))
tribonacci = [f for f in trib(n)]
#Comprehension list applying the tribonacci generator, and holding the result in 
#a list, sequences.

print(tribonacci)
