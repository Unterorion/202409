list1 = [3,2,1]
print(list1)

list1.append(4)
print(list1)

'''list2 = list1
list1.pop()
print(list2)
print(list1)'''

list1.append([5,6])
print(list1)

print(list1.pop())
print(list1)

list2 = [5,6]
list1.extend(list2)
print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)

list1.insert(0,7)
print(list1)

list1.append(7)
list1.extend([6,5])
print(list1)

print(list1.count(7))

list1.remove(7)
print(list1)