class node:
	def __init__(self,data,next=None):
		self.data=data
		self.next=next
class linkedlist:
	def __init(self):
		self.head=None
	def first(self,newdata):
		newnode=node(newdata)
		newnode.next=self.head
		self.head=newnode
	def insert(self,newdata,p):
		temp=self.head
		if p==0:
			return node(newdata,self.head)
		while p>1:
			self.head=self.head.next
			p-=1
		self.head.next=node(newdata,self.head.next)
		return temp
		'''temp=self.head
		c=0
		while(temp):
			if c==p:
				prevnode=temp.data
			c+=1
			temp=temp.next
		if prevnode is None:
			print("prevnode is null")
			return
		newnode=node(newdata)
		newnode.next=prevnode.next
		prevnode.next=newnode'''
	def last(self,newdata):
		newnode=node(newdata)
		if self.head is None:
			self.head=newnode
			newnode.next=None
			return
		last=self.head
		while(last.next):
			last=last.next
		last.next=newnode
		newnode.next=None

	def printl(self):
		temp=self.head
		while(temp):
			print(temp.data,end=" ")
			temp=temp.next
		
			
if __name__=="__main__":
	llist=linkedlist()
	llist.head=node(1)
	llist.first(343)
	llist.last(98655)
	llist.insert(676,2)
	
	llist.printl()