def add(a, b):
	print "ADDING {} + {}".format(a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING {} - {}".format(a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING {} 8 {}".format(a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING {} / {}".format(a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(20, 7)
height = subtract(72, 6)
weight = multiply(20, 8)
iq = divide(240, 2.1)

print "Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: {}. Can you do it by hand?".format(what)