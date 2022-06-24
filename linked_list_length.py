'''
Given a singly linked list, return its length
'''
class Node():
  def __init__(self, val =0):
    self.val = val
    self.next = None
    
def returnLength(node):
  length = 0
  while node:
    length+=1
    node = node.next
  return length
def printLinkedList(head):
  node = head
  while node:
    print("val: ", node.val)
    node = node.next

node_values = ["harry", "styles", "loves", "architecture"]
head = None
count =  0
for word in node_values:
  node = Node(word)
  count+=1
  node.next = head
  head = node

print("Expecting linked list size of: ", count, "\n------")
print("linked list size", returnLength(head))
printLinkedList(head)
    
  