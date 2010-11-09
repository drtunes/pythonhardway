# Python the Hard Way
# Exercise 20: Functions and Files

from sys import argv

script, input = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
file = open(input)

print "First let's print the whole file:\n"
print_all( file )

print "Now let's rewind, kind of like a tape."
rewind( file )

print "Let's print three lines:"

line = 1
print_a_line( line, file )

line = line + 1
print_a_line( line, file )

line = line + 1
print_a_line( line, file )

