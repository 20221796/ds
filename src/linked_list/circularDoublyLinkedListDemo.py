from circularDoublyLinkedList_copy import *

list = CircularDoublyLinkedList()
list.append(30); list.insert(0,20)

a=[1,2,3,4,5]
list.extend(a)
list.reverse()
list.pop(0)

print("count(3): ", list.count(3))
print("get(2): ", list.get(2))
list.printList()