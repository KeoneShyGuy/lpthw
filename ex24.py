from __future__ import print_function

print ("Let's practice everything.")
print ("You'\'d need to know \'bount escapes with \\ that do \n newlines and \t tabs.")

Poem = """
\t The lovely world
with logic fo firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print ("_______________")
print (Poem)
print ("_______________")

five = 10 - 2 + 3 - 6
print ("This should be five: %s" % five)

def secret_formula(started):
	JellyBeans = started * 500
	Jars = JellyBeans / 1000
	Crates = Jars / 100
	return JellyBeans, Jars, Crates
	
StartPoint = 10000

Beans, Jars, Crates = secret_formula(StartPoint)

print ("With a starting point of: {}.".format(StartPoint))
print ("We'd have {} beans, {} jars, and {} crates.".format(Beans, Jars, Crates))

StartPoint = StartPoint / 10

print ("We can also do that this way:")
print ("We'd have {} beans, {} jars, and {} crates.".format(secret_formula(StartPoint)))