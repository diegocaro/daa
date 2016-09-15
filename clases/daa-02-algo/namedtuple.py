from collections import namedtuple

LinkedList = namedtuple('LinkedList', ['value', 'prev', 'next'])

head = LinkedList(5, None, None)
newnode = LinkedList(-1, head, None)

#updating the "next" reference in head
head = head._replace(next=newnode) 

ptr = head
while ptr != None:
  print(ptr.value)
  ptr = ptr.next