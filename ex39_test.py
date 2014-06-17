import hashmap

# Tests that it will work.

jazz = hashmap.new()
hashmap.set(jazz, 'Miles Davis', 'Flamenco Sketches')
assert hashmap.get(jazz, 'Miles Davis') == 'Flamenco Sketches', "Failed Flamenco test."


# confirms set will replace previous one
hashmap.set(jazz, 'Miles Davis', 'Kind of Blue')
assert hashmap.get(jazz, 'Miles Davis') == 'Kind of Blue', "Failed Kind of Blue test."

hashmap.set(jazz, 'Duke Ellington', 'Beginning to See the Light')
assert hashmap.get(jazz, 'Duke Ellington') == 'Beginning to See the Light', "Failed test."

hashmap.set(jazz, 'Billy Strayhorn', 'Lush Life')
assert hashmap.get(jazz, 'Billy Strayhorn') == 'Lush Life', "Failed test."
# assert that Miles Davis is unchanged
assert hashmap.get(jazz, 'Miles Davis') == 'Kind of Blue', "Failed Kind of Blue test."

print "---- List Test ----"
hashmap.list(jazz)

# These replaced by assertions above
# print "---- Get Test ----"
# print hashmap.get(jazz, 'Miles Davis')
# print hashmap.get(jazz, 'Duke Ellington')
# print hashmap.get(jazz, 'Billy Strayhorn')

print "---- Delete Test ----"
print "** Goodbye Miles"
assert hashmap.get(jazz, 'Miles Davis') is not None, "Failed. Miles Davis should exist."
hashmap.delete(jazz, "Miles Davis")
assert hashmap.get(jazz, 'Miles Davis') is None, "Failed delete test. Miles Davis should not exist."
hashmap.list(jazz)

print "** Goodbye Duke"
hashmap.delete(jazz, "Duke Ellington")
hashmap.list(jazz)

print "** Goodbye Billy"
hashmap.delete(jazz, "Billy Strayhorn")
hashmap.list(jazz)

print "** Goodbye Pork Pie Hat"
hashmap.delete(jazz, "Charles Mingus")
assert hashmap.get(jazz, 'Charles Mingus') is None, "Failed delete test. Charles Mingus should not exist."
