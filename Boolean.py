class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    def print(self):
        temp=self.head
        prev=None
        while temp:
            prev=temp
            temp=temp.next
            print(prev.next==temp)
linked=LinkedList()
linked.push(1)
linked.push(2)
linked.push(3)
linked.print()
            
        
