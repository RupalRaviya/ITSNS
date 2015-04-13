#!/usr/bin/python

import sys

def main():

#	b = range(10)
	a = input("Enter the value:")
	print type(a)
	if a < range(0,9):
		print "value is in range"
	else:
		print "value is not in range"
main()

