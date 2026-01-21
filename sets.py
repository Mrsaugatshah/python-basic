# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)


# myset = {"apple", "banana", "cherry"}
# print(type(myset))

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)


# thisset = {"apple", "banana", "cherry"} cant directly accessed index

# for x in thisset:
#   print(x)
  
# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)
 
 
 #TO ADD

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)



#TO REMOVE

# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()

# print(x)

# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)



# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

#JOIN SETS

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1 | set2
# print(set3)



#JOIN TUPLE AND SETS
# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)


# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)



# #INTERSECITION
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)




# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)




#DEFFERECE
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)



# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 - set2
# print(set3)


#SYMITRIC DEFF
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2)

# print(set3)



# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.symmetric_difference_update(set2)

# print(set1)



#FROZENSETS
# x = frozenset({"apple", "banana", "cherry"})
# print(x)
# print(type(x))



