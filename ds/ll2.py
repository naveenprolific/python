class Node:
 def __init__(self,data):
  self.data=data
  self.next=None
 
class LinkedList:
 def __init__(self):
  self.head=None
  self.size=0
 
 
 
 def append(self,data):
  if(self.head==None):
   newnode=Node(data)
   self.head=newnode
  else:
   current=self.head
   while(current.next!=None):
    current=current.next
   current.next=Node(data)
  self.size=self.size+1
 
 
 
 def insert(self,data,position):
  if(position==0):
   newnode=Node(data)
   newnode.next=self.head
   self.head=newnode
  elif(position>self.size):
   print("\n\nIndex is out of range\n\n")
  elif(position==self.size):
   self.append(data)
  else:
   current=self.head
   count=0
   while(current!=None):
    if(count==position-2):
     break
    else:
     count+=1
     current=current.next
   newnode=Node(data)
   newnode.next=current.next
   current.next=newnode
 
 
 def printlist(self):
  current=self.head
  while(current!=None):
   print(current.data,end=" ")
   current=current.next
mylinklist=LinkedList()
mylinklist.append(4)
mylinklist.append(5)
mylinklist.append(8)
mylinklist.append(10)
print("\n\nThe linked list before insertion:\n\n")
mylinklist.printlist()
mylinklist.insert(6,3)
print("\n\nThe linked list after insertion:\n\n")
mylinklist.printlist()
mylinklist.insert(10,4)
print("\n\nThe linked list after insertion:\n\n")
mylinklist.printlist()
mylinklist.insert(2,0)
print("\n\nThe linked list after insertion:\n\n")
mylinklist.printlist()
mylinklist.insert(12,8)