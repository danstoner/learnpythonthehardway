numbers = []

def do_loop(thelist,max,inc):
    """This function accepts a list, the max value, and the increment by value."""
    i = 0
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i+inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return thelist

numbers = do_loop(numbers,6,1)


print "The numbers: "

for num in numbers:
    print num

numbers = []
numbers = do_loop(numbers,6,2)
print "AGAIN the numbers by twos..."
for num in numbers:
    print num
