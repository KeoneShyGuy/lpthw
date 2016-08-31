# trying to figure out how this logic works since it may come in handy in the future
b = 5
a = 32.5

while b:
	a, b = b, a%b
	print "a: {} | b: {}".format(a, b)