## LISTS in python
print("\n ... LISTS IN PYTHON ... \n")

# Inserting elements in a list
print("Enter list elements: -> ")
l = []
for i in range(5):
	a = int(input())
	l.append(a)

# Length of list
print('Length of list: ',len(l))

# SLICING
x = l[1:4]
print('List slice[1-4]:', x)

# APPEND List
l.append(20)
print('Append 20 to list: ', l)

# EXTEND List
l2 = [5,11,6]
l.extend(l2)
print('Extend a list: ', l)

# INSERT in a list
l.insert(3,99)
print('Insert element at (pos=3, val=99): ', l)

# SORT list
l.sort()
print('Sorted List: ', l)

# POP element from list (index)
l.pop(1)
print('Pop element from list [pop(index)]: ', l)

# SUM of elements in list
print('Sum of all elemnts: ', sum(l))

# Count occurences on an element in list
n = int(input("Enter element you wish to count: "))
print('Occurences of x in list: ' , l.count(n))