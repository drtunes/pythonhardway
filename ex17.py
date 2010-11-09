# Python the Hard Way
# Exercise 17: More Files

from sys import argv
from os.path import exists

script, source, destination = argv

print "Copying from %s to %s" % (source, destination)

input = open(source)
indata = input.read()

print "the input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(destination)
print "Ready, type ENTER to continue, CTRL-C to abort."
raw_input()

output = open(destination, 'w')
output.write(indata)

print "Alright, done."

input.close()
output.close()
