# %d for digit or number format ?

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r displays in raw form
print "I said: %r." % x

# %s is a normal string unquoted, but is contained inside single quotes.
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# plus sign appears to be string concatenation
print w + e
