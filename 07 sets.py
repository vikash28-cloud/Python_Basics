#  set is a collection of non repeatative elements.
'''set = {1,2,3,4,5,"vikash","1",1,2}
print(set) #it cannot print the repeat value of element
print(type(set))'''

#empty set 
'''set1 = {} # dictionary
set2 = () # tuple
set3 = [] # list
set4 = set() # empty set 
print(type(set1))
print(type(set2))
print(type(set3))
print(type(set4))'''

# adding values to an empty set
'''v = set()
print(type(v))
v.add(4)
v.add(1)
v.add(4)
print(v)'''

# methods in set
a = {1,2,3,8,3,8,10}
'''a.add((5,4,9)) # adding elements 
print(a)
print("there are",len(a),"elements present in a set")#how many elements in a set    
a.remove(1) # remove an element from set
a.remove(3)
print(a)
print(a.clear())  # empty the set'''

#union--
print(a.union({11,12,13}))

#intersection--
print(a.intersection({1,2,10}))

