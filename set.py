# set

s={10,20,30}
print(s)
print(type(s))

s.add(40)
s.add(50)
print(s)

s.clear()
print(s)

# set difference
s1={10,20,30}
s2={30,40}
s=s2.difference(s1)
print(s)

# intersection
s1={10,20,30}
s2={30,40}
s=s1.intersection(s2)
print(s)

# union
s1={10,20,30}
s2={30,40}
s=s1.union(s2)
print(s)

# disjoint
s1={10,20,30}
s2={30,40}
print(s1.isdisjoint(s2))

# symmetric difference
s1={10,20,30}
s2={30,40}
s=s1.symmetric_difference(s2)
print(s)

# sub set
s1={10,20,30}
s2={10,20,30,40}
print(s1.issubset(s2))

# super set
s1={10,20,30}
s2={30,40}
print(s1.issuperset(s2))

# pop
s={10,20,30}
print(s.pop())
print(s.pop())

# remove
s={10,20,30,40}
s1=s.remove(40)
print(s)