#!/usr/bin/python

print ('enter any character from a-z : ')

def vowelChecker (inputchar):
	print ('enter character to check')
inputChar = raw_input()

if (inputChar == "a" or inputChar == "e" or
     inputChar == "i" or inputChar == "o" or inputChar == "u" ):
	print "character is vowel"
else:
	print "character is not vowel"




