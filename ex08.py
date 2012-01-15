# Python the Hard Way
# Exercise 8: Printing, Printing

f = "%r %r %r %r"

print f % (1, 2, 3, 4)
print f % ("one", "two", "three", "four")
print f % (True, False, False, True)
print f % (f, f, f, f)
print f % (
	"i had this thing.",
	"that you could type up right.",
	"but it didn't sing.",
	"so i said goodnight."
	)
