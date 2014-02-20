numbers = []

def do_loop(thelist,max):
    i = 0
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i+1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return thelist

numbers = do_loop(numbers,6)


print "The numbers: "

for num in numbers:
    print num
