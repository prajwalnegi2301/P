'''1.sets are those things that store different values
2.sets are unordered, they print randomly
3.by default, sets are first priority not dictionary as dictionary alse has has same implemetaion.
4.sets and dictionary both starts with curly brackets
5. they can stor multiple data type like list'''

sets={1,2,3,4,4,5,5,6,7}
print(sets)# 1,2,3,4,5,6,7 values will be printed in unorder(random)

sets1={1,2,3,3,"hello",'f'}
print(sets1) # 3 will not print 2 times

# we will create an empty dictionary by this
sets2={}
print(type(sets2))

# to create an empty set
sets3=set()
print(type(sets3))

#insertion, union, add, difference
s1={"delhi","mumbai"}
s2={"chennai", "kolkata"}
print(s1.union(s2))
print(s1) # we will see that s1 is not change after union function
s1.update(s2)
print(s1) # after updating we will see that s1 now contains s2 (union)
# {A(union)B - A(intersection)B} -> symmetric_difference
print(s1.symmetric_difference(s2))

# if 'is' is present before function then it gives us either true or false
print(s1.isdisjoint(s2))

# superset and subset
print(s1.issuperset(s2))
print(s2.issubset(s2))

'''whenever error comes it means that iske neeche ki lines will not work'''

# add and remove
s1.add("okhla")
print(s1)
s1.remove("delhi")
print(s1)

# if we say { s1.remove("tokyo"), then it will give an error whereas if we say that s1.discard("tokyo"), it will give none as output }
s1.discard("japan")
print(s1)

# to pop and store it in an item
item=s1.pop()
print(item)

# "del" keyword will delete and if we print after that, it will show error.
del s2
print(s2)

# "clear" function empty kr dega set ko
s1.clear()
print(s1)  # abhi error show krega line no 52 del s2 ke print ki vjh se..





