class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def insert(self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head = new_node
    def insertafter(self,prev,newdata):
	    if prev is None:
		    print("prev shld exist ")
		    return
	    new_node=Node(newdata)
	    new_node.next=prev.next
	    prev.next= new_node

    def insertlast(self,newdata):
	    new_node=Node(newdata)
	    if self.head is None:
		    self.head=new_node
		    return
	    last = self.head
	    while (last.next):
		    last = last.next
	    last.next=new_node
	    

	def printList(self):
        temp = self.head
        while (temp):
        	print(temp.data,end=" ")
        	temp = temp.next

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.data == data:
                found = True
            else:
                current = current.next
        if current is None:
             raise ValueError("Data not in list")
        return current
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.next
        else:
            previous.next=current.next
if __name__ == '__main__':
	llist = LinkedList()
	llist.insertlast(6)
    llist.insert(7)
    llist.insert(1)
    llist.insertlast(4)
    llist.insertafter(llist.head.next, 8)
    llist.printList()