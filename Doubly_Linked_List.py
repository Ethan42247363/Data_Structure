class Node:
    def __init__(self,data=None):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def add(self,data):
        if self.head==None:
           self.head=Node(data)
        else:
            currentNode=self.head
            while currentNode.next!=None:
                currentNode=currentNode.next

            nwNode=Node(data)
            nwNode.prev=currentNode
            currentNode.next=nwNode

    def traverse(self):
        if self.head==None:
            print("Error")
        else:
            currentNode=self.head
            while currentNode.next!=None:
                print(currentNode.data,"<->",end=" ")
                currentNode=currentNode.next
            print(currentNode.data,"<--> End")

    def insert(self,index,nwdata):
        if self.head==None and index==0:
            self.head=Node(nwdata)
        elif self.head==None and index>0:
            print("Error")
        else:
            currentNode=self.head
            prevNode=None
            i=0
            while i!=index and currentNode.next!=None:
                i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if i!=index and currentNode.next==None:
                print("Error")
            if i==index:
                nwNode=Node(nwdata)
                nwNode.next=currentNode
                currentNode.prev=nwNode
                if prevNode==None:
                    self.head=nwNode
                else:
                    prevNode.next=nwNode
                    nwNode.prev=prevNode

                
    def search(self,index):
        currentNode=self.head
        prevNode=None
        i=0
        if self.head==None:
            print("Error")
        else:
            while i!=index and currentNode.next!=None:
                i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if i!=index and currentNode.next==None:
                print("Error")
            else:
                print(currentNode.data)

    def delete(self,index):
        if self.head==None:
            print("Error")
        else:
            currentNode=self.head
            prevNode=None
            i=0
            while i!=index and currentNode.next!=None:
                i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if i!=index and currentNode.next==None:
                print("Error")
            else:
                prevNode.next=currentNode.next
                currentNode.next.prev=prevNode
        
    def update(self,index,nwdata):
        if self.head==None:
            print("Error")
        else:
            currentNode=self.head
            prevNode=None
            i=0
            while i!=index and currentNode.next!=None:
                i+=1
                prevNode=currentNode
                currentNode=currentNode.next
            if i!=index and currentNode.next==None:
                print("Error")
            else:
                currentNode.data=nwdata
                
if __name__=='__main__':
    ll=DoublyLinkedList( )
    ll.add(16)
    ll.add(4)
    ll.add(7)
    ll.add(9)
    ll.add(2)
    ll.add(5)
    ll.add(9)
    ll.traverse()        #16,4,7,9,2,5,9
    ll.search(4)         #2
    ll.insert(2,18)
    ll.traverse()        #16,4,18,7,9,2,5,9
    ll.delete(3)
    ll.traverse()        #16,4,18,9,2,5,9
    ll.update(2,20)
    ll.traverse()        #16,4,20,9,2,5,9
