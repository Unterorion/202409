s = set('hello')
print(s)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1&s2)
print(s1.intersection(s2))

print(s1|s2)
print(s1.union(s2))

print(s1-s2)
print(s1.difference(s2))
print(s2-s1)
print(s2.difference(s1))

s1.add(0)
print(s1)

s2.update([10,11,12])
print(s2)

s1.remove(0)
print(s1)