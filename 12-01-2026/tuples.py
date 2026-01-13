# tuple is a built-in data type in python that represents immutable sequence of object, means tuple is a collection which is ordered and unchangeable , allow Duplicates. 
# they can contain heterogeneous data types(different type of data). 
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created. But if you want to change tuple first chnage into list and than update and again change into tuple.

mytuple = ("apple","banana","cat",1)
print(mytuple[1])
print(mytuple[-1]) # from back
print(mytuple[1:3]) # range
print(len(mytuple))
print(type(mytuple[2]))
print(type(mytuple[3]))

mytuple1 = list(mytuple)
mytuple1[1]=8
print(mytuple1)
mytuple1.remove("apple")
mytuple=tuple(mytuple1)
print(type(mytuple))
print(mytuple)

print(mytuple.count("cat"))